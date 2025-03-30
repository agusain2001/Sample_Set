from fastapi import APIRouter, HTTPException
import os 
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, "..")
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from instagram.instagram_client import fetch_latest_instagram_post
from summarization.llm_summarizer import LLMSummarizer
from xcom.xcom_client import XClient

router = APIRouter()

@router.post("/post-tweet")
async def post_tweet_endpoint():
    try:
        # Fetch Instagram post
        insta_data = fetch_latest_instagram_post()
        caption = next(insta_data.iterate_items())['caption']
        
        # Summarize caption
        summarizer = LLMSummarizer()

        tweet_text = summarizer.summarize_for_tweet(caption)
        
        print(tweet_text)
        # Post to X.com
        x_client = XClient()
        success = x_client.post_tweet(tweet_text)
        
        return {
            "success": success,
            "tweet_text": tweet_text,
            "original_caption": caption
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))