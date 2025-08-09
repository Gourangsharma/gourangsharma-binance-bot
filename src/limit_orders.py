from config import client
import sys
import logging


logging.basicConfig(filename='bot.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def place_limit_order(symbol, side, quantity, price):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side.upper(),
            type='LIMIT',
            quantity=quantity,
            price=price,
            timeInForce='GTC'
        )
        logging.info(f"LIMIT ORDER: {side} {quantity} {symbol} @ {price}")
        print("Limit order sent!")
    except Exception as e:
        logging.error(f"LIMIT ORDER FAILED: {str(e)}")
        print("Error placing limit order:", e)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python limit_orders.py <symbol> <side> <quantity> <price>")
        sys.exit(1)

    symbol = sys.argv[1]
    side = sys.argv[2]
    quantity = float(sys.argv[3])
    price = str(sys.argv[4])

    place_limit_order(symbol, side, quantity, price)
