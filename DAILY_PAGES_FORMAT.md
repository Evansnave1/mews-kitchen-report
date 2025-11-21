# Daily Pages Format - Clean, Professional Reports

## 🎯 Overview

The **Daily Pages** format creates clean, professional reports with **one page per day** - perfect for posting in the kitchen or printing for daily briefings.

### Key Features:
- ✅ **One clean page per day** (not crowded!)
- ✅ **Timeline format** - Events chronologically with timestamps
- ✅ **Clear sections** - Time | Service | Details layout
- ✅ **Professional design** - Similar to Oracle system reports
- ✅ **Print-ready** - Optimized for Letter/A4 paper
- ✅ **Easy to scan** - Information organized logically

## 📄 Report Structure

### Sheet 1: Week Overview
Quick summary of the entire week:
```
Date         Day       Guests  Breakfast  Lunch  Dinner
2024-01-15   Monday    45      38         12     42
2024-01-16   Tuesday   52      45         15     48
...
```

### Sheets 2-8: Daily Pages (One Per Day)
Each day gets its own clean page with:

**Header:**
```
┌─────────────────────────────────────┐
│        MONDAY                        │  ← Large, bold day name
├─────────────────────────────────────┤
│ 2024-01-15  •  45 Guests  • 38B/12L/42D │  ← Summary line
└─────────────────────────────────────┘
```

**Overview Section:**
```
📋 Corporate conference group checking in
⚠️  DIETARY: 2 guests lactose intolerant, 1 vegan
```

**Timeline Section:**
```
TIME    SERVICE/EVENT           DETAILS
────────────────────────────────────────────────────
07:00   BREAKFAST              25 covers
                               Location: Main Restaurant
                               Regular buffet service

11:30   LUNCH                  8 covers
                               Location: Restaurant
                               Early lunch - Business travelers

12:00   LUNCH                  25 covers
                               Location: Grand Ballroom
                               Pre-ordered: 15x Chicken, 8x Salmon, 2x Vegetarian
                               ⏰ 12:30 Seat, 12:45 Serve, 13:45 Clear

19:00   DINNER                 30 covers
                               Location: Main Restaurant
                               Regular service
```

**Preparation Checklist:**
```
PREPARATION CHECKLIST
────────────────────────────────
☐ Extra gluten-free bread needed
☐ Prepare vegan options for dinner
☐ Anniversary cake for Table 5
```

## 🚀 How to Use

### Generate Daily Pages Report

```bash
# With real Mews data
python3 main.py --notes my_notes.json --daily-pages --format excel

# Demo mode
python3 demo.py --notes notes_detailed.example.json --daily-pages --format excel --start-date 2024-01-15
```

### Open and Print

```bash
# Open the report
open demo_reports/demo_meal_plan_daily_2024-01-15.xlsx

# Print each day's sheet separately
# Each sheet is optimized for one printed page
```

## 📋 Layout Details

### Time Column (Left)
- **Bold timestamps** (07:00, 12:00, 19:00)
- Easy to scan quickly
- Chronological order

### Service Column (Middle)
- **Bold meal names** (BREAKFAST, LUNCH, DINNER)
- Event names
- Highlighted for important services (>50 covers)

### Details Column (Right)
- Number of covers
- Location
- Menu selections
- Special notes
- Timing requirements

## 💡 Real-World Example

### Monday - Regular Service Day

```
═══════════════════════════════════════════════════
                   MONDAY
───────────────────────────────────────────────────
  2024-01-15  •  45 Guests  •  38B/12L/42D
═══════════════════════════════════════════════════

TIME    SERVICE             DETAILS
────────────────────────────────────────────────────
07:30   BREAKFAST          25 covers
                           Location: Main Restaurant
                           Regular buffet service

12:00   LUNCH              18 covers
                           Location: Restaurant
                           Regular service

19:00   DINNER             30 covers
                           Location: Main Restaurant
                           Table 5 - Anniversary, cake needed

PREPARATION CHECKLIST
────────────────────────────────
☐ Anniversary cake for Table 5
```

### Tuesday - Wedding Day

```
═══════════════════════════════════════════════════
                   TUESDAY
───────────────────────────────────────────────────
  2024-01-16  •  60 Guests  •  52B/26L/60D
═══════════════════════════════════════════════════

📋 WEDDING - Smith & Johnson - High occupancy
⚠️  DIETARY: 2 nut allergies (Table 3), 1 pescatarian, 3 vegetarian

TIME    SERVICE             DETAILS
────────────────────────────────────────────────────
07:30   BREAKFAST          20 covers
                           Location: Main Restaurant
                           Regular service

09:00   BREAKFAST          32 covers
                           Location: Main Restaurant
                           Wedding party - Extended buffet
                           Champagne breakfast option

12:00   LUNCH              18 covers
                           Location: Restaurant

13:00   LUNCH              8 covers
                           Location: Garden Terrace
                           Light lunch for wedding party

18:00   DINNER             15 covers
                           Location: Main Restaurant
                           Early sitting - Regular guests

19:30   DINNER             60 covers ⚠️
                           Location: Grand Ballroom
                           WEDDING RECEPTION
                           Menu: 40x Beef, 15x Salmon, 5x Vegetarian
                           ⏰ 19:30 Drinks, 20:00 Starter, 21:45 Cake

21:45   Event              Cake cutting ceremony

23:00   Event              Late-night snack buffet

PREPARATION CHECKLIST
────────────────────────────────
☐ 60 portions set menu
☐ Extra champagne (80 glasses)
☐ Prepare nut-free alternatives
☐ Vegetarian options ready
☐ Kids menu items prepped
☐ Late-night finger food buffet
```

### Wednesday - Conference Day

```
═══════════════════════════════════════════════════
                  WEDNESDAY
───────────────────────────────────────────────────
  2024-01-17  •  80 Guests  •  45B/80L/65D
═══════════════════════════════════════════════════

📋 Tech Summit Conference - 80 attendees
⚠️  DIETARY: 5 vegetarian options needed

TIME    SERVICE             DETAILS
────────────────────────────────────────────────────
07:00   BREAKFAST          45 covers
                           Location: Conference Hall Foyer
                           Conference breakfast - Extended buffet
                           Extra coffee and tea

10:30   Coffee Break       80 attendees
                           Location: Conference Hall Foyer
                           Items: Coffee, tea, pastries, fruit

12:30   LUNCH              80 covers ⚠️
                           Location: Conference Room A
                           Plated service - FAST timing
                           45x Chicken Salad, 25x Pasta, 10x Vegan
                           ⏰ 12:30 Seat, 12:45 Serve, 13:45 Clear
                           Conference resumes at 14:00

15:00   Coffee Break       80 attendees
                           Location: Conference Hall Foyer
                           Items: Coffee, tea, cookies

19:00   DINNER             65 covers
                           Location: Main Restaurant
                           Conference networking dinner - Buffet

PREPARATION CHECKLIST
────────────────────────────────
☐ Large quantity prep for 80 people lunch
☐ Coffee supplies for 3 breaks (240 cups)
☐ Buffet dinner for 65
☐ Vegan and vegetarian options throughout
```

## 🎨 Design Features

### Visual Hierarchy
1. **Day name** - Large, bold, centered (24pt)
2. **Date summary** - Medium, centered with stats
3. **Alerts** - Colored background (yellow for notes, red for dietary)
4. **Timeline** - Left-aligned with clear columns
5. **Checklist** - Simple checkbox format

### Color Coding
- **Blue header** - Professional brand color (#366092)
- **Light blue** - Date summary (#E8F0F8)
- **Yellow** - General notes/highlights (#FFF9E6)
- **Light red** - Dietary warnings (#FFE6E6)
- **Gray** - Section headers (#D3D3D3)

### Print Optimization
- Letter size (8.5" x 11") or A4
- Portrait orientation
- Margins optimized for printing
- Text size readable when printed
- Each day fits on one page

## 📊 Comparison with Other Formats

| Feature | Daily Pages | Detailed Report | Standard Report |
|---------|-------------|-----------------|-----------------|
| Layout | Timeline | Multi-sheet tabs | Single table |
| Pages per day | 1 clean page | Multiple tabs | All in one |
| Print-friendly | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| Easy to scan | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| Detail level | Medium-High | Very High | Medium |
| Post in kitchen | ✅ Perfect | ❌ Too much | ✅ Basic |
| Daily briefing | ✅ Perfect | ⭐ OK | ⭐ Basic |
| Weekly planning | ⭐ OK | ✅ Best | ✅ Good |

## 💼 Best Use Cases

### ✅ Use Daily Pages For:
- **Daily briefings** - Print Monday's page for Monday briefing
- **Kitchen posting** - Post today's page in prep area
- **Station assignments** - One page per station
- **Service briefings** - Clear timeline for waiters
- **Event days** - Clean layout for complex events
- **Training** - Easy for new staff to understand

### ⚠️ Use Detailed Report For:
- **Weekly planning** - Manager needs full week view
- **Multiple properties** - Comparing across locations
- **Historical records** - Archiving complete information
- **Complex analysis** - Need all data in one place

### ⚠️ Use Standard Report For:
- **Quick overview** - Just need counts
- **Email distribution** - Simple attachment
- **Basic planning** - No special events

## 🔄 Workflow Recommendations

### Sunday Evening:
1. Generate weekly report with daily pages
2. Print all 7 days
3. Review with management

### Daily (Morning):
1. Post today's page in kitchen prep area
2. Brief team using timeline
3. Check off prep items as completed
4. Mark completed services during day

### Daily (Evening):
1. Remove today's page
2. Post tomorrow's page
3. Prep team reviews tomorrow's requirements

## 📝 Tips for Kitchen Staff

1. **Timeline is your friend** - Follow it chronologically
2. **Highlight dietary warnings** - Use physical highlighter
3. **Check off prep items** - Use pen to mark completed
4. **Note actual times** - Write actual service times next to planned
5. **Keep visible** - Post at eye level in expo or prep area
6. **One page per station** - Grill gets their items, pastry gets theirs

## 🎯 Printing Tips

### For Daily Use:
```
- Print: Today's sheet only
- Size: Letter or A4
- Orientation: Portrait
- Quality: Normal (save ink)
- Copies: 2-3 (kitchen, expo, office)
```

### For Weekly Planning:
```
- Print: All sheets
- Bind: Staple or clip together
- Distribute: Manager, head chef, F&B director
```

### For Posting:
```
- Print: Single day
- Laminate: Optional (reusable with dry-erase)
- Post: Visible location
- Update: Daily
```

---

**The Daily Pages format gives you clean, professional, one-page-per-day reports that are perfect for posting in the kitchen or using in daily briefings!** 📄✨
