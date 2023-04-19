from cgitb import reset
from traceback import format_exc, print_tb
#from pandas_datareader import data as pdr
import yfinance as yf
import pandas as pd

msft = yf.Ticker("ADVANC.BK")
#print(msft.fast_info)
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

print("===========yearLow=================")
print(msft.major_holders)

print("===========data=================")
data = msft.history(period = "5d")
data = data.sort_index()
print(data)
print(data.to_dict())
dictdata = data.to_dict()
keydata = dictdata.keys()
print(keydata)
opendata = dictdata['Open']
opendatakeys = opendata.keys()
print(opendatakeys)

json = [{
    time:"",
    open:111,
    high:222,
    low:222,
    close:222,
    volume:123123

},]


# data = msft.history(period = "1mo")
# data = data()
# print(data)
# data = msft.history(period = "3mo")
# data = data.sort_index()
# print(data)



