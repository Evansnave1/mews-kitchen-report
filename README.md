# Kitchen Meal Planner for Mews

A simple Python application that generates weekly meal planning reports for kitchen and restaurant staff using the Mews Connector API.

## What It Does

This tool helps kitchen chefs and restaurant waiters plan their weekly operations by providing accurate forecasts of:

- **Breakfast counts** - How many guests need breakfast each day
- **Lunch counts** - How many guests need lunch each day
- **Dinner counts** - How many guests need dinner each day
- **Conference meals** - Special event/conference meal requirements
- **Total guest counts** - Total number of guests staying each day

## Features

- ✅ Generates weekly meal forecasts based on confirmed reservations
- ✅ Identifies meal products automatically from reservation data
- ✅ Supports multiple output formats: Console, Excel, PDF, JSON
- ✅ Simple command-line interface
- ✅ Configurable for demo and production Mews environments

## Requirements

- Python 3.7 or higher
- Mews API credentials (Client Token and Access Token)
- Internet connection to access Mews API

## 🚀 Try It Now - Demo Mode!

**Don't have Mews credentials yet?** No problem! Try demo mode to see how the reports look:

```bash
cd kitchen-meal-planner
pip3 install -r requirements.txt
python3 demo.py --format excel pdf
```

Open `demo_reports/` to see your generated reports! See [DEMO_MODE.md](DEMO_MODE.md) for details.

---

## Quick Start

**New users:** See [GETTING_STARTED.md](GETTING_STARTED.md) for detailed setup instructions!

### Installation

1. **Install dependencies**
   ```bash
   cd kitchen-meal-planner
   pip install -r requirements.txt
   ```

2. **Test installation**
   ```bash
   python test_installation.py
   ```
   This verifies all dependencies are installed correctly.

3. **Configure your Mews credentials**
   ```bash
   cp config.example.py config.py
   ```

   Then edit `config.py` and add your Mews credentials:
   ```python
   CLIENT_TOKEN = "your-client-token-here"
   ACCESS_TOKEN = "your-access-token-here"
   BASE_URL = "https://api.mews-demo.com"  # or https://api.mews.com for production
   ```

4. **Verify setup**
   ```bash
   python test_installation.py
   ```
   Should show all green checkmarks ✅

## Getting Mews Credentials

### For Testing (Demo Environment)
You can use the public demo credentials from Mews:
- Check the [Getting Started guide](../gitbook-connector-api/getting-started/README.md) in the API documentation

### For Production
1. Contact your Mews account manager or [partnersuccess@mews.com](mailto:partnersuccess@mews.com)
2. Request API access and get your Client Token
3. Generate an Access Token for your property in Mews Operations

## Usage

### Basic Usage - Current Week

Generate a report for the upcoming week (starting next Monday):

```bash
python main.py
```

This will display the report in your console:

```
================================================================================
                       KITCHEN MEAL PLANNING REPORT
                   Week of 2024-01-15 to 2024-01-22
                   Generated: 2024-01-12 10:30:00 UTC
================================================================================

Date         Day        Guests   Breakfast  Lunch      Dinner     Conf
--------------------------------------------------------------------------------
2024-01-15   Monday     45       38         12         42         0
  NOTE: Conference group checking in - Corporate event
  DIETARY: 2 guests lactose intolerant, 1 vegan
  LOCATION: Conference meals in Grand Ballroom
  SPECIAL: Coffee & tea setup needed by 8:00 AM
2024-01-16   Tuesday    52       45         15         48         0
  DIETARY: Wedding party - 2 nut allergies in group
2024-01-17   Wednesday  48       42         18         45         25
2024-01-18   Thursday   51       44         16         48         0
2024-01-19   Friday     55       48         20         52         0
2024-01-20   Saturday   62       55         25         58         0
2024-01-21   Sunday     58       52         22         54         0
--------------------------------------------------------------------------------
WEEKLY TOTAL            371      324        128        347        25
================================================================================
```

**Note:** The example above shows notes added for Monday and Tuesday. Notes are optional - you can add them only for days that need special attention.

### Generate Excel Report

```bash
python main.py --format excel
```

This creates a formatted Excel file in the `reports/` directory that can be:
- Printed and posted in the kitchen
- Shared with the team via email
- Used for inventory planning

### Generate PDF Report

```bash
python main.py --format pdf
```

Creates a professional PDF report suitable for printing.

### Generate Multiple Formats

```bash
python main.py --format console excel pdf
```

### Specify a Custom Date

Generate report for a specific week:

```bash
python main.py --start-date 2024-02-01
```

### Custom Output Directory

```bash
python main.py --format excel pdf --output-dir ./weekly_reports
```

### Adding Notes and Comments

Add important details to your reports like dietary restrictions, conference locations, and special requirements:

```bash
python main.py --notes notes.json --format excel pdf
```

Create a `notes.json` file with your comments (see [notes.example.json](notes.example.json) for reference):

```json
{
  "2024-01-15": {
    "general": "Conference group checking in - Corporate event",
    "dietary": "2 guests lactose intolerant, 1 vegan",
    "location": "Conference meals in Grand Ballroom",
    "special": "Coffee & tea setup needed by 8:00 AM"
  },
  "2024-01-16": {
    "dietary": "Wedding party - 2 nut allergies in group"
  }
}
```

**Note types supported:**
- `general` - General notes about the day
- `dietary` - Dietary restrictions and allergies (e.g., "2 lactose intolerant", "1 vegan")
- `location` - Where meals will be served (e.g., "Conference room A", "Grand Ballroom")
- `special` - Special requests (e.g., "Extra coffee station", "Tea service at 3pm")

Notes will appear in the report directly under each day's meal counts.

## Report Output

### Console Output
- Quick view directly in terminal
- Perfect for quick checks

### Excel Output (.xlsx)
- Formatted spreadsheet with styling
- Easy to print or share
- Can be modified if needed

### PDF Output (.pdf)
- Professional looking report
- Ready to print and post in kitchen
- Cannot be modified (good for official records)

### JSON Output (.json)
- Machine-readable format
- Can be integrated with other systems
- Good for automated workflows

## Common Use Cases with Notes

### Example 1: Dietary Restrictions
Track allergies and special dietary needs:
```json
{
  "2024-01-15": {
    "dietary": "2 lactose intolerant, 1 vegan, 3 gluten-free"
  }
}
```

### Example 2: Conference Meals
Plan conference service locations:
```json
{
  "2024-01-17": {
    "general": "Tech Summit Conference - 80 attendees",
    "location": "Breakfast in Main Hall, Lunch in Conference Room A",
    "special": "Coffee breaks at 10am and 3pm"
  }
}
```

### Example 3: Special Events
Note important service details:
```json
{
  "2024-01-20": {
    "general": "VIP Wedding - Extra staff needed",
    "dietary": "Bride is vegetarian, 4 guests with nut allergies",
    "special": "Champagne brunch setup, Chef's special menu"
  }
}
```

## How It Works

1. **Connects to Mews API** - Uses your credentials to access reservation data
2. **Loads Configuration** - Retrieves all services, products, and meal configurations
3. **Identifies Meal Products** - Automatically finds breakfast, lunch, dinner products
4. **Analyzes Reservations** - Looks at all confirmed reservations for the week
5. **Counts Guests and Meals** - Calculates daily meal requirements based on:
   - Number of guests per reservation
   - Which meal products are included
   - Length of stay
6. **Generates Report** - Formats the data in your chosen format

## Understanding the Data

### Guest Counts
Total number of guests staying at the property each day (from reservations)

### Meal Counts
- Calculated based on meal products included in reservations
- Takes into account product charging modes (per person, per day, etc.)
- Only counts confirmed and active reservations

### Conference Meals
Special events or group bookings with meal requirements

## Troubleshooting

### "Error: config.py not found"
You need to create `config.py` from the example file and add your credentials.

### "API Request Error: 401 Unauthorized"
Your credentials are incorrect. Check your CLIENT_TOKEN and ACCESS_TOKEN in `config.py`.

### "No meal products found"
Your property might use different names for meal products. You can customize the keyword matching in `config.py` by setting the `MEAL_KEYWORDS` dictionary.

### Low or zero meal counts
This could mean:
- No meal products are configured in Mews
- Reservations don't have meal products attached
- The date range has no confirmed reservations

## Scheduling Automatic Reports

You can schedule this tool to run automatically using cron (Linux/Mac) or Task Scheduler (Windows).

### Example cron job (runs every Monday at 8 AM):
```bash
0 8 * * 1 cd /path/to/kitchen-meal-planner && python main.py --format excel pdf
```

## Customization

### Customizing Meal Keywords

If your property uses different names for meals, edit the `MEAL_KEYWORDS` in `config.py`:

```python
MEAL_KEYWORDS = {
    'breakfast': ['breakfast', 'petit déjeuner', 'morning buffet'],
    'lunch': ['lunch', 'déjeuner', 'midday meal'],
    'dinner': ['dinner', 'dîner', 'evening menu'],
    'conference': ['conference', 'event', 'meeting package']
}
```

## For Developers

### Project Structure
```
kitchen-meal-planner/
├── mews_client.py       # Mews API client
├── meal_planner.py      # Meal planning logic
├── report_generator.py  # Report generation (Excel, PDF)
├── main.py             # Main application entry point
├── config.example.py   # Configuration template
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

### Extending the Application

You can extend this application by:
- Adding more meal types
- Including dietary restrictions tracking
- Integrating with inventory management systems
- Adding email notification features
- Creating a web interface

## Support

For issues related to:
- **This application**: Create an issue in the project repository
- **Mews API access**: Contact [partnersuccess@mews.com](mailto:partnersuccess@mews.com)
- **Mews API documentation**: See the [Connector API docs](../gitbook-connector-api/README.md)

## License

This is an example application provided as-is for educational and practical purposes.

## Version

Version 1.0 - January 2024
