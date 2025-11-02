import os
from supabase import create_client, Client
from dotenv import load_dotenv
import requests
from datetime import datetime

# Load environment variables
load_dotenv()

class PushoverNotifier:
    """Handles push notifications via Pushover"""
    
    def __init__(self):
        self.user_key = os.getenv("PUSHOVER_USER_KEY")
        self.app_token = os.getenv("PUSHOVER_TOKEN")
        self.api_url = "https://api.pushover.net/1/messages.json"
        
        if not self.user_key or not self.app_token:
            raise ValueError("PUSHOVER_USER_KEY and PUSHOVER_TOKEN must be set in .env file")
    
    def send_notification(self, message, title=None, priority=0, sound=None):
        """Send a push notification"""
        payload = {
            "token": self.app_token,
            "user": self.user_key,
            "message": message,
        }
        
        if title:
            payload["title"] = title
        if priority:
            payload["priority"] = priority
        if sound:
            payload["sound"] = sound
        
        try:
            response = requests.post(self.api_url, data=payload)
            response.raise_for_status()
            print(f"✓ Notification sent successfully")
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"✗ Failed to send notification: {e}")
            return None

def add_entry():
    """Add a new entry to the Supabase database"""
    
    # Initialize Pushover notifier
    try:
        notifier = PushoverNotifier()
    except ValueError as e:
        print(f"✗ Warning: Pushover not configured: {e}")
        notifier = None
    
    try:
        # Initialize Supabase client
        supabase_url = os.getenv("SUPABASE_API_URL")
        supabase_key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
        
        if not supabase_url or not supabase_key:
            raise ValueError("SUPABASE_API_URL and SUPABASE_SERVICE_ROLE_KEY must be set in .env file")
        
        supabase: Client = create_client(supabase_url, supabase_key)
        
        # Data to insert
        # Get today's date in YYYY-MM-DD format
        today = datetime.now().strftime("%Y-%m-%d")
        
        data = {
            "week_number": 1,
            "date": today,
            "weight": 75,
            "fat_percent": 0.09,
            "bmi": 25,
            "fat_weight": 7.5,
            "lean_weight": 67.5,
            "neck": 16,
            "shoulders": 18,
            "biceps": 19,
            "forearms": 13,
            "chest": 40,
            "above_navel": 36,
            "navel": 38,
            "waist": 38,
            "hips": 40,
            "thighs": 22,
            "calves": 15
        }
        
        table_name = os.getenv("SUPABASE_TABLE", "progress")
        
        # Check if entry with the same week_number already exists
        print(f"Checking for existing entry with week_number {data['week_number']}...")
        existing = supabase.table(table_name).select("*").eq("week_number", data["week_number"]).execute()
        
        if existing.data and len(existing.data) > 0:
            print(f"✗ Entry with week_number {data['week_number']} already exists")
            print(f"  Existing entry: Date={existing.data[0].get('date')}, Weight={existing.data[0].get('weight')} kg")
            
            # Send "Entry already exist" notification
            if notifier:
                notifier.send_notification(
                    message="Entry already exist",
                    title="Supabase Activity"
                )
            
            return None
        
        # Entry doesn't exist, proceed with insertion
        print(f"No existing entry found. Proceeding with insertion...")
        response = supabase.table(table_name).insert(data).execute()
        
        print(f"✓ Entry added successfully to '{table_name}' table")
        print(f"  Week Number: {data['week_number']}")
        print(f"  Date: {data['date']}")
        print(f"  Weight: {data['weight']} kg")
        
        # Send push notification
        if notifier:
            notifier.send_notification(
                message="Entry Created",
                title="Supabase Activity"
            )
        
        return response
        
    except Exception as e:
        print(f"✗ Error adding entry: {e}")
        return None

if __name__ == "__main__":
    print("Adding new entry to Supabase...")
    print("-" * 50)
    add_entry()

