# FinPulse-AI 🚀

A professional-grade Python automation pipeline that integrates real-time financial market data with **Google Gemini AI** for deep sentiment analysis and automated **Telegram** alerting.

## 📌 Key Features
- **Automated Data Ingestion:** Fetches live price data via REST APIs (Binance).
- **AI-Driven Research:** Leverages the **Gemini-Pro** model to transform raw data into human-readable market sentiment.
- **Enterprise Logging:** Built-in Python `logging` module to track script heartbeats and performance.
- **Error Resilience:** Implements `try-except` blocks to handle API timeouts or network failures gracefully.
- **Cloud Optimized:** Designed for headless deployment on **Google Cloud Compute Engine (GCP)** or any Linux VPS using `cron`.

## 🛠️ Technical Stack
- **Language:** Python 3.10+
- **LLM Engine:** Google Generative AI (Gemini)
- **Networking:** Requests (REST API)
- **Security:** `python-dotenv` for environment variable isolation.

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.x installed.
- Telegram Bot Token & Chat ID.
- Google Gemini API Key.

### 2. Installation
Clone the repository and install dependencies:
```bash
apt install python3 
git clone [https://github.com/anonymousblessed21/Finpulse-AI.git](https://github.com/anonymousblessed21/Finpulse-AI.git)
cd Finpulse-AI
pip install -r requirements.txt
py main.py
```
### 🔐Security Notice
This project uses .env files to ensure that all sensitive credentials (API keys, Tokens) are kept out of the source code. The .gitignore is pre-configured to prevent accidental exposure of these secrets.
