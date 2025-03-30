from fastapi import FastAPI
import sys
import os


# Append the parent directory (project root) to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, "..")
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from src.comon.logger import logger
from src.api.routes import router  

app = FastAPI()
app.include_router(router)


@app.get("/health")
async def health_check():
    logger.info("Health check endpoint called")
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    logger.info("Starting server...")
    uvicorn.run("src.api.app:app", host="0.0.0.0", port=8000, reload=True)