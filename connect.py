import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1234'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT stock_id, symbol FROM sp01.stock")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)