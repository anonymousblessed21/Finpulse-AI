import os
import requests
import google.generativeai as genai
from dotenv import load_dotenv
import logging

# Set up basic logging to see what the script is doing
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load credentials securely
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_market_data():
    """Fetches real-time BTC price data from Binance."""
    response = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
    return response.json()

def analyze_with_gemini(data):
    """
    Summarizes raw market data into human-readable sentiment 
    using the Gemini-Pro Generative Model.
    """
    model = genai.GenerativeModel('gemini-pro')
    prompt = f"Analyze this price data: {data}. Provide a 1-sentence market sentiment summary."
    response = model.generate_content(prompt)
    return response.text

def send_telegram_alert(message):
    """Sends the final analysis to a designated Telegram chat."""
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("CHAT_ID")
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url)

# Main Execution Logic
if __name__ == "__main__":
    logging.info("Starting the FinPulse-AI pipeline...")
    try:
        data = get_market_data()
        logging.info("Successfully fetched market data.")
        
        summary = analyze_with_gemini(data)
        logging.info("Gemini analysis complete.")
        
        send_telegram_alert(f"🚀 Market Alert: {summary}")
        logging.info("Alert sent successfully!")
        
    except Exception as e:
        logging.error(f"Pipeline failed: {e}")
