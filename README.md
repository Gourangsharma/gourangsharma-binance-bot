# GourangSharma-Trading-Bot

This is a simple Python-based trading bot for Binance Futures Testnet.  
It can place **Market** and **Limit** orders via the official Binance Futures API.

---

## Features
- Place Market Orders (Buy/Sell)
- Place Limit Orders (Buy/Sell)
- Stop Limit Orders
- Simple CLI Menu for easy interaction
- Uses `.env` to store API credentials securely
- Logs API requests, responses, and errors to `bot.log`

---

## 1. API Setup Instructions

1. **Create a Binance Futures Testnet account**  
   Visit: [https://testnet.binancefuture.com](https://testnet.binancefuture.com) and register.

2. **Generate API Keys**  
   - Go to API Management.
   - Create a new API key for the Futures Testnet.
   - Enable permissions: `TRADE` and `USER_DATA`.
   - Copy the **API Key** and **API Secret**.

3. **Store API Keys in `.env` file**  
   Create a file named `.env` in the project root:
   ```env
   API_KEY=your_testnet_api_key_here
   API_SECRET=your_testnet_api_secret_here

---

## 2. Install Requirements
Make sure Python 3.9+ is installed. Then run:
pip install -r requirements.txt

---

## 3. How to Run the Bot

Option 1 — Run Market Order Directly  
python src/market_orders.py BTCUSDT BUY 0.01  
- `BTCUSDT` → trading pair  
- `BUY` or `SELL` → order side  
- `0.01` → quantity

Option 2 — Run Limit Order Directly  
python src/limit_orders.py BTCUSDT SELL 0.01 42000  
- Last value is the **limit price**.

Option 3 — Use CLI Menu (Recommended for easy use)  
python cli_menu.py  
This shows a simple menu:
=== Binance Futures Bot Menu ===
1. Place Market Order
2. Place Limit Order
3. Exit
Follow the prompts.

---

## 4. Logs
All bot activity and errors are stored in:
bot.log

For demonstration, a simulated log with successful orders is also provided:
bot_demo.log

---

## 5. Notes
- If API keys are invalid or Binance Testnet is down, you may see:
  APIError(code=-2015): Invalid API-key, IP, or permissions for action
  This is normal if the Testnet API is not accepting orders.
- Once valid keys are available, the bot will place orders successfully.

---

## Author
Gourang Sharma

