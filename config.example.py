"""
Configuration file for Mews Kitchen Meal Planner
Copy this file to config.py and fill in your credentials
"""

# Mews API Credentials
# Get these from your Mews account or Mews partner manager

# Client Token - Identifies your application
CLIENT_TOKEN = "your-client-token-here"

# Access Token - Identifies the specific property/enterprise
ACCESS_TOKEN = "your-access-token-here"

# API Base URL
# Demo environment (for testing): https://api.mews-demo.com
# Production environment: https://api.mews.com
BASE_URL = "https://api.mews-demo.com"

# Optional: Customize meal product identification
# If your property uses different names for meal products,
# you can customize the keywords used to identify them
MEAL_KEYWORDS = {
    'breakfast': ['breakfast', 'bfast', 'morning', 'continental'],
    'lunch': ['lunch', 'noon', 'midday'],
    'dinner': ['dinner', 'evening', 'supper'],
    'conference': ['conference', 'meeting', 'event', 'banquet', 'catering']
}
