import yfinance as yf


# stock_info = yf.Ticker('siri.bk').fast_info
# print("stock_info:", stock_info)
# print(type(stock_info['lastPrice']))

msft = yf.Ticker("intl")
# print(msft.fast_info)
# print("")
# print(msft.info.keys())
# hist = msft.history(period="1mo")
print(msft.fast_info)
# current -previous
# percent = (curent/previose) -1 *100