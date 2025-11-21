# Demo Mode - Try Without Mews Credentials

Don't have Mews credentials yet? No problem! Use demo mode to see exactly how the reports look with realistic sample data.

## What is Demo Mode?

Demo mode generates realistic sample meal planning data so you can:
- ✅ See how reports look before connecting to Mews
- ✅ Test all output formats (Console, Excel, PDF, JSON)
- ✅ Experiment with the notes feature
- ✅ Show your team what the tool can do
- ✅ No Mews credentials required!

## Quick Start

```bash
# View demo report in console
python3 demo.py

# Generate Excel report
python3 demo.py --format excel

# Generate Excel and PDF reports
python3 demo.py --format excel pdf

# All formats including JSON
python3 demo.py --format excel pdf json
```

## Demo Data Includes

The demo generates realistic data for a typical hotel week:

**Realistic Numbers:**
- 45-64 guests per day (varies by day of week)
- ~85% breakfast participation
- ~30% lunch participation
- ~90% dinner participation
- Conference meals on select days

**Sample Notes:**
- Dietary restrictions (lactose intolerant, vegan, nut allergies, etc.)
- Conference locations (Grand Ballroom, Conference Room A)
- Special requirements (coffee setups, VIP guests)
- General reminders (event groups checking in)

## Command Options

```bash
# Custom date
python3 demo.py --start-date 2024-02-05 --format excel

# Without notes
python3 demo.py --no-notes --format excel

# Custom output directory
python3 demo.py --format excel pdf --output-dir ./my_demos

# Help
python3 demo.py --help
```

## What You'll See

### Console Output
```
================================================================================
                      KITCHEN MEAL PLANNING REPORT (DEMO)
                        Week of 2025-11-24 to 2025-12-01
================================================================================

Date         Day        Guests   Breakfast  Lunch      Dinner     Conf
--------------------------------------------------------------------------------
2025-11-24   Monday     46       39         15         43         0
  NOTE: Corporate conference group checking in
  DIETARY: 2 guests lactose intolerant, 1 vegan
  LOCATION: Conference meals in Grand Ballroom
  SPECIAL: Coffee & tea setup needed by 8:00 AM
2025-11-25   Tuesday    55       46         18         49         0
  DIETARY: Wedding party - 2 nut allergies in group
...
```

### Excel Report
- Professional formatting with colors
- Meal counts in table format
- Notes appear below each day (italic, gray background)
- Weekly totals highlighted
- Ready to print or edit

### PDF Report
- Professional document ready for printing
- Notes integrated into the table
- Perfect for posting in the kitchen
- Cannot be edited (official record)

## Output Files

Demo reports are saved to `demo_reports/` directory:
- `demo_meal_plan_YYYY-MM-DD.xlsx` - Excel file
- `demo_meal_plan_YYYY-MM-DD.pdf` - PDF file
- `demo_meal_plan_YYYY-MM-DD.json` - JSON file

## Opening the Files

**macOS:**
```bash
open demo_reports/demo_meal_plan_2025-11-24.xlsx
open demo_reports/demo_meal_plan_2025-11-24.pdf
```

**Linux:**
```bash
xdg-open demo_reports/demo_meal_plan_2025-11-24.xlsx
xdg-open demo_reports/demo_meal_plan_2025-11-24.pdf
```

**Windows:**
```bash
start demo_reports\demo_meal_plan_2025-11-24.xlsx
start demo_reports\demo_meal_plan_2025-11-24.pdf
```

Or just open them from your file browser!

## Use Cases for Demo Mode

### 1. Evaluate the Tool
Try it out before getting Mews credentials to see if it meets your needs.

### 2. Show Your Team
Generate sample reports to show kitchen staff and managers what the tool produces.

### 3. Test Workflows
Practice using the tool before connecting to real data.

### 4. Print Samples
Print demo reports to see how they look on paper.

### 5. Training
Use demo data to train staff on reading the reports.

## What's Different from Real Mode?

| Feature | Demo Mode | Real Mode (main.py) |
|---------|-----------|---------------------|
| Data source | Generated sample data | Real Mews reservations |
| Credentials | Not required | Mews API credentials required |
| Notes | Pre-defined demo notes | Load from your notes.json file |
| Accuracy | Realistic but fake | Actual reservation data |
| Output formats | Same (Console, Excel, PDF, JSON) | Same |

## When to Switch to Real Mode

Once you have Mews credentials:

1. **Get credentials** (see [GETTING_STARTED.md](GETTING_STARTED.md))
2. **Configure** `config.py` with your tokens
3. **Use** `main.py` instead of `demo.py`:

```bash
# Real data
python3 main.py --format excel pdf

# Real data with your notes
python3 main.py --notes weekly-notes.json --format excel pdf
```

## Tips

- **Save demo files**: Keep them as examples for comparison
- **Show stakeholders**: Use demo mode to get buy-in before setup
- **Test printing**: Print demo PDFs to verify your printer settings
- **Practice notes**: Use `--no-notes` to see reports without notes
- **Different dates**: Generate multiple weeks to see variety

## Comparison: Demo vs Real

```bash
# Generate demo report
python3 demo.py --format excel pdf

# When ready, generate real report
python3 main.py --format excel pdf
```

The output format is identical - only the data source changes!

---

**Ready to try it?**

```bash
python3 demo.py --format excel pdf
```

Then check the `demo_reports/` folder to see your generated reports! 🎉
