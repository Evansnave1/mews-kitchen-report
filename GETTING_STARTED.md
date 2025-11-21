# Getting Started - Testing and Using the Kitchen Meal Planner

This guide will help you test the application and start using it in production.

## Quick Start Options

### Option 1: Test with Mews Demo Environment (Recommended for Testing)
### Option 2: Use with Your Production Mews Account

---

## Option 1: Testing with Mews Demo Environment

The Mews API provides a demo environment with sample data you can use for testing.

### Step 1: Install Dependencies

```bash
cd kitchen-meal-planner
pip install -r requirements.txt
```

### Step 2: Get Demo Credentials

Mews provides public demo credentials for testing. You can find them in the official documentation:

1. Visit the Mews Connector API documentation
2. Navigate to the "Getting Started" section
3. Look for demo environment credentials

**Demo Environment Details:**
- Base URL: `https://api.mews-demo.com`
- Demo credentials are publicly available in the Mews documentation
- Contains sample hotel data with reservations

### Step 3: Configure the Application

```bash
# Copy the example config
cp config.example.py config.py

# Edit config.py with demo credentials
nano config.py  # or use your preferred editor
```

Update `config.py`:
```python
CLIENT_TOKEN = "your-demo-client-token"
ACCESS_TOKEN = "your-demo-access-token"
BASE_URL = "https://api.mews-demo.com"
```

### Step 4: Test the Application

```bash
# Basic test - console output
python main.py --start-date 2024-01-15

# Test with Excel output
python main.py --start-date 2024-01-15 --format excel

# Test with notes
cp notes.example.json my-notes.json
python main.py --start-date 2024-01-15 --notes my-notes.json --format excel pdf
```

**Expected Behavior:**
- You should see meal counts based on demo reservations
- Excel/PDF files will be created in the `reports/` directory
- Notes should appear in the reports

### Troubleshooting Demo Environment

**If you get authentication errors:**
- Double-check your credentials match the demo credentials exactly
- Ensure BASE_URL is `https://api.mews-demo.com` (no trailing slash)

**If you see zero meal counts:**
- The demo environment may not have meal products configured
- This is normal - the app is working, just no meal data in demo
- Focus on testing the report generation and notes features

---

## Option 2: Production Use with Your Mews Account

### Step 1: Get Production Credentials

**You need two tokens:**

1. **Client Token** - Identifies your application
   - Contact: [partnersuccess@mews.com](mailto:partnersuccess@mews.com)
   - Mention you want to build a meal planning integration
   - They will provide your Client Token

2. **Access Token** - Identifies your property
   - Log in to Mews Operations (your hotel's Mews system)
   - Navigate to: Settings → Integrations → Mews Connector API
   - Create a new Access Token
   - Give it a name like "Kitchen Meal Planner"

### Step 2: Configure Production Settings

```bash
cp config.example.py config.py
```

Edit `config.py`:
```python
CLIENT_TOKEN = "your-production-client-token"
ACCESS_TOKEN = "your-production-access-token"
BASE_URL = "https://api.mews.com"  # Production URL
```

### Step 3: Verify Your Meal Products are Configured

The application automatically identifies meal products, but they need to be set up in Mews first:

**In Mews Operations:**
1. Go to: Settings → Services → Products
2. Ensure you have products for:
   - Breakfast (name should contain "breakfast" or "morning")
   - Lunch (name should contain "lunch" or "midday")
   - Dinner (name should contain "dinner" or "evening")
3. Products should be configured with:
   - Charging Mode: "Per Person Per Time Unit" (for per-guest pricing)
   - Classification: Food = Yes

### Step 4: Test with Real Data

```bash
# Generate report for current week
python main.py

# Generate report for next week
python main.py --start-date 2025-01-27

# Generate Excel and PDF for printing
python main.py --format excel pdf
```

### Step 5: Create Your First Weekly Report

1. **Check upcoming reservations** in Mews
2. **Create a notes file** for special requirements:

```bash
# Copy the example
cp notes.example.json weekly-notes.json

# Edit with real requirements
nano weekly-notes.json
```

Example for your property:
```json
{
  "2025-01-27": {
    "dietary": "3 vegetarian, 1 vegan (Room 205)",
    "special": "Early breakfast service for tour group at 6am"
  },
  "2025-01-28": {
    "general": "Corporate conference - 50 attendees",
    "location": "Breakfast buffet in Main Hall, Lunch in Conference Room A",
    "dietary": "2 gluten-free, 4 dairy-free",
    "special": "Coffee breaks at 10am and 3pm"
  }
}
```

3. **Generate the report**:

```bash
python main.py --notes weekly-notes.json --format excel pdf
```

4. **Print and distribute**:
   - Excel file: Easy to email or edit if needed
   - PDF file: Print and post in kitchen prep area

---

## Regular Weekly Workflow

### Every Monday Morning:

1. **Update notes file**:
```bash
# Start with last week's notes
cp weekly-notes.json weekly-notes-backup.json

# Edit for this week
nano weekly-notes.json
```

2. **Generate reports**:
```bash
python main.py --notes weekly-notes.json --format excel pdf
```

3. **Distribute**:
   - Print PDF → Post in kitchen
   - Email Excel → Restaurant manager, head chef
   - Keep JSON → Archive for records

### Automated Daily Updates (Optional):

Create a cron job or scheduled task:

```bash
# Example cron job - runs every day at 6am
0 6 * * * cd /path/to/kitchen-meal-planner && python main.py --format excel
```

---

## Verifying Everything Works

### Checklist:

- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Config file created with valid credentials
- [ ] Can run `python main.py` without errors
- [ ] Reports show meal counts (not all zeros)
- [ ] Excel file opens correctly
- [ ] PDF file looks good for printing
- [ ] Notes appear in reports when using `--notes` option

### If Meal Counts are Zero:

**Common reasons:**
1. No meal products configured in Mews
2. Reservations don't have meal products attached
3. Looking at wrong date range (no reservations in that period)
4. Meal products don't match naming patterns

**Solutions:**
1. Check Mews: Settings → Services → Products
2. Ensure products have names like "Breakfast", "Lunch", "Dinner"
3. Verify reservations have these products attached
4. Customize product keywords in `config.py`:

```python
MEAL_KEYWORDS = {
    'breakfast': ['breakfast', 'petit déjeuner', 'morning meal'],
    'lunch': ['lunch', 'almuerzo', 'midday'],
    'dinner': ['dinner', 'cena', 'evening'],
    'conference': ['conference', 'banquet', 'event']
}
```

---

## Next Steps

### Week 1: Testing Phase
- Generate reports for current/next week
- Compare with actual reservations in Mews
- Verify meal counts match expectations
- Test notes feature with real dietary restrictions

### Week 2: Kitchen Team Training
- Show kitchen staff how to read reports
- Explain the notes sections
- Get feedback on format and content
- Adjust as needed

### Week 3+: Regular Use
- Make report generation part of Monday routine
- Keep notes file updated
- Archive old reports
- Monitor for accuracy

---

## Getting Help

### Issues with the Application
- Check error messages carefully
- Verify config.py settings
- Ensure Mews credentials are valid

### Issues with Mews API
- Contact: [partnersuccess@mews.com](mailto:partnersuccess@mews.com)
- Reference: Mews Connector API documentation
- Mention you're using the Kitchen Meal Planner

### Feature Requests
- Want additional meal types?
- Need different report format?
- Want automatic email delivery?
- All can be customized!

---

## Pro Tips

1. **Keep a backup of notes files**: Archive each week for historical reference
2. **Use consistent date formats**: Always YYYY-MM-DD
3. **Print in color**: Notes stand out better with color printing
4. **Post at eye level**: Kitchen staff should see it easily
5. **Update mid-week if needed**: Run again if large reservations change

---

## Security Notes

⚠️ **Important:**
- Never commit `config.py` to version control (it's in `.gitignore`)
- Keep your Access Token secure
- Don't share credentials via email or chat
- Rotate Access Tokens periodically in Mews

---

## Quick Reference Commands

```bash
# Console output (quick check)
python main.py

# Excel report for printing
python main.py --format excel

# Full report with notes
python main.py --notes weekly-notes.json --format excel pdf

# Specific date range
python main.py --start-date 2025-02-03 --format excel

# Custom output location
python main.py --format excel pdf --output-dir ./weekly_reports

# Help
python main.py --help
```

---

Ready to get started? Follow Option 1 for testing or Option 2 for production use!
