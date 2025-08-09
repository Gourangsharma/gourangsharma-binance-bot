from config import client
import sys
import logging


logging.basicConfig(filename='bot.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def place_stop_limit_order(symbol, side, quantity, stop_price, limit_price):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side.upper(),
            type='STOP_MARKET',  
            stopPrice=stop_price,
            closePosition=False,
            timeInForce='GTC',
            quantity=quantity,
            price=limit_price
        )
        logging.info(f"STOP-LIMIT ORDER: {side} {quantity} {symbol} | Stop: {stop_price} → Limit: {limit_price}")
        print("Stop-limit order placed!")
    except Exception as e:
        logging.error(f"STOP-LIMIT FAILED: {str(e)}")
        print("Error placing stop-limit order:", e)

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python stop_limit.py <symbol> <side> <quantity> <stop_price> <limit_price>")
        sys.exit(1)

    symbol = sys.argv[1]
    side = sys.argv[2]
    quantity = float(sys.argv[3])
    stop_price = str(sys.argv[4])
    limit_price = str(sys.argv[5])

    place_stop_limit_order(symbol, side, quantity, stop_price, limit_price)
