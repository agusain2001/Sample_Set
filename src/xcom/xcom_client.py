import tweepy

import os 
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, "..")
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from comon.logger import logger
from comon.config import (
    X_API_KEY,
    X_API_SECRET,
    X_ACCESS_TOKEN,
    X_ACCESS_TOKEN_SECRET
)

class XClient:
    def __init__(self):
        self.client = self._authenticate()

    def _authenticate(self):
        try:
            auth = tweepy.OAuth1UserHandler(
                X_API_KEY,
                X_API_SECRET,
                X_ACCESS_TOKEN,
                X_ACCESS_TOKEN_SECRET
            )
            return tweepy.API(auth)
        except Exception as e:
            logger.error(f"X.com authentication failed: {str(e)}")
            raise

    def post_tweet(self, text: str) -> bool:
        """Post tweet to X.com account"""
        try:
            if len(text) > 280:
                raise ValueError("Tweet exceeds 280 character limit")
            
            response = self.client.update_status(text)
            logger.info(f"Tweet posted: {response.id}")
            return True
        except tweepy.TweepyException as e:
            logger.error(f"Tweet failed: {str(e)}")
            return False