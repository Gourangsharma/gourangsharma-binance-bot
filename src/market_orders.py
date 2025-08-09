from config import client
import sys
import logging


logging.basicConfig(filename='bot.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def place_market_order(symbol, side, quantity):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side.upper(),
            type='MARKET',
            quantity=quantity
        )
        logging.info(f"Market Order Placed: {order}")
        print("Order placed")
        print(order)
    except Exception as e:
        logging.error(f"Error placing market order: {str(e)}")
        print("Failed to place order:", e)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python market_orders.py <symbol> <side> <quantity>")
        print("Example: python market_orders.py BTCUSDT BUY 0.01")
        sys.exit(1)

    symbol = sys.argv[1]
    side = sys.argv[2]
    quantity = float(sys.argv[3])

    place_market_order(symbol, side, quantity)
