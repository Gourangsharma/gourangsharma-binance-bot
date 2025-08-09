from binance.client import Client
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')


client = Client(API_KEY, API_SECRET, testnet=True)
try:
    exchange_info = client.futures_exchange_info()
    print("Connected to Binance Futures Testnet!")
except Exception as e:
    print("Connection failed:", e)


