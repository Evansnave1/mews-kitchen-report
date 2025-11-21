# Test the Application Right Now - Step by Step

Follow these exact steps to test the Kitchen Meal Planner application.

## Step 1: Install Dependencies

```bash
cd kitchen-meal-planner
pip3 install -r requirements.txt
```

**What this does:** Installs the required Python libraries (requests, openpyxl, reportlab)

**Expected output:**
```
Successfully installed requests-X.X.X openpyxl-X.X.X reportlab-X.X.X
```

## Step 2: Verify Installation

```bash
python3 test_installation.py
```

**Expected output:**
```
✅ Python version OK
✅ requests installed
✅ openpyxl installed
✅ reportlab installed
✅ All project files present
⚠️  config.py not found
```

## Step 3: Get Mews Demo Credentials

**Option A: Use Mews Demo Environment (Easiest)**

The Mews API documentation provides demo credentials. To get them:

1. Visit: https://mews-systems.gitbook.io/connector-api/
2. Look for "Getting Started" or "Authentication" section
3. Find the demo credentials (they're public for testing)

**Typical demo credentials format:**
- Client Token: `E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D`
- Access Token: `C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D`
- Base URL: `https://api.mews-demo.com`

**Option B: Use Your Production Mews Account**

Contact [partnersuccess@mews.com](mailto:partnersuccess@mews.com) to get production credentials.

## Step 4: Create Configuration File

```bash
cp config.example.py config.py
```

Then edit `config.py`:

```bash
nano config.py  # or use: code config.py, vim config.py, etc.
```

Update with your credentials:

```python
CLIENT_TOKEN = "your-client-token-here"
ACCESS_TOKEN = "your-access-token-here"
BASE_URL = "https://api.mews-demo.com"
```

Save and exit.

## Step 5: Verify Configuration

```bash
python3 test_installation.py
```

**Expected output:**
```
✅ All dependencies installed correctly
✅ Configuration file ready
🎉 You're ready to use the application!
```

## Step 6: Test Basic Report Generation

```bash
python3 main.py --start-date 2024-01-15
```

**What happens:**
- Connects to Mews API
- Fetches reservations for the week of Jan 15-22, 2024
- Displays a meal planning report in your terminal

**Example output:**
```
================================================================================
                       KITCHEN MEAL PLANNING REPORT
                   Week of 2024-01-15 to 2024-01-22
================================================================================

Date         Day        Guests   Breakfast  Lunch      Dinner     Conf
--------------------------------------------------------------------------------
2024-01-15   Monday     12       10         5          11         0
2024-01-16   Tuesday    15       13         7          14         0
...
```

**If you see zeros (0) for all meals:**
- This is OK! It just means the demo environment doesn't have meal products configured
- The application is working correctly
- Focus on testing the notes and report generation features

## Step 7: Test Excel Report Generation

```bash
python3 main.py --start-date 2024-01-15 --format excel
```

**Expected output:**
```
Loading Mews configuration...
Loaded X services
Loaded X products

Calculating meal counts...
Found X reservations

Excel report saved: reports/meal_plan_2024-01-15.xlsx
Report generation complete!
```

**Check the file:**
```bash
ls -la reports/
open reports/meal_plan_2024-01-15.xlsx  # macOS
# or
xdg-open reports/meal_plan_2024-01-15.xlsx  # Linux
# or just open it from your file browser
```

## Step 8: Test Notes Feature

Create a test notes file:

```bash
cat > test-notes.json << 'EOF'
{
  "2024-01-15": {
    "general": "Test conference group",
    "dietary": "2 vegan, 1 gluten-free",
    "location": "Main dining room",
    "special": "Extra coffee needed"
  },
  "2024-01-16": {
    "dietary": "Shellfish allergy - Room 205"
  }
}
EOF
```

Generate report with notes:

```bash
python3 main.py --start-date 2024-01-15 --notes test-notes.json --format console
```

**Expected output:**
```
2024-01-15   Monday     12       10         5          11         0
  NOTE: Test conference group
  DIETARY: 2 vegan, 1 gluten-free
  LOCATION: Main dining room
  SPECIAL: Extra coffee needed
2024-01-16   Tuesday    15       13         7          14         0
  DIETARY: Shellfish allergy - Room 205
```

## Step 9: Test Full Report Generation

```bash
python3 main.py --start-date 2024-01-15 --notes test-notes.json --format excel pdf
```

**Expected output:**
```
Excel report saved: reports/meal_plan_2024-01-15.xlsx
PDF report saved: reports/meal_plan_2024-01-15.pdf
Report generation complete!
```

**Check the files:**
```bash
ls -la reports/
```

You should see:
- `meal_plan_2024-01-15.xlsx` - Excel spreadsheet
- `meal_plan_2024-01-15.pdf` - PDF document

Open both and verify:
- ✅ Tables are formatted correctly
- ✅ Notes appear under each day
- ✅ Weekly totals are calculated
- ✅ Ready for printing

## Step 10: Test with Current Week

```bash
python3 main.py --format excel pdf
```

This generates a report for the upcoming week (starting next Monday).

## Troubleshooting

### Error: "No module named 'requests'"
**Solution:** Run `pip3 install -r requirements.txt`

### Error: "config.py not found"
**Solution:** Run `cp config.example.py config.py` and edit with your credentials

### Error: "401 Unauthorized"
**Solution:** Check your CLIENT_TOKEN and ACCESS_TOKEN in config.py

### Error: "Connection refused" or "Timeout"
**Solution:** Check your internet connection and BASE_URL in config.py

### All meal counts are zero
**Explanation:** The demo environment may not have meal products configured. This is normal for testing. The application is working correctly - you're just seeing zero counts because there's no meal data.

**To verify it's working:**
- Check that you get reservation data (Guest counts > 0)
- Check that the report generates successfully
- Check that notes appear correctly

## Success! What's Next?

If all tests passed, you're ready to:

1. **For Production Use:**
   - Get your production Mews credentials
   - Update `config.py` with production URL and tokens
   - Ensure meal products are configured in Mews
   - Start generating weekly reports!

2. **Customize:**
   - Adjust meal product keywords in `config.py`
   - Create your own notes templates
   - Set up automated scheduling

3. **Learn More:**
   - Read [GETTING_STARTED.md](GETTING_STARTED.md) for detailed workflow
   - Check [NOTES_FEATURE.md](NOTES_FEATURE.md) for notes documentation
   - Read [README.md](README.md) for full feature list

## Quick Reference

```bash
# Basic report (console)
python3 main.py

# Excel report
python3 main.py --format excel

# With notes
python3 main.py --notes weekly-notes.json --format excel pdf

# Specific date
python3 main.py --start-date 2024-02-05 --format excel

# Help
python3 main.py --help
```

---

**Questions or issues?** Check the troubleshooting section or refer to the documentation files.
