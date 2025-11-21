# Notes and Comments Feature

The Kitchen Meal Planner now supports adding notes and comments to your weekly reports!

## Why Use Notes?

Kitchen and restaurant staff often need to communicate important information beyond just meal counts:
- **Dietary restrictions** - Allergies, intolerances, special diets
- **Service locations** - Where conference meals should be served
- **Special requirements** - Extra coffee stations, specific setup times
- **General reminders** - VIP guests, large groups, special events

## How to Add Notes

### 1. Create a Notes File

Create a JSON file (e.g., `notes.json`) with your comments:

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

### 2. Generate Report with Notes

```bash
python main.py --notes notes.json --format excel pdf
```

## Note Types

The application supports four types of notes per day:

| Type | Purpose | Example |
|------|---------|---------|
| `general` | General information about the day | "Conference group checking in" |
| `dietary` | Dietary restrictions and allergies | "2 lactose intolerant, 1 vegan, 3 gluten-free" |
| `location` | Where meals will be served | "Conference meals in Grand Ballroom" |
| `special` | Special requests or setup needs | "Coffee & tea setup needed by 8:00 AM" |

## How Notes Appear in Reports

### Console Output
```
2024-01-15   Monday     45       38         12         42         0
  NOTE: Conference group checking in - Corporate event
  DIETARY: 2 guests lactose intolerant, 1 vegan
  LOCATION: Conference meals in Grand Ballroom
  SPECIAL: Coffee & tea setup needed by 8:00 AM
```

### Excel Output
- Notes appear as italicized rows below each day
- Light gray background to distinguish from meal counts
- Spans across all columns for easy reading

### PDF Output
- Notes integrated into the table
- Smaller italic font
- Clearly associated with the specific day

## Real-World Examples

### Example 1: Conference Event
```json
{
  "2024-01-17": {
    "general": "Tech Summit - 80 conference attendees",
    "dietary": "5 vegetarian, 2 vegan, 3 gluten-free",
    "location": "Breakfast in Main Hall, Lunch in Conference Room A, Dinner in Restaurant",
    "special": "Coffee breaks at 10am and 3pm in lobby"
  }
}
```

### Example 2: Wedding Event
```json
{
  "2024-01-20": {
    "general": "VIP Wedding - Smith & Johnson",
    "dietary": "Bride is vegetarian, 4 guests with nut allergies, 2 gluten-free",
    "location": "Reception dinner in Grand Ballroom",
    "special": "Champagne brunch setup at 11am, Chef's special menu"
  }
}
```

### Example 3: Simple Dietary Note
```json
{
  "2024-01-18": {
    "dietary": "Room 305 - severe shellfish allergy (EpiPen on file)"
  }
}
```

## Tips for Using Notes

1. **Keep it concise** - Notes should be quick to read at a glance
2. **Update weekly** - Create a new notes file each week
3. **Use the example** - Copy `notes.example.json` as a starting point
4. **Print and post** - Generate Excel/PDF reports with notes for the kitchen wall
5. **Date format** - Always use YYYY-MM-DD format for dates

## Notes File Template

See [notes.example.json](notes.example.json) for a complete template you can copy and customize.

## Workflow Suggestion

**Monday morning routine:**
1. Check upcoming reservations in Mews
2. Contact front desk about special requests
3. Update `notes.json` with dietary restrictions and special events
4. Generate weekly report: `python main.py --notes notes.json --format excel pdf`
5. Print and post in kitchen prep area
6. Email PDF to restaurant manager

This ensures your kitchen team has all the information they need for the week ahead!
