import yfinance as yf

msft = yf.Ticker("MSFT")
print(msft.fast_info)
print("==========currency==================")

print(msft.fast_info.currency)

print("===========dayHigh=================")

print(msft.fast_info.day_high)
print("===========dayLow=================")
print(msft.fast_info.day_low)

print("============exchange================")
print(msft.fast_info.exchange)

print("============fiftyDayAverage================")
print(msft.fast_info.fifty_day_average)


print("============lastPrice================")
print(msft.fast_info.last_price)


print("============lastVolume================")
print(msft.fast_info.last_volume)


print("============marketCap================")
print(msft.fast_info.market_cap)


print("============open================")
print(msft.fast_info.open)


print("============previousClose================")
print(msft.fast_info.previous_close)

print("===========quoteType=================")
print(msft.fast_info.quote_type)
print("===========regularMarketPreviousClose=================")
print(msft.fast_info.regular_market_previous_close)

print("==========shares==================")
print(msft.fast_info.shares)

print("==========tenDayAverageVolume==================")
print(msft.fast_info.ten_day_average_volume)

print("==========threeMonthAverageVolume==================")
print(msft.fast_info.three_month_average_volume)

print("==========timezone==================")
print(msft.fast_info.timezone)

print("==========twoHundredDayAverage==================")
print(msft.fast_info.two_hundred_day_average)

print("===========yearChange=================")
print(msft.fast_info.year_change)

print("==========yearHigh==================")
print(msft.fast_info.year_high)

print("===========yearLow=================")
print(msft.fast_info.year_low)

