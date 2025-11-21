"""
Kitchen Meal Planner - Generates weekly meal forecasts for kitchen staff
Analyzes reservations and meal product orders to forecast breakfast, lunch, dinner counts
"""

from datetime import datetime, timedelta
from typing import Dict, List, Tuple
from collections import defaultdict
from mews_client import MewsAPIClient


class MealPlanner:
    """Generates meal planning reports from Mews reservation data"""

    def __init__(self, client: MewsAPIClient):
        """
        Initialize meal planner

        Args:
            client: MewsAPIClient instance
        """
        self.client = client
        self.meal_products = {}
        self.services = {}
        self.age_categories = {}

    def load_configuration(self):
        """Load products, services, and age categories from Mews"""
        print("Loading Mews configuration...")

        # Load services
        services = self.client.get_services()
        for service in services:
            self.services[service['Id']] = service
        print(f"Loaded {len(self.services)} services")

        # Load products (meals)
        products = self.client.get_products()
        for product in products:
            self.meal_products[product['Id']] = product
        print(f"Loaded {len(self.meal_products)} products")

        # Load age categories
        age_categories = self.client.get_age_categories()
        for category in age_categories:
            self.age_categories[category['Id']] = category
        print(f"Loaded {len(self.age_categories)} age categories")

    def identify_meal_products(self) -> Dict[str, List[Dict]]:
        """
        Identify which products are meals (breakfast, lunch, dinner)
        Based on product names and classifications

        Returns:
            Dictionary with meal types as keys and product lists as values
        """
        meals = {
            'breakfast': [],
            'lunch': [],
            'dinner': [],
            'conference': [],
            'other': []
        }

        for product_id, product in self.meal_products.items():
            # Check product names in English
            name = product.get('Names', {}).get('en-US', '').lower()
            classifications = product.get('Classifications', {})

            # Identify meal type by name
            if any(keyword in name for keyword in ['breakfast', 'bfast', 'morning']):
                meals['breakfast'].append(product)
            elif any(keyword in name for keyword in ['lunch', 'noon']):
                meals['lunch'].append(product)
            elif any(keyword in name for keyword in ['dinner', 'evening', 'supper']):
                meals['dinner'].append(product)
            elif any(keyword in name for keyword in ['conference', 'meeting', 'event', 'banquet']):
                meals['conference'].append(product)
            elif classifications.get('Food'):
                meals['other'].append(product)

        return meals

    def calculate_meal_counts(self, start_date: datetime, end_date: datetime) -> Dict:
        """
        Calculate meal counts for each day in the date range

        Args:
            start_date: Start date for forecast
            end_date: End date for forecast

        Returns:
            Dictionary with daily meal counts
        """
        print(f"\nCalculating meal counts from {start_date.date()} to {end_date.date()}...")

        # Get reservations
        reservation_data = self.client.get_reservations(start_date, end_date)
        reservations = reservation_data.get('Reservations', [])
        print(f"Found {len(reservations)} reservations")

        # Identify meal products
        meal_products = self.identify_meal_products()

        # Initialize daily counts
        daily_counts = defaultdict(lambda: {
            'breakfast': 0,
            'lunch': 0,
            'dinner': 0,
            'conference': 0,
            'total_guests': 0,
            'reservations': []
        })

        # Process each reservation
        for reservation in reservations:
            # Get person counts
            total_persons = self._get_total_persons(reservation)

            # Get reservation dates
            start_utc = datetime.fromisoformat(reservation['StartUtc'].replace('Z', '+00:00'))
            end_utc = datetime.fromisoformat(reservation['EndUtc'].replace('Z', '+00:00'))

            # Get product orders (meals included in reservation)
            product_orders = reservation.get('ProductOrders', [])

            # Process each day of the stay
            current_date = start_utc.date()
            end_date_obj = end_utc.date()

            while current_date < end_date_obj:
                date_key = current_date.strftime('%Y-%m-%d')

                # Add total guests
                daily_counts[date_key]['total_guests'] += total_persons

                # Track reservation
                daily_counts[date_key]['reservations'].append({
                    'id': reservation['Id'],
                    'guests': total_persons,
                    'state': reservation['State']
                })

                # Check which meal products are included
                for product_order in product_orders:
                    product_id = product_order['ProductId']
                    product = self.meal_products.get(product_id)

                    if not product:
                        continue

                    # Check if this product order is active on current_date
                    po_start = datetime.fromisoformat(product_order.get('StartUtc', reservation['StartUtc']).replace('Z', '+00:00')).date()
                    po_end = datetime.fromisoformat(product_order.get('EndUtc', reservation['EndUtc']).replace('Z', '+00:00')).date()

                    if po_start <= current_date < po_end:
                        # Determine meal type and add count
                        for meal_type, products in meal_products.items():
                            if product in products:
                                # Count considers the charging mode
                                count = product_order.get('Count', 1)
                                charging_mode = product.get('ChargingMode', '')

                                if charging_mode == 'PerPersonPerTimeUnit':
                                    # Each person gets the meal
                                    daily_counts[date_key][meal_type] += total_persons * count
                                else:
                                    # Fixed count regardless of persons
                                    daily_counts[date_key][meal_type] += count

                current_date += timedelta(days=1)

        return dict(daily_counts)

    def _get_total_persons(self, reservation: Dict) -> int:
        """
        Calculate total persons from PersonCounts

        Args:
            reservation: Reservation object

        Returns:
            Total number of persons
        """
        person_counts = reservation.get('PersonCounts', [])
        total = sum(pc.get('Count', 0) for pc in person_counts)

        # Fallback to AdultCount + ChildCount if PersonCounts not available
        if total == 0:
            total = reservation.get('AdultCount', 0) + reservation.get('ChildCount', 0)

        return total

    def generate_weekly_report(self, start_date: datetime, notes: Dict = None) -> Dict:
        """
        Generate a weekly meal planning report

        Args:
            start_date: Start date (will generate 7 days from this date)
            notes: Optional dictionary with notes per date

        Returns:
            Weekly report data
        """
        end_date = start_date + timedelta(days=7)

        # Load configuration if not already loaded
        if not self.meal_products:
            self.load_configuration()

        # Calculate meal counts
        daily_counts = self.calculate_meal_counts(start_date, end_date)

        # Build weekly report
        report = {
            'start_date': start_date.strftime('%Y-%m-%d'),
            'end_date': end_date.strftime('%Y-%m-%d'),
            'generated_at': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC'),
            'daily_breakdown': [],
            'notes': notes or {}
        }

        # Process each day
        current_date = start_date.date()
        for i in range(7):
            date_key = current_date.strftime('%Y-%m-%d')
            day_data = daily_counts.get(date_key, {
                'breakfast': 0,
                'lunch': 0,
                'dinner': 0,
                'conference': 0,
                'total_guests': 0,
                'reservations': []
            })

            # Get notes for this date
            day_notes = notes.get(date_key, {}) if notes else {}

            report['daily_breakdown'].append({
                'date': date_key,
                'day_name': current_date.strftime('%A'),
                'breakfast': day_data['breakfast'],
                'lunch': day_data['lunch'],
                'dinner': day_data['dinner'],
                'conference': day_data['conference'],
                'total_guests': day_data['total_guests'],
                'reservation_count': len(day_data['reservations']),
                'notes': day_notes
            })

            current_date += timedelta(days=1)

        # Calculate weekly totals
        report['weekly_totals'] = {
            'breakfast': sum(day['breakfast'] for day in report['daily_breakdown']),
            'lunch': sum(day['lunch'] for day in report['daily_breakdown']),
            'dinner': sum(day['dinner'] for day in report['daily_breakdown']),
            'conference': sum(day['conference'] for day in report['daily_breakdown']),
            'total_guests': sum(day['total_guests'] for day in report['daily_breakdown']),
        }

        return report

    def print_report(self, report: Dict):
        """
        Print report to console in a readable format

        Args:
            report: Report data from generate_weekly_report
        """
        print("\n" + "=" * 80)
        print(f"KITCHEN MEAL PLANNING REPORT".center(80))
        print(f"Week of {report['start_date']} to {report['end_date']}".center(80))
        print(f"Generated: {report['generated_at']}".center(80))
        print("=" * 80 + "\n")

        # Daily breakdown
        print(f"{'Date':<12} {'Day':<10} {'Guests':<8} {'Breakfast':<10} {'Lunch':<10} {'Dinner':<10} {'Conf':<8}")
        print("-" * 80)

        for day in report['daily_breakdown']:
            print(f"{day['date']:<12} {day['day_name']:<10} {day['total_guests']:<8} "
                  f"{day['breakfast']:<10} {day['lunch']:<10} {day['dinner']:<10} {day['conference']:<8}")

            # Print notes if available
            notes = day.get('notes', {})
            if notes:
                if notes.get('general'):
                    print(f"  NOTE: {notes['general']}")
                if notes.get('dietary'):
                    print(f"  DIETARY: {notes['dietary']}")
                if notes.get('location'):
                    print(f"  LOCATION: {notes['location']}")
                if notes.get('special'):
                    print(f"  SPECIAL: {notes['special']}")

        # Weekly totals
        print("-" * 80)
        totals = report['weekly_totals']
        print(f"{'WEEKLY TOTAL':<22} {totals['total_guests']:<8} "
              f"{totals['breakfast']:<10} {totals['lunch']:<10} {totals['dinner']:<10} {totals['conference']:<8}")
        print("=" * 80 + "\n")
