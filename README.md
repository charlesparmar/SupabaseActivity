# Supabase Activity Scripts

Python scripts to manage workout/body measurement data in a Supabase database with real-time push notifications via Pushover.

## Features

- ✅ **Duplicate Detection**: Automatically checks for existing entries before insertion
- 📱 **Push Notifications**: Real-time notifications for all operations via Pushover
- 🗄️ **Supabase Integration**: Seamless database operations with Supabase
- 📊 **Progress Tracking**: Track comprehensive body measurements and progress
- 🔒 **Environment Variables**: Secure configuration using .env files
- 🚀 **Easy to Use**: Simple command-line interface

## 🚀 GitHub Actions (Trigger from Phone!)

You can trigger these scripts directly from your phone using GitHub Actions workflows!

### Quick Access:
- 📱 **Add Entry**: [Run Workflow](https://github.com/charlesparmar/SupabaseActivity/actions/workflows/add-entry.yml)
- 📱 **Remove Entry**: [Run Workflow](https://github.com/charlesparmar/SupabaseActivity/actions/workflows/remove-entry.yml)

### For Phone Apps & API Details:
See the complete guide: **[GITHUB_ACTIONS_GUIDE.md](GITHUB_ACTIONS_GUIDE.md)**

Includes setup for:
- iOS Shortcuts
- Android HTTP Shortcuts
- Tasker, Pushcut, and more!

### GitHub Secrets Configuration:
To use GitHub Actions, add these secrets to your repository:
1. Go to: `Settings` → `Secrets and variables` → `Actions`
2. Add the following secrets:
   - `SUPABASE_API_URL`
   - `SUPABASE_SERVICE_ROLE_KEY`
   - `SUPABASE_TABLE`
   - `PUSHOVER_USER_KEY`
   - `PUSHOVER_TOKEN`

---

## Setup

### Local Installation

1. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your `.env` file with the following variables:
```
SUPABASE_API_URL=your_supabase_url
SUPABASE_SERVICE_ROLE_KEY=your_supabase_service_role_key
SUPABASE_TABLE=progress
PUSHOVER_USER_KEY=your_pushover_user_key
PUSHOVER_TOKEN=your_pushover_token
```

## Scripts

**Note:** Make sure to activate the virtual environment before running scripts:
```bash
source venv/bin/activate
```

### Add.py
Adds a new entry to the Supabase database and sends a Pushover notification.

**Usage:**
```bash
python Add.py
```

**What it does:**
- Checks if an entry with the same `week_number` already exists
- If entry exists:
  - Sends push notification "Entry already exist"
  - Terminates without adding the entry
- If entry doesn't exist:
  - Inserts a new record with predefined body measurements
  - Uses today's date automatically
  - Automatically updates `id` and `created_at` fields (handled by Supabase)
  - Sends push notification "Entry Created"

**Note:** The date field is automatically set to today's date. If you want to use a different date, modify the `today` variable in the script.

### Remove.py
Removes entries from the Supabase database and sends push notifications.

**Usage:**
```bash
# Remove by week number
python Remove.py 1

# Remove by ID
python Remove.py --id abc123-def456-...

# List all entries
python Remove.py --list

# Show help
python Remove.py --help
```

**What it does:**
- Attempts to delete the specified entry from the database
- Sends push notifications based on the result:
  - **"Entry Deleted"** - if the entry was successfully deleted
  - **"Entry not Found"** - if no entry exists with that week number or ID
  - **"Problem running Remove Script"** - if there's an error accessing the database or any other issue

## Environment Variables

- `SUPABASE_API_URL`: Your Supabase project URL
- `SUPABASE_SERVICE_ROLE_KEY`: Your Supabase service role key
- `SUPABASE_TABLE`: Table name (default: "progress")
- `PUSHOVER_USER_KEY`: Your Pushover user key
- `PUSHOVER_TOKEN`: Your Pushover application token

## Push Notifications

The scripts send push notifications via Pushover for the following events:

### Add.py Notifications:
- 🟢 **"Entry Created"** - Successfully added a new entry
- 🟡 **"Entry already exist"** - Attempted to add a duplicate entry

### Remove.py Notifications:
- 🔴 **"Entry Deleted"** - Successfully deleted an entry
- 🟠 **"Entry not Found"** - Attempted to delete a non-existent entry
- ⚠️ **"Problem running Remove Script"** - Error occurred during execution

## Data Fields

The scripts work with the following data fields:
- `week_number` - Week identifier (used for duplicate detection)
- `date` - Date of measurement (auto-set to today)
- `weight` - Body weight in kg
- `fat_percent` - Body fat percentage
- `bmi` - Body Mass Index
- `fat_weight` - Fat weight in kg
- `lean_weight` - Lean body weight in kg
- `neck` - Neck circumference
- `shoulders` - Shoulder width
- `biceps` - Bicep circumference
- `forearms` - Forearm circumference
- `chest` - Chest circumference
- `above_navel` - Measurement above navel
- `navel` - Measurement at navel
- `waist` - Waist circumference
- `hips` - Hip circumference
- `thighs` - Thigh circumference
- `calves` - Calf circumference

## Requirements

- Python 3.13+
- Supabase account with a configured database
- Pushover account for push notifications
- Virtual environment (recommended)

## License

This project is open source and available for personal use.

## Contributing

Feel free to submit issues and enhancement requests!

