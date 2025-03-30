# Instagram-to-X Integration System

A backend system that fetches the latest Instagram post from **bbcnews**, summarizes its caption using AI, and posts it to X.com.

---

## 📝 Table of Contents
- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [API Endpoints](#-api-endpoints)
- [Testing](#-testing)
- [Deployment](#-deployment)
- [Customization](#-customization)
- [Architecture](#-architecture)
- [License](#-license)

---

## 🚀 Features
### **Part 1: Instagram Data Fetching**
- Fetches the latest post’s **caption** and **image URL** from the BBC News Instagram account.
- Robust error handling for network issues, rate limits, and invalid responses.
- Supports custom Instagram usernames via configuration.

### **Part 2: Caption Summarization & X.com Integration**
- Uses **Google Gemini** (free LLM) to generate concise summaries (≤280 characters).
- Posts summarized tweets to X.com via the Twitter API v1.1.
- REST API endpoint (`/post-tweet`) to trigger the workflow.

---

## 📦 Prerequisites
- Python 3.10+
- Instagram account credentials (optional, uses Apify scraping as fallback)
- [Google Gemini API Key](https://aistudio.google.com/app/apikey)
- [X.com Developer Credentials](https://developer.twitter.com/)

---

## 🛠 Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/instagram-x-integration.git
cd instagram-x-integration

# Install dependencies
pip install -r requirements.txt
```

---

## ⚙ Configuration
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

Update `.env` with your credentials:
```ini
# Required APIs
APIFY_API_TOKEN="your_apify_token"       # For Instagram scraping
GEMINI_API_KEY="your_gemini_key"         # For summarization
X_API_KEY="your_x_api_key"
X_API_SECRET="your_x_api_secret"
X_ACCESS_TOKEN="your_x_access_token"
X_ACCESS_TOKEN_SECRET="your_x_token_secret"

# Optional Overrides
INSTAGRAM_USERNAME="bbcnews"             # Change target account
LOG_LEVEL="INFO"                         # DEBUG/INFO/WARNING/ERROR
```

---

## 🖥 Usage
Run the API Server:
```bash
python -m src.api.app
```

Access Swagger docs at [http://localhost:8000/docs](http://localhost:8000/docs).

Trigger the Workflow:
```bash
curl -X POST http://localhost:8000/post-tweet
```

Response:
```json
{
  "success": true,
  "tweet_text": "Summary of the caption...",
  "original_caption": "Full caption from Instagram..."
}
```

---

## 🛡 API Endpoints
| Endpoint       | Method | Description                              |
|---------------|--------|------------------------------------------|
| `/post-tweet` | POST   | Fetches, summarizes, and posts to X.com |
| `/health`     | GET    | Health check (`{"status": "ok"}`)       |

---

## 🧪 Testing
Run unit and integration tests:
```bash
# Run all tests
python -m pytest tests/

# Test specific modules
python -m pytest tests/test_instagram.py      # Part 1 tests
python -m pytest tests/test_summarization.py  # Part 2 LLM tests
python -m pytest tests/test_xcom.py           # Part 2 X.com tests
```

---

## 💪 Deployment
### Docker Containerization:
```bash
# Build the image
docker build -t instagram-x-integration .

# Run the container
docker run -p 8000:8000 --env-file .env instagram-x-integration
```

---

## 🔧 Customization
### Change Instagram Account:
Update `INSTAGRAM_USERNAME` in `.env`.

### Modify Summarization Logic:
Edit `src/summarization/llm_summarizer.py` to tweak the LLM prompt.

### Add Automation:
Use cron jobs or Celery to schedule `/post-tweet` executions.

---

## 🏢 Architecture
```
┌─────────────┐       ┌──────────────┐       ┌───────────┐
│ Instagram   │       │ Google       │       │ X.com     │
│ Client      │──────▶│ Gemini       │──────▶│ API       │
└─────────────┘       └──────────────┘       └───────────┘
      ▲                      ▲                      ▲
      │ Fetch Post           │ Summarize            │ Post Tweet
      │                      │                      │
┌─────┴──────┐         ┌─────┴──────┐         ┌─────┴──────┐
│ FastAPI    │         │ LLM        │         │ X.com      │
│ Endpoint   │         │ Module     │         │ Client     │
└────────────┘         └────────────┘         └────────────┘
```

---


