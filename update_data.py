import mysql.connector
import yfinance as yf
#update one by one data 
li = [ 'BTG']

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
)
def newList(li):
  return [i+'.BK' for i in li]
data_li = newList(li)

mycursor = mydb.cursor()

for i in data_li:
    dhr = yf.Ticker(i)
    info = dhr.info
    index = data_li.index(i)
    print(i)
    sql = "UPDATE sp01.stock SET sector= %s, industry= %s, symbol= %s WHERE stock_id = %s"
    val = [(info.get('sector'), info.get('industry'), i, '98')]

    mycursor.executemany(sql, val)
    mydb.commit()

print(mycursor.rowcount, "was inserted.")