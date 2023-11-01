# Stock Trading Application with Alpaca API Using Python

## Introduction
This repository contains a set of Python scripts that utilize the Alpaca API to perform various tasks related to stock trading. These scripts are designed to be modular and can be used together to build a comprehensive stock trading application.

## Installation

1. Install Dependencies:
   
      pip install alpaca-trade-api


2. Set Alpaca API Credentials:
Replace the `ALPACA_API_KEY` and `ALPACA_SECRET_KEY` variables in the scripts with your own API credentials.

## Usage

You can now run the individual scripts based on your requirements.

### Microservices Overview and Function Signature:

1. **Retrieve Stock Information**

     Description: This microservice allows you to retrieve detailed information about a specific stock.


              def retrieve_stock_info(symbol: str) -> dict:
 

2. **Place Buy Order**

     Description: This microservice enables you to place a buy order for a specific stock.

 
              def place_buy_order(symbol: str, qty: int) -> None:
 

3. **Place Sell Order**

     Description: This microservice allows you to place a sell order for a specific stock.

              def place_sell_order(symbol: str, qty: int) -> None:
 

4. **Retrieve Order History**

     Description: This microservice retrieves the order history for your account.

              def retrieve_and_display_orders() -> None:
 

5. **Add to Cart**

     Description: This microservice allows you to add stocks to a cart for later processing.

              def add_to_cart(stock_symbol: str) -> None:
 

6. **View Cart**

     Description: This microservice displays the contents of the cart.

              def view_cart() -> None:
 

7. **Buy Stocks**

     Description: This microservice allows you to buy the stocks in your cart.

              def buy_stocks() -> None:
 

## Example Usage

### Example 1: Retrieve stock information

    stock_info = retrieve_stock_info('AAPL')
    print(stock_info)

### Example 2: Place a buy order

    place_buy_order('AAPL', 10)

### Example 3: Place a sell order

    place_sell_order('AAPL', 5)

### Example 4: Retrieve and display order history

    retrieve_and_display_orders()

### Example 5: Add stocks to cart

    add_to_cart('AAPL')
    add_to_cart('GOOGL')

### Example 6: View cart

    view_cart()

### Example 7: Buy stocks from the cart

    buy_stocks()


**Note: Ensure you have valid Alpaca API credentials to use these services. Use the Paper Trading API for testing.


