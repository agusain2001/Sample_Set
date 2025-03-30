import logging
import sys

# Initialize root logger
logger = logging.getLogger("app")
logger.setLevel(logging.INFO)

# Prevent duplicate handlers
if not logger.handlers:
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)