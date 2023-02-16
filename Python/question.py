import pymysql
import db

conn = pymysql.Connect(        
        host='localhost',
        port=3306,
        user='root',
        password='123456xx?!',
        database='stockproject',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()

cur.execute("SELECT * FROM stockproject.Multiple_choice;"),
sql_select = "SELECT * FROM stockproject.Multiple_choice;"

data_a = cur.fetchone(),
print(data_a),
print("============================="),
data_all = cur.fetchall()
print(data_all)

cur.close(),
conn.close()