import pymysql

# Connect to the database
conn = pymysql.Connect(        
        host='localhost',
        port=3306,
        user='root',
        password='123456xx?!',
        database='stockproject',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()

# Retrieve the data
sql = "SELECT Multiple_choiceID,chapterid,question, option_a, option_b, option_c, option_d, answer FROM stockproject.Multiple_choice"
cur.execute(sql)
data = cur.fetchall()


# Close the connection
conn.close()
