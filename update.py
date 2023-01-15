import mysql.connector
import yfinance as yf

li = [ '2S', '3K-BAT', '7UP', 'A', 'AAI', 'AAV', 'ACC', 'ACE', 'ACG', 'ADVANC', 
'AEONTS', 'AFC', 'AGE', 'AH', 'AHC', 'AI', 'AIE', 'AIMCG', 'AIMIRT', 'AIT',
'AJ', 'AJA', 'AKR', 'ALLA', 'ALLY', 'ALT', 'ALUCON', 'AMANAH', 'AMARIN', 'AMATA', 
'AMATAR', 'AMATAV', 'AMC', 'AMR', 'ANAN', 'AOT', 'AP', 'APCO', 'APCS', 'APEX', 
'APURE', 'AQ', 'AQUA', 'AS', 'ASAP', 'ASEFA', 'ASIA', 'ASIAN', 'ASIMAR', 'ASK',
'ASP', 'ASW', 'AURA', 'AWC', 'AYUD', 'B','B', 'B52', 'BA','BAFS',
'BAM', 'BANPU', 'BAREIT', 'BAY', 'BBGI', 'BBL', 'BCH', 'BCP', 'BCPG', 'BCT',
'BDMS', 'BEAUTY', 'BEC', 'BEM', 'BEYOND', 'BGC', 'BGRIM', 'BH', 'BIG', 'BIOTEC',
'BIZ','BJC', 'BJCHI', 'BKD', 'BKI', 'BKKCP', 'BLA', 'BLAND', 'BLISS', 'BOFFICE', 
'BPP', 'BR', 'BRI', 'BROCK', 'BRR', 'BRRGIF', 'BSBM', 'BTG', 'BTNC', 'BTS' ]

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
    val = [(info.get('sector'), info.get('industry'), i, index+1)]

    mycursor.executemany(sql, val)
    mydb.commit()

print(mycursor.rowcount, "was inserted.")


#in li second index 57 'B' = B-WORK, 56 = B  
#B-work, bkd, bliss, brrgif