#!/usr/bin/env python3
"""
Demo Mode - Generate Sample Reports
Creates meal planning reports with dummy data to demonstrate functionality
No Mews credentials required!
"""

from datetime import datetime, timedelta
import json
from pathlib import Path
import random

from meal_planner import MealPlanner
from report_generator import ReportGenerator


class DemoDataGenerator:
    """Generates realistic demo data for testing"""

    def __init__(self):
        self.meal_products = {
            'breakfast-001': {
                'Id': 'breakfast-001',
                'Names': {'en-US': 'Continental Breakfast'},
                'ChargingMode': 'PerPersonPerTimeUnit',
                'Classifications': {'Food': True}
            },
            'lunch-001': {
                'Id': 'lunch-001',
                'Names': {'en-US': 'Lunch Buffet'},
                'ChargingMode': 'PerPersonPerTimeUnit',
                'Classifications': {'Food': True}
            },
            'dinner-001': {
                'Id': 'dinner-001',
                'Names': {'en-US': 'Dinner Service'},
                'ChargingMode': 'PerPersonPerTimeUnit',
                'Classifications': {'Food': True}
            },
            'conference-001': {
                'Id': 'conference-001',
                'Names': {'en-US': 'Conference Package'},
                'ChargingMode': 'PerPersonPerTimeUnit',
                'Classifications': {'Food': True}
            }
        }

    def generate_weekly_data(self, start_date: datetime) -> dict:
        """Generate demo meal planning data for a week"""

        daily_breakdown = []
        current_date = start_date.date()

        # Base occupancy that varies by day of week
        base_occupancy = {
            0: 45,   # Monday
            1: 52,   # Tuesday
            2: 48,   # Wednesday
            3: 51,   # Thursday
            4: 55,   # Friday
            5: 62,   # Saturday
            6: 58    # Sunday
        }

        for i in range(7):
            day_of_week = current_date.weekday()
            guests = base_occupancy[day_of_week] + random.randint(-3, 3)

            # Meal participation rates
            breakfast_rate = random.uniform(0.82, 0.88)
            lunch_rate = random.uniform(0.25, 0.35)
            dinner_rate = random.uniform(0.88, 0.95)

            breakfast = int(guests * breakfast_rate)
            lunch = int(guests * lunch_rate)
            dinner = int(guests * dinner_rate)

            # Add conference meals on some days
            conference = 0
            if day_of_week == 2:  # Wednesday
                conference = 25
            elif day_of_week == 4:  # Friday
                conference = 15

            daily_breakdown.append({
                'date': current_date.strftime('%Y-%m-%d'),
                'day_name': current_date.strftime('%A'),
                'breakfast': breakfast,
                'lunch': lunch,
                'dinner': dinner,
                'conference': conference,
                'total_guests': guests,
                'reservation_count': random.randint(20, 35),
                'notes': {}
            })

            current_date += timedelta(days=1)

        # Calculate totals
        weekly_totals = {
            'breakfast': sum(day['breakfast'] for day in daily_breakdown),
            'lunch': sum(day['lunch'] for day in daily_breakdown),
            'dinner': sum(day['dinner'] for day in daily_breakdown),
            'conference': sum(day['conference'] for day in daily_breakdown),
            'total_guests': sum(day['total_guests'] for day in daily_breakdown)
        }

        return {
            'start_date': start_date.strftime('%Y-%m-%d'),
            'end_date': (start_date + timedelta(days=7)).strftime('%Y-%m-%d'),
            'generated_at': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC'),
            'daily_breakdown': daily_breakdown,
            'weekly_totals': weekly_totals,
            'notes': {}
        }


def add_demo_notes(report: dict) -> dict:
    """Add realistic demo notes to the report"""

    demo_notes = {
        report['daily_breakdown'][0]['date']: {
            'general': 'Corporate conference group checking in',
            'dietary': '2 guests lactose intolerant, 1 vegan',
            'location': 'Conference meals in Grand Ballroom',
            'special': 'Coffee & tea setup needed by 8:00 AM'
        },
        report['daily_breakdown'][1]['date']: {
            'dietary': 'Wedding party - 2 nut allergies in group'
        },
        report['daily_breakdown'][2]['date']: {
            'general': 'Tech Summit Conference - 80 attendees',
            'location': 'Breakfast in Main Hall, Lunch in Conference Room A',
            'dietary': '5 vegetarian meals for dinner',
            'special': 'Coffee breaks at 10am and 3pm'
        },
        report['daily_breakdown'][4]['date']: {
            'dietary': 'VIP guest in Suite 305 - shellfish allergy',
            'special': 'Chef\'s special menu for Friday dinner service'
        }
    }

    # Add notes to daily breakdown
    for day in report['daily_breakdown']:
        if day['date'] in demo_notes:
            day['notes'] = demo_notes[day['date']]

    return report


def print_demo_report(report: dict):
    """Print report in console format"""
    print("\n" + "=" * 80)
    print(f"KITCHEN MEAL PLANNING REPORT (DEMO)".center(80))
    print(f"Week of {report['start_date']} to {report['end_date']}".center(80))
    print(f"Generated: {report['generated_at']}".center(80))
    print("=" * 80 + "\n")

    print(f"{'Date':<12} {'Day':<10} {'Guests':<8} {'Breakfast':<10} {'Lunch':<10} {'Dinner':<10} {'Conf':<8}")
    print("-" * 80)

    for day in report['daily_breakdown']:
        print(f"{day['date']:<12} {day['day_name']:<10} {day['total_guests']:<8} "
              f"{day['breakfast']:<10} {day['lunch']:<10} {day['dinner']:<10} {day['conference']:<8}")

        # Print notes
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

    print("-" * 80)
    totals = report['weekly_totals']
    print(f"{'WEEKLY TOTAL':<22} {totals['total_guests']:<8} "
          f"{totals['breakfast']:<10} {totals['lunch']:<10} {totals['dinner']:<10} {totals['conference']:<8}")
    print("=" * 80 + "\n")


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='Demo mode - Generate sample meal planning reports (no Mews credentials needed)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # View demo report in console
  python3 demo.py

  # Generate demo Excel report
  python3 demo.py --format excel

  # Generate demo Excel and PDF reports
  python3 demo.py --format excel pdf

  # Without notes
  python3 demo.py --no-notes --format excel
        """
    )

    parser.add_argument(
        '--start-date',
        type=str,
        help='Start date (YYYY-MM-DD). Defaults to next Monday.'
    )

    parser.add_argument(
        '--format',
        nargs='+',
        choices=['console', 'excel', 'pdf', 'json'],
        default=['console'],
        help='Output format(s). Default: console'
    )

    parser.add_argument(
        '--no-notes',
        action='store_true',
        help='Generate report without demo notes'
    )

    parser.add_argument(
        '--output-dir',
        type=str,
        default='./demo_reports',
        help='Output directory. Default: ./demo_reports'
    )

    parser.add_argument(
        '--notes',
        type=str,
        help='Use custom detailed notes file (e.g., notes_detailed.example.json)'
    )

    parser.add_argument(
        '--detailed',
        action='store_true',
        help='Generate detailed report with service times and prep lists'
    )

    parser.add_argument(
        '--daily-pages',
        action='store_true',
        help='Generate clean daily pages format (one page per day with timeline)'
    )

    args = parser.parse_args()

    # Determine start date
    if args.start_date:
        try:
            start_date = datetime.strptime(args.start_date, '%Y-%m-%d')
        except ValueError:
            print(f"Error: Invalid date format '{args.start_date}'. Use YYYY-MM-DD")
            return
    else:
        # Default to next Monday
        today = datetime.now()
        days_ahead = 0 - today.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        start_date = today + timedelta(days=days_ahead)
        start_date = start_date.replace(hour=0, minute=0, second=0, microsecond=0)

    print("=" * 80)
    print("DEMO MODE - Sample Meal Planning Report".center(80))
    print("=" * 80)
    print(f"\nGenerating demo report for week starting: {start_date.strftime('%Y-%m-%d')}")
    print("Note: This is sample data to demonstrate the application")
    print("To use with real Mews data, configure config.py and run main.py\n")

    # Generate demo data
    generator = DemoDataGenerator()
    report = generator.generate_weekly_data(start_date)

    # Load custom notes if provided
    if args.notes:
        try:
            with open(args.notes, 'r') as f:
                custom_notes = json.load(f)
            # Apply notes to report
            for day in report['daily_breakdown']:
                if day['date'] in custom_notes:
                    day['notes'] = custom_notes[day['date']]
            print(f"✅ Loaded custom notes from: {args.notes}")
        except FileNotFoundError:
            print(f"Warning: Notes file not found: {args.notes}")
        except json.JSONDecodeError as e:
            print(f"Warning: Invalid JSON in notes file: {e}")
    # Add demo notes unless disabled or custom notes provided
    elif not args.no_notes:
        report = add_demo_notes(report)
        print("✅ Demo notes included")

    # Output in requested formats
    if 'console' in args.format:
        print_demo_report(report)

    # Create output directory if needed
    if any(fmt in args.format for fmt in ['excel', 'pdf', 'json']):
        output_dir = Path(args.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        week_str = start_date.strftime('%Y-%m-%d')
        base_filename = f"demo_meal_plan_{week_str}"

        # Use appropriate generator based on flags
        if args.daily_pages:
            from daily_page_generator import DailyPageGenerator
            generator = DailyPageGenerator(report)
            base_filename = f"demo_meal_plan_daily_{week_str}"

            if 'excel' in args.format:
                excel_file = output_dir / f"{base_filename}.xlsx"
                generator.generate_daily_pages_excel(str(excel_file))

            if 'pdf' in args.format:
                pdf_file = output_dir / f"{base_filename}.pdf"
                generator.generate_daily_pages_pdf(str(pdf_file))
        elif args.detailed:
            from detailed_report_generator import DetailedReportGenerator
            generator = DetailedReportGenerator(report)
            base_filename = f"demo_meal_plan_detailed_{week_str}"

            if 'excel' in args.format:
                excel_file = output_dir / f"{base_filename}.xlsx"
                generator.generate_detailed_excel(str(excel_file))
        else:
            generator = ReportGenerator(report)

            if 'excel' in args.format:
                excel_file = output_dir / f"{base_filename}.xlsx"
                generator.generate_excel(str(excel_file))

        if 'pdf' in args.format:
            pdf_file = output_dir / f"{base_filename}.pdf"
            if not args.detailed and not args.daily_pages:
                generator.generate_pdf(str(pdf_file))
            elif args.detailed:
                print("Note: Detailed PDF not yet implemented, use Excel format")

        if 'json' in args.format:
            json_file = output_dir / f"{base_filename}.json"
            generator.generate_json(str(json_file))

        print(f"\n✅ Demo reports saved to: {output_dir}/")
        print(f"\nTo view the files:")
        print(f"  cd {output_dir}")
        print(f"  open {base_filename}.xlsx    # or .pdf")

    print("\n" + "=" * 80)
    print("This is sample data to show you how the reports look.".center(80))
    print("When ready, get Mews credentials and use main.py for real data.".center(80))
    print("=" * 80 + "\n")


if __name__ == '__main__':
    main()
