import os
from dotenv import load_dotenv


load_dotenv()

APIFY_API_TOKEN = os.getenv("APIFY_API_TOKEN")
if not APIFY_API_TOKEN:
    raise ValueError("APIFY_API_TOKEN is not set. Please update your .env file with your Apify API token.")

GEMINI_API_TOKEN =os.getenv("GEMINI_API_KEY")
if not GEMINI_API_TOKEN:
    raise ValueError("GEMINI_API_TOKEN is not set. Please update your .env file with your Apify API token.")

X_API_KEY = os.getenv("X_API_KEY")
X_API_SECRET= os.getenv("X_API_SECRET")
X_ACCESS_TOKEN= os.getenv("X_ACCESS_TOKEN")
X_ACCESS_TOKEN_SECRET=os.getenv("X_ACCESS_TOKEN_SECRET")
 
INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME", "bbcnews")
