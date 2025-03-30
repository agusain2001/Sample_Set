import os
import google.generativeai as genai
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, "..")
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from comon.logger import logger
from comon.config import GEMINI_API_TOKEN
# import sys
# from dotenv import load_dotenv




class LLMSummarizer:
    def __init__(self):
        # if not GEMINI_API_TOKEN:
        #     raise ValueError("GEMINI_API_TOKEN is not configured")
        genai.configure(api_key=GEMINI_API_TOKEN)
        self.model = genai.GenerativeModel('gemini-2.0-flash')

    def summarize_for_tweet(self, caption: str) -> str:
        """Summarize text for Twitter's 280 character limit"""
        try:
            prompt = f"Summarize this Instagram caption into a concise tweet (max 280 characters): {caption}"
            response = self.model.generate_content(prompt)
            summary = response.text.strip()
            
            if len(summary) > 280:
                return self._truncate_summary(summary)
            return summary
        except Exception as e:
            logger.error(f"Summarization failed: {str(e)}")
            raise

    def _truncate_summary(self, text: str) -> str:
        """Fallback truncation if LLM exceeds limit"""
        return text[:277] + "..."
    
