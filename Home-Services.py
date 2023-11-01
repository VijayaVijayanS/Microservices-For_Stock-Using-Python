import os
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


def main():
    print("Alpaca API Console Application - Stock Information Retrieval")

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
        else:
            print(f"Stock symbol '{symbol}' not found or an error occurred.")


if __name__ == "__main__":
    main()
 
