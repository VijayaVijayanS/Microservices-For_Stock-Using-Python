import alpaca_trade_api as tradeapi

# Set your Alpaca API credentials
ALPACA_API_KEY = 'PKQXY66TMDHLUTYEWVXG'
ALPACA_SECRET_KEY = 'YNYnaq3s80lgN5MAb2E4QQmyePWr49kFHL6XU6aq'
ALPACA_BASE_URL = 'https://paper-api.alpaca.markets'  # Use 'https://api.alpaca.markets' for live trading

# Initialize Alpaca API client
api = tradeapi.REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, base_url=ALPACA_BASE_URL)

def retrieve_and_display_assets():
    try:
        assets = api.list_assets(status='active')  # You can pass additional parameters to filter assets
        if assets:
            print("List of Assets:")
            for asset in assets:
                print(f"Symbol: {asset.symbol}")
                print(f"Name: {asset.name}")
                print(f"Exchange: {asset.exchange}")
                print(f"Tradable: {'Yes' if asset.tradable else 'No'}")
                print(f"Status: {asset.status}")
                print()
        else:
            print("No assets found.")
    except tradeapi.rest.APIError as e:
        print(f"Error retrieving assets: {e}")

def main():
    print("Alpaca API Console Application - Retrieve and Display Assets")

    retrieve_and_display_assets()

if __name__ == "__main__":
    main()
 
