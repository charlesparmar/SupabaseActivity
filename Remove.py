import os
from supabase import create_client, Client
from dotenv import load_dotenv
import sys
import requests

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

def remove_entry(week_number=None, entry_id=None):
    """
    Remove an entry from the Supabase database
    
    Args:
        week_number: Remove entry by week number
        entry_id: Remove entry by ID
    """
    
    try:
        # Initialize Pushover notifier
        notifier = PushoverNotifier()
    except ValueError as e:
        print(f"✗ Warning: Pushover not configured: {e}")
        notifier = None
    
    try:
        # Initialize Supabase client
        supabase_url = os.getenv("SUPABASE_API_URL")
        supabase_key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
        
        if not supabase_url or not supabase_key:
            if notifier:
                notifier.send_notification(
                    message="Problem running Remove Script",
                    title="Supabase Activity"
                )
            raise ValueError("SUPABASE_API_URL and SUPABASE_SERVICE_ROLE_KEY must be set in .env file")
        
        supabase: Client = create_client(supabase_url, supabase_key)
        
        table_name = os.getenv("SUPABASE_TABLE", "progress")
        
        if not entry_id and week_number is None:
            print("✗ Please provide either week_number or entry_id to remove")
            print("Usage:")
            print("  python Remove.py <week_number>")
            print("  python Remove.py --id <entry_id>")
            if notifier:
                notifier.send_notification(
                    message="Problem running Remove Script",
                    title="Supabase Activity"
                )
            return None
        
        # Perform deletion
        if entry_id:
            response = supabase.table(table_name).delete().eq("id", entry_id).execute()
            identifier = f"ID {entry_id}"
        else:
            response = supabase.table(table_name).delete().eq("week_number", week_number).execute()
            identifier = f"week_number {week_number}"
        
        # Check if any rows were deleted
        if response.data and len(response.data) > 0:
            print(f"✓ Entry with {identifier} removed successfully from '{table_name}' table")
            if notifier:
                notifier.send_notification(
                    message="Entry Deleted",
                    title="Supabase Activity"
                )
        else:
            print(f"✗ Entry with {identifier} not found in '{table_name}' table")
            if notifier:
                notifier.send_notification(
                    message="Entry not Found",
                    title="Supabase Activity"
                )
        
        return response
        
    except Exception as e:
        print(f"✗ Error removing entry: {e}")
        if notifier:
            notifier.send_notification(
                message="Problem running Remove Script",
                title="Supabase Activity"
            )
        return None

def list_entries():
    """List all entries in the database"""
    
    # Initialize Supabase client
    supabase_url = os.getenv("SUPABASE_API_URL")
    supabase_key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
    
    if not supabase_url or not supabase_key:
        raise ValueError("SUPABASE_API_URL and SUPABASE_SERVICE_ROLE_KEY must be set in .env file")
    
    supabase: Client = create_client(supabase_url, supabase_key)
    
    table_name = os.getenv("SUPABASE_TABLE", "progress")
    
    try:
        response = supabase.table(table_name).select("id, week_number, date, weight").order("week_number").execute()
        
        if response.data:
            print("\nCurrent entries in database:")
            print("-" * 70)
            print(f"{'ID':<40} {'Week':<8} {'Date':<12} {'Weight':<8}")
            print("-" * 70)
            for entry in response.data:
                print(f"{entry.get('id', 'N/A'):<40} {entry.get('week_number', 'N/A'):<8} {entry.get('date', 'N/A'):<12} {entry.get('weight', 'N/A'):<8}")
        else:
            print("No entries found in database")
            
    except Exception as e:
        print(f"✗ Error listing entries: {e}")

if __name__ == "__main__":
    print("Remove Entry from Supabase")
    print("-" * 50)
    
    # Parse command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == "--list":
            list_entries()
        elif sys.argv[1] == "--id" and len(sys.argv) > 2:
            remove_entry(entry_id=sys.argv[2])
        elif sys.argv[1] == "--help":
            print("Usage:")
            print("  python Remove.py <week_number>       # Remove by week number")
            print("  python Remove.py --id <entry_id>     # Remove by ID")
            print("  python Remove.py --list              # List all entries")
            print("  python Remove.py --help              # Show this help")
        else:
            try:
                week_num = int(sys.argv[1])
                remove_entry(week_number=week_num)
            except ValueError:
                print(f"✗ Invalid week number: {sys.argv[1]}")
                print("Use --help for usage information")
    else:
        print("Usage:")
        print("  python Remove.py <week_number>       # Remove by week number")
        print("  python Remove.py --id <entry_id>     # Remove by ID")
        print("  python Remove.py --list              # List all entries")
        print("  python Remove.py --help              # Show this help")

