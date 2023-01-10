import yfinance as yf

msft = yf.Ticker("2S.BK")

data = msft.info 
# rf = data.split()

# print(type(data))
keys = []
values = []
for i in data:
    keys.append(i)
    values.append(data[i])

# print("keys : ", str(keys))
# print("values : ", str(values))
print("\n")
# [print(key,':',value) for key, value in data.items()]

print(data.get('longBusinessSummary'))