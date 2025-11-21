#!/usr/bin/env python3
"""
Kitchen Meal Planner - Main Application
Generates weekly meal planning reports for kitchen and restaurant staff
"""

import argparse
from datetime import datetime, timedelta
import sys
import json
from pathlib import Path

from mews_client import MewsAPIClient
from meal_planner import MealPlanner
from report_generator import ReportGenerator
from detailed_report_generator import DetailedReportGenerator


def load_config():
    """Load configuration from config.py"""
    try:
        import config
        return config
    except ImportError:
        print("Error: config.py not found!")
        print("Please create config.py with your Mews credentials.")
        print("See config.example.py for reference.")
        sys.exit(1)


def parse_date(date_str: str) -> datetime:
    """
    Parse date string to datetime

    Args:
        date_str: Date string in YYYY-MM-DD format

    Returns:
        datetime object
    """
    try:
        return datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        print(f"Error: Invalid date format '{date_str}'. Use YYYY-MM-DD")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description='Generate weekly meal planning reports for kitchen staff',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate report for current week
  python main.py

  # Generate report for specific date
  python main.py --start-date 2024-01-15

  # Generate Excel and PDF reports
  python main.py --format excel pdf

  # Include notes with dietary restrictions and special requirements
  python main.py --notes notes.json --format excel pdf

  # Specify output directory
  python main.py --output-dir ./reports
        """
    )

    parser.add_argument(
        '--start-date',
        type=str,
        help='Start date for the weekly report (YYYY-MM-DD). Defaults to next Monday.'
    )

    parser.add_argument(
        '--format',
        nargs='+',
        choices=['console', 'excel', 'pdf', 'json'],
        default=['console'],
        help='Output format(s). Default: console'
    )

    parser.add_argument(
        '--output-dir',
        type=str,
        default='./reports',
        help='Output directory for reports. Default: ./reports'
    )

    parser.add_argument(
        '--notes',
        type=str,
        help='Path to JSON file with notes/comments for the week'
    )

    parser.add_argument(
        '--detailed',
        action='store_true',
        help='Generate detailed report with service times, prep lists, and staffing'
    )

    args = parser.parse_args()

    # Determine start date
    if args.start_date:
        start_date = parse_date(args.start_date)
    else:
        # Default to next Monday
        today = datetime.now()
        days_ahead = 0 - today.weekday()  # Monday is 0
        if days_ahead <= 0:
            days_ahead += 7
        start_date = today + timedelta(days=days_ahead)
        start_date = start_date.replace(hour=0, minute=0, second=0, microsecond=0)

    print(f"Kitchen Meal Planning Report")
    print(f"Generating report for week starting: {start_date.strftime('%Y-%m-%d')}")
    print("")

    # Load configuration
    config = load_config()

    # Initialize Mews client
    try:
        client = MewsAPIClient(
            client_token=config.CLIENT_TOKEN,
            access_token=config.ACCESS_TOKEN,
            base_url=config.BASE_URL
        )
    except AttributeError as e:
        print(f"Error: Missing configuration in config.py: {e}")
        print("Please check config.example.py for required fields.")
        sys.exit(1)

    # Initialize meal planner
    planner = MealPlanner(client)

    # Load notes if provided
    notes = None
    if args.notes:
        try:
            with open(args.notes, 'r') as f:
                notes = json.load(f)
            print(f"Loaded notes from: {args.notes}\n")
        except FileNotFoundError:
            print(f"Warning: Notes file not found: {args.notes}")
        except json.JSONDecodeError as e:
            print(f"Warning: Invalid JSON in notes file: {e}")

    # Generate report
    try:
        report = planner.generate_weekly_report(start_date, notes)
    except Exception as e:
        print(f"Error generating report: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

    # Output report in requested formats
    if 'console' in args.format:
        planner.print_report(report)

    # Create output directory if needed
    if any(fmt in args.format for fmt in ['excel', 'pdf', 'json']):
        output_dir = Path(args.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        # Generate filename base
        week_str = start_date.strftime('%Y-%m-%d')
        base_filename = f"meal_plan_{week_str}"

        # Choose generator based on detailed flag
        if args.detailed:
            generator = DetailedReportGenerator(report)
            base_filename = f"meal_plan_detailed_{week_str}"

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
            if not args.detailed:
                generator.generate_pdf(str(pdf_file))
            else:
                print("Note: Detailed PDF not yet implemented, use Excel format for detailed reports")

        if 'json' in args.format:
            json_file = output_dir / f"{base_filename}.json"
            generator.generate_json(str(json_file))

    print("\nReport generation complete!")


if __name__ == '__main__':
    main()
