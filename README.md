# Supabase Activity Scripts

Python scripts to manage workout/body measurement data in a Supabase database.

## Setup

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

## Data Fields

The scripts work with the following data fields:
- week_number
- date
- weight
- fat_percent
- bmi
- fat_weight
- lean_weight
- neck
- shoulders
- biceps
- forearms
- chest
- above_navel
- navel
- waist
- hips
- thighs
- calves

