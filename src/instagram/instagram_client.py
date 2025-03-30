import sys
import os


# Append the parent directory (project root) to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, "..")
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from apify_client import ApifyClient
from comon.config import APIFY_API_TOKEN  # Import the token from config

def fetch_latest_instagram_post(instagram_username: str = "bbcnews") -> dict:
    
    if not APIFY_API_TOKEN:
        raise ValueError("APIFY_API_TOKEN is not set.")

    try:
        # Initialize the ApifyClient with the API token
        client = ApifyClient(APIFY_API_TOKEN)
        
        # Prepare the Actor input
        run_input = {
            "username": [instagram_username],  # Pass the username as a list
            "resultsLimit": 1,  # Limit to one (latest) post
        }
        
        # Call the actor using the working actor ID "nH2AHrwxeTRJoN5hX"
        run = client.actor("nH2AHrwxeTRJoN5hX").call(run_input=run_input)
        
        return client.dataset(run["defaultDatasetId"])
            
    
    except Exception as e:  
        raise e

if __name__ == "__main__":
    try:
        result = fetch_latest_instagram_post("bbcnews")
        for item in result.iterate_items():
            print("Latest Post:", item['caption'])
    except Exception as err:
        print("An error occurred:", err)
