# Detailed Kitchen Reports - Enhanced Planning

## 🎯 What Kitchen Staff Really Need

The enhanced detailed report format includes everything a chef or waiter needs to know before starting their day:

### Service Timing
- Exact times for breakfast, lunch, dinner
- Multiple sittings/service times
- Early and late service requests
- Room service orders by time

### Guest Information
- How many covers per service time
- VIP guests requiring special attention
- Group bookings vs individual guests
- Room numbers for dietary restrictions

### Location Details
- Which dining room/conference room
- Buffet vs plated service setup
- Table assignments
- Room service details

### Menu Planning
- Pre-ordered menu selections
- How many of each dish
- Dietary requirements per person
- Children's menu needs

### Preparation Checklist
- Ingredients to prep
- Special items needed
- Quantities for the day
- Advance preparation tasks

### Staffing Requirements
- How many waiters/chefs needed
- Peak service times
- Special event staffing
- Contact information

## 📋 Example Detailed Notes File

Create a JSON file with comprehensive details:

```json
{
  "2024-01-15": {
    "general": "Busy Monday - Conference group + regular guests",
    "dietary": "2 guests lactose intolerant (Rooms 205, 312), 1 vegan (Room 404)",

    "lunch": {
      "service_times": [
        {
          "time": "11:30",
          "covers": 8,
          "notes": "Early lunch - Business travelers",
          "location": "Restaurant"
        },
        {
          "time": "12:00",
          "covers": 25,
          "notes": "Conference group lunch",
          "location": "Grand Ballroom",
          "menu": "Pre-ordered: 15x Chicken, 8x Salmon, 2x Vegetarian"
        }
      ],
      "special_requests": [
        "Fast service needed - conference resumes at 14:00"
      ]
    },

    "ingredients_prep": [
      "Extra gluten-free bread needed",
      "Prepare vegan options for dinner"
    ],

    "staffing": {
      "lunch_staff": "4 waiters + 2 chefs (conference)",
      "notes": "Extra staff needed for conference lunch"
    }
  }
}
```

## 🚀 How to Use

### Step 1: Create Detailed Notes

Copy the template:
```bash
cp notes_detailed.example.json my_detailed_notes.json
```

Edit with your actual service times and requirements.

### Step 2: Generate Detailed Report

```bash
# With Mews data
python3 main.py --notes my_detailed_notes.json --detailed --format excel

# Demo mode
python3 demo.py --notes notes_detailed.example.json --detailed --format excel
```

### Step 3: View the Report

The Excel file will have multiple sheets:
- **Weekly Summary** - Quick overview
- **Mon 01-15, Tue 01-16...** - Daily details (one sheet per day)
- **Prep Checklist** - All ingredients to prep
- **Staffing** - Weekly staffing requirements

## 📊 Report Features

### Daily Detail Sheets

Each day gets its own sheet with:

**Breakfast Section:**
- Service times (e.g., 07:00, 08:30)
- Number of covers per time
- Location (Main Restaurant, Room Service)
- Special requests

**Lunch Section:**
- Multiple sitting times (11:30, 12:00, 13:00)
- Covers per sitting
- Menu selections if pre-ordered
- Service timing notes

**Dinner Section:**
- First, main, and late seatings
- VIP tables and celebrations
- Children's menus
- Wine pairings

**Coffee Breaks:**
- Times and locations
- Number of attendees
- Items needed

**Room Service:**
- Orders by meal type
- Peak times
- Special instructions

**Preparation List:**
- Checklist format with ☐ boxes
- Ingredients and quantities
- Special items

**Timeline:**
- Event schedule
- Critical timing points
- Setup and service milestones

### Prep Checklist Sheet

Consolidated prep list for the week:
- ☐ Checkbox format for easy tracking
- Organized by day
- All special ingredients
- Advance preparation items

### Staffing Sheet

Weekly staffing overview:
- Staff needed per meal per day
- Peak days highlighted
- Special notes (conferences, events)
- Contact information for event coordinators

## 💡 Real-World Examples

### Example 1: Regular Service Day

```json
{
  "2024-01-15": {
    "breakfast": {
      "service_times": [
        {
          "time": "07:30",
          "covers": 25,
          "notes": "Regular buffet service",
          "location": "Main Restaurant"
        }
      ]
    },

    "lunch": {
      "service_times": [
        {
          "time": "12:00",
          "covers": 18,
          "location": "Restaurant"
        }
      ]
    },

    "dinner": {
      "service_times": [
        {
          "time": "19:00",
          "covers": 30,
          "location": "Main Restaurant"
        }
      ],
      "special_requests": [
        "Table 5 - Anniversary, cake needed"
      ]
    },

    "ingredients_prep": [
      "Anniversary cake for Table 5"
    ]
  }
}
```

### Example 2: Conference Day

```json
{
  "2024-01-17": {
    "general": "Tech Summit Conference - 80 attendees",

    "breakfast": {
      "service_times": [
        {
          "time": "07:00",
          "covers": 80,
          "notes": "Conference breakfast - Extended buffet",
          "location": "Conference Hall Foyer"
        }
      ],
      "special_requests": [
        "Extra coffee - high consumption expected",
        "5 vegan options needed"
      ]
    },

    "lunch": {
      "service_times": [
        {
          "time": "12:30",
          "covers": 80,
          "notes": "Plated service - FAST timing",
          "location": "Conference Room A",
          "menu": "45x Chicken Salad, 25x Pasta, 10x Vegan",
          "timing": "12:30 Seat, 12:45 Serve, 13:45 Clear - Conference resumes 14:00"
        }
      ]
    },

    "coffee_breaks": [
      {
        "time": "10:30",
        "location": "Conference Hall Foyer",
        "items": "Coffee, tea, pastries, fruit",
        "covers": 80
      },
      {
        "time": "15:00",
        "location": "Conference Hall Foyer",
        "items": "Coffee, tea, cookies",
        "covers": 80
      }
    ],

    "ingredients_prep": [
      "Prep for 80 lunch (45 chicken, 25 pasta, 10 vegan)",
      "Coffee for 3 breaks (estimate 240 cups total)",
      "Pastries and cookies for breaks"
    ],

    "staffing": {
      "breakfast_staff": "3 waiters + 1 chef + coffee attendant",
      "lunch_staff": "6 waiters + 2 chefs (TIMING CRITICAL)",
      "notes": "Contact: Sarah Chen sarah@techsummit.com 555-0123"
    }
  }
}
```

### Example 3: Wedding Day

```json
{
  "2024-01-20": {
    "general": "WEDDING - Smith & Johnson - 60 guests",
    "dietary": "Bride vegetarian, 2 nut allergies (Table 3), 4 gluten-free",

    "dinner": {
      "service_times": [
        {
          "time": "19:30",
          "covers": 60,
          "notes": "WEDDING RECEPTION DINNER",
          "location": "Grand Ballroom",
          "menu": "3-course set:\nStarter: Caesar (3x vegan)\nMain: 40x Beef, 15x Salmon, 5x Vegetarian\nDessert: Tiramisu (3x dairy-free)",
          "timing": "19:30 Drinks, 20:00 Starter, 20:30 Main, 21:15 Dessert, 21:45 Cake"
        }
      ],
      "special_requests": [
        "External wedding cake arrives 18:00",
        "Champagne toast at 21:45 (80 glasses)",
        "Kids menu for 6 children",
        "NUT-FREE zone Table 3",
        "Late-night snack buffet 23:00"
      ]
    },

    "ingredients_prep": [
      "60 portions 3-course menu",
      "Extra champagne (80 glasses)",
      "Nut-free alternatives ready",
      "Vegetarian options (bride + 4 others)",
      "Kids menu items",
      "Late-night finger food buffet"
    ],

    "staffing": {
      "dinner_staff": "8 waiters + 3 chefs + event coordinator",
      "notes": "ALL HANDS - Staff briefing 17:00"
    },

    "timeline": [
      "17:00 - Staff briefing",
      "18:00 - Wedding cake delivery",
      "18:30 - Final table check",
      "19:30 - Guests arrive",
      "21:45 - Cake cutting",
      "23:00 - Late buffet",
      "00:30 - Service ends"
    ]
  }
}
```

## 🎯 Benefits

### For Chefs:
- ✅ Know exactly what to prep
- ✅ Timing for each service
- ✅ Special dietary requirements clearly marked
- ✅ Quantities and menu selections

### For Waiters:
- ✅ Service times and locations
- ✅ Number of covers per sitting
- ✅ VIP tables and special requests
- ✅ Room numbers for dietary restrictions

### For Managers:
- ✅ Staffing requirements clear
- ✅ Timeline for complex events
- ✅ Checklist format for quality control
- ✅ Weekly overview at a glance

## 📝 Tips

1. **Update Sunday night** - Prep notes for the upcoming week
2. **Print daily sheets** - One sheet per station (grill, salads, pastry)
3. **Use checkboxes** - Cross off prep items as completed
4. **Highlight allergies** - Use red highlighter for dietary restrictions
5. **Keep timeline visible** - Post event timelines in expo area
6. **Morning briefing** - Review daily sheet with team at lineup

## 🔄 Workflow

### Sunday Evening:
1. Check upcoming reservations
2. Contact front desk about special requests
3. Update detailed notes file
4. Generate weekly report

### Monday Morning:
1. Print daily sheets
2. Brief kitchen team
3. Post prep checklist
4. Review any VIP/dietary notes

### Throughout Week:
1. Update notes as new info comes in
2. Regenerate report if major changes
3. Check off prep items
4. Notes for next week

---

**The detailed report format gives kitchen staff everything they need in one place - no more hunting through emails, notes, or reservation systems!**
