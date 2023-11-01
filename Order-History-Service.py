import alpaca_trade_api as tradeapi

# Set your Alpaca API credentials
ALPACA_API_KEY = 'PKQXY66TMDHLUTYEWVXG'
ALPACA_SECRET_KEY = 'YNYnaq3s80lgN5MAb2E4QQmyePWr49kFHL6XU6aq'
ALPACA_BASE_URL = 'https://paper-api.alpaca.markets'  # Use 'https://api.alpaca.markets' for live trading

# Initialize Alpaca API client
api = tradeapi.REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, base_url=ALPACA_BASE_URL)

def retrieve_stock_info(symbol):
    try:
        asset = api.get_asset(symbol)
        return asset
    except tradeapi.rest.APIError as e:
        print(f"Error: {e}")
        return None

def place_buy_order(symbol, qty):
    try:
        api.submit_order(
            symbol=symbol,
            qty=qty,
            side='buy',
            type='market',
            time_in_force='gtc'
        )
        print(f"Buy order for {qty} shares of {symbol} placed successfully.")
    except tradeapi.rest.APIError as e:
        print(f"Error placing buy order: {e}")

def place_sell_order(symbol, qty):
    try:
        api.submit_order(
            symbol=symbol,
            qty=qty,
            side='sell',
            type='market',
            time_in_force='gtc'
        )
        print(f"Sell order for {qty} shares of {symbol} placed successfully.")
    except tradeapi.rest.APIError as e:
        print(f"Error placing sell order: {e}")

def retrieve_and_display_orders():
    try:
        orders = api.list_orders()
        if orders:
            print("\nOrders:")
            for order in orders:
                print(f"Order ID: {order.id}")
                print(f"Symbol: {order.symbol}")
                print(f"Side: {order.side}")
                print(f"Quantity: {order.qty}")
                print(f"Type: {order.type}")
                print(f"Status: {order.status}")
                print()
        else:
            print("No orders found.")
    except tradeapi.rest.APIError as e:
        print(f"Error retrieving orders: {e}")

def main():
    print("Alpaca API Console Application - Stock Information, Buy Order, Sell Order, and Orders")

    while True:
        symbol = input("\nEnter a stock symbol (e.g., AAPL): ")

        if symbol.upper() == 'EXIT':
            print("Exiting...")
            break

        stock_info = retrieve_stock_info(symbol)
        if stock_info:
            print("\nStock Information:")
            print(f"Symbol: {stock_info.symbol}")
            print(f"Name: {stock_info.name}")
            print(f"Exchange: {stock_info.exchange}")
            print(f"Tradable: {'Yes' if stock_info.tradable else 'No'}")
            print(f"Status: {stock_info.status}")

            action = input("Enter 'B' to buy, 'S' to sell, or 'O' to view orders: ")
            if action.upper() == 'B':
                qty = int(input("Enter the quantity to buy: "))
                place_buy_order(symbol, qty)
            elif action.upper() == 'S':
                qty = int(input("Enter the quantity to sell: "))
                place_sell_order(symbol, qty)
            elif action.upper() == 'O':
                retrieve_and_display_orders()
            else:
                print("Invalid action. Please enter 'B', 'S', or 'O'.")
        else:
            print(f"Stock symbol '{symbol}' not found or an error occurred.")

if __name__ == "__main__":
    main()
