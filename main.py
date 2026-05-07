import os
import requests
import google.generativeai as genai
from dotenv import load_dotenv

# Load credentials securely
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_market_data():
    # Example: Pulling BTC price from Binance
    response = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
    return response.json()

def analyze_with_gemini(data):
    model = genai.GenerativeModel('gemini-pro')
    prompt = f"Analyze this price data: {data}. Provide a 1-sentence market sentiment summary."
    response = model.generate_content(prompt)
    return response.text

def send_telegram_alert(message):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("CHAT_ID")
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url)

# Main Execution Logic
if __name__ == "__main__":
    data = get_market_data()
    summary = analyze_with_gemini(data)
    send_telegram_alert(f"🚀 Market Alert: {summary}")
