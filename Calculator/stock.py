# This code is made by MRayan Asim
# Packages needed:
# pip install yfinance
import yfinance as yf


# Function to fetch stock information
def get_stock_info(symbol):
    stock = yf.Ticker(symbol)

    # Get stock info
    info = stock.info

    # Extract desired information
    current_price = stock.history().tail(1)["Close"].iloc[0]
    market_cap = info.get("marketCap", "N/A")
    volume = info.get("regularMarketVolume", "N/A")
    previous_close = info.get("previousClose", "N/A")
    high = info.get("dayHigh", "N/A")
    low = info.get("dayLow", "N/A")

    # Print the stock information
    print(f"Stock Symbol: {symbol}")
    print(f"Current Price: {current_price}")
    print(f"Market Cap: {market_cap}")
    print(f"Volume: {volume}")
    print(f"Previous Close: {previous_close}")
    print(f"Day's High: {high}")
    print(f"Day's Low: {low}")


symbol = input("Enter the stock symbol: ")
get_stock_info(symbol)
