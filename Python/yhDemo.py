import yfinance as yf

msft = yf.Ticker("APPL")
msft.fast_info


print(msft.history_metadata)
print("============================")

print(msft.major_holders)

print("============================")

print(msft.info)