from market_orders import place_market_order
from limit_orders import place_limit_order

def main():
    while True:
        print("\n=== Binance Futures Bot Menu ===")
        print("1. Place Market Order")
        print("2. Place Limit Order")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ").strip()
        
        if choice == "1":
            symbol = input("Enter symbol (e.g. BTCUSDT): ").upper()
            side = input("Enter side (BUY/SELL): ").upper()
            qty = input("Enter quantity: ").strip()
            
            place_market_order(symbol, side, qty)
        
        elif choice == "2":
            symbol = input("Enter symbol (e.g. BTCUSDT): ").upper()
            side = input("Enter side (BUY/SELL): ").upper()
            qty = input("Enter quantity: ").strip()
            price = input("Enter limit price: ").strip()
            
            place_limit_order(symbol, side, qty, price)
        
        elif choice == "3":
            print("Exiting bot. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
