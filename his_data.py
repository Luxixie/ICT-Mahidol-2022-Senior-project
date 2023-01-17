import yfinance as yf
from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd

aot = yf.Ticker("AOT.BK")


aot_his = aot.history(start='2023-01-01', end='2023-01-10', interval='1d')
# print(aot_his.head())

li = ["AOT.BK"]

for i in li:
    # print(i)
    dhr = yf.Ticker(i)
    info = dhr.info
    print(info.keys())
    dhr.get_financials()
    print(i)
    # print(info)
    # print(dhr.get_financials())
    print(info.get('longName'))
    print(info.get('address1'))
    print(info.get('address2'))
    print(info.get('city'))
    print(info.get('zip'))
    print(info.get('country'))
    print(info.get('phone'))
    print(info.get('website'))
    print(info.get('longBusinessSummary'))
   
    print("\n")