# insert company profile into company_profile table
# with 

import mysql.connector
import yfinance as yf
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
)

li = ['2S', '3K-BAT', '7UP', 'A', 'AAI', 'AAV', 'ACC', 'ACE', 'ACG', 'ADVANC',
    'AEONTS', 'AFC', 'AGE', 'AH', 'AHC', 'AI', 'AIE', 'AIMCG', 'AIMIRT', 'AIT',]

def newList(li):
  return [i+'.BK' for i in li]
new_li = newList(li)

mycursor = mydb.cursor()
for i in new_li:
    print(i)
    key = yf.Ticker(i)
    key = key.info
    index = new_li.index(i)+1
    # print(key)
    # print(key.get('longName'))
    sql = "REPLACE INTO sp01.company_profile (profile_id, stock_id, company_name, address, phone_number, website, company_description) VALUES (%s, %s, %s, %s, %s, %s, %s)"
     
    
    val = [(index, index ,key.get('longName'), key.get('address1'), key.get('phone'), key.get('website'), key.get('longBusinessSummary'))] 
    

    mycursor.executemany(sql, val)

    mydb.commit()

print(mycursor.rowcount, "was inserted.")