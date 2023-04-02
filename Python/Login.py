from configparser import MAX_INTERPOLATION_DEPTH
import yfinance as yf
from concurrent.futures import process
from crypt import methods
from datetime import datetime
from re import A, I, search
from time import time
from traceback import format_exc
from unittest import result
from urllib import response
from webbrowser import get
from click import password_option
from flask import Flask,request,jsonify,session
from flask_cors import *
from importlib_metadata import email
import db
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route("/login",methods=['POST'])
def trylogin():
    print(request.json)
    email = request.json.get('email'),
    password = request.json.get('password'),
    print(email[0]),     
    print(password[0]),
    sql = f"SELECT * FROM stockproject.accounts where Email='{email[0]}';"
    datas = db.query_data(sql)
    password2 = datas[0]["Password"]
    print(password)
    print(password2)
    if(password2 == password[0]):
        accountid = datas[0]["AccountId"]
        username = datas[0]["FirstName"]+datas[0]["LastName"]
        region = datas[0]["Region"]
        birthdate = datas[0]["BOD"]
        email = datas[0]["Email"]
        json_result = {"state": 1, "vData":{"token":"asdasdasdasdad","accountid":accountid, "username":username,"region":region,"birthdate":birthdate,"email":email}}
        print(json_result)
        return jsonify(json_result)
    else:
        return "true"




@app.route("/signup", methods=['POST'])
def addNewUser():
    firstname = request.json.get('firstname'),
    lastname = request.json.get('lastname'),
    region = request.json.get('region'),
    bod = request.json.get('bod'),
    email = request.json.get('email'),
    password = request.json.get('password'),
    print(firstname)
    print(lastname)
    print(region)
    print(bod)
    print(email)
    print(password)
    sql = f"INSERT INTO `stockproject`.`accounts` (`FirstName`, `LastName`, `Region`, `Bod`, `Email`, `Password`, `LoginToken`) VALUES ('{firstname[0]}', '{lastname[0]}', '{region[0]}', '{bod[0]}', '{email[0]}', '{password[0]}', 'zxcvbnmasdfghjklqwertyuiopasd');"
    db.insert_or_update_data(sql)
    json_result = {"state": 1, "vData":{"token":"asdasdasdasdad","name":"admin"}}
    return jsonify(json_result)

@app.route("/editprofile", methods=['POST'])
def edituser():
    accountid = request.json.get('accountid'),
    firstname = request.json.get('firstname'),
    lastname = request.json.get('lastname'),
    region = request.json.get('region'),
    bod = request.json.get('bod'),
    email = request.json.get('email'),
    print(accountid)
    print(firstname)
    print(lastname)
    print(region)
    print(bod)
    print(email)
    ##sql = f"UPDATE stockproject SET `accounts` (`FirstName`, `LastName`, `Region`, `Bod`, `Email`, `LoginToken`) VALUES ('{firstname[0]}', '{lastname[0]}', '{region[0]}', '2023-2-7', '{email[0]}', 'zxcvbnmasdfghjklqwertyuiopasd' WHERE AccountId = {accountid[0]};"
    ##sql = f"UPDATE `stockproject`.`accounts` SET `FirstName` = '{firstname[0]}', `LastName` = '{lastname[0]}', `Region` = '{region[0]}', `BOD` = '{bod[0]}', `Email` = '{email[0]}', `LoginToken` = 'asdasdasdasd' WHERE (`AccountId` = '{accountid[0]}');"
    ##sql = f"UPDATE `stockproject`.`accounts` (`FirstName`, `LastName`, `Region`, `Bod`, `Email`, `LoginToken`) VALUES ('{firstname[0]}', '{lastname[0]}', '{region[0]}', '{bod[0]}', '{email[0]}', 'zxcvbnmasdfghjklqwertyuiopasd' WHERE AccountId = {accountid[0]});"
    sql = f"UPDATE `stockproject`.`accounts` SET `FirstName` = '{firstname[0]}', `LastName` = '{lastname[0]}', `Region` = '{region[0]}', `Bod` = '{bod[0]}', `Email` = '{email[0]}', `LoginToken` = 'zxcvbnmasdfghjklqwertyuiopasd' WHERE `AccountId` = {accountid[0]};"
    print(sql)
    db.insert_or_update_data(sql)
    json_result = {"state": 1, "vData":{"token":"asdasdasdasdad","name":"admin"}}
    return jsonify(json_result)

@app.route("/editpassword", methods=['POST'])
def editpassword():
    email = request.json.get('email'),
    password = request.json.get('password'),
    print(password)

    sql = f"UPDATE `stockproject`.`accounts` SET  `Password` = '{password[0]}', `LoginToken` = 'zxcvbnmasdfghjklqwertyuiopasd' WHERE `Email` = '{email[0]}';"
    print(sql)
    db.insert_or_update_data(sql)
    json_result = {"state": 1, "vData":{"token":"asdasdasdasdad","name":"admin"}}
    return jsonify(json_result)



@app.route('/question/<string:symbol>',methods=['POST'])
def question(symbol):
    quizzes = []
    sql = f"SELECT  * FROM stockproject.Multiple_choice where chapterid = {symbol} ORDER by rand() limit 10 "
    datas = db.query_data(sql)
   
    ##选项+答案
    for question in datas: 
        quiz = {
            "text":question["question"],
            "responses":[] 

        }
        
        correctAnswer = question["answer"]
        
        responsees = quiz["responses"]
        ##A
        A = question["option_a"]
        if correctAnswer == "A":
            AnswerA= {"text":f"{A}","correct":True}
            responsees.append(AnswerA)
        else:
            AnswerA= {"text":f"{A}"}
            responsees.append(AnswerA)
        
         ##B
        B = question["option_b"]
        if correctAnswer == "B":
            AnswerB= {"text":f"{B}","correct":True}
            responsees.append(AnswerB)
        else:
            AnswerB= {"text":f"{B}"}
            responsees.append(AnswerB)

         ##C
        C = question["option_c"]
        if correctAnswer == "C":
            AnswerC= {"text":f"{C}","correct":True}
            responsees.append(AnswerC)
        else:
            AnswerC= {"text":f"{C}"}
            responsees.append(AnswerC)

         ##D
        D = question["option_d"]
        if correctAnswer == "D":
            AnswerD= {"text":f"{D}","correct":True}
            responsees.append(AnswerD)
        else:
            AnswerD= {"text":f"{D}"}
            responsees.append(AnswerD)
        
        quizzes.append(quiz)

    return quizzes


@app.route("/knowledge/recordcheck",methods=['POST'])
def createRecord():
    #1.check record 
    #2. if record is null then create a new learning record 
    details =  request.get_data()
    result = json.loads(details)
    currentime  = str(datetime.now())
    print(result)
    print(currentime)
    userid = result['userid']
    if userid is None:
        return jsonify(status = "Success")

    chapterid = result['chapterid']
    subchapterindex = result['subchapterindex']
    sql = f"SELECT * FROM stockproject.subchapters where chapters_id = {chapterid} and subchapterIndex = {subchapterindex}"
    datas = db.query_data(sql)
    print(datas)
    print(len(datas))
    if len(datas) == 1:
         subid  = datas[0]['subchapters_id']
         print(subid)
         sql = f"SELECT * FROM stockproject.Learning_process where chapter_id = {chapterid} and subchapters_id= {subchapterindex} and AccountId = {userid}"
         print(sql)
         datas = db.query_data(sql)
         print(datas)
         if len(datas) == 0:
            print("insert")
            
            sql = f"INSERT INTO `stockproject`.`Learning_process` (`AccountId`, `chapter_id`, `subchapters_id`,`isLearned`,`Time`) VALUES ({userid},{chapterid},{subchapterindex},'1','{currentime}');"
            print(sql)
            db.insert_or_update_data(sql)
         elif len(datas) == 1:
              print(datas[0])
              lsid = datas[0]["Learning_process id"]
              print("update")
              print(lsid)
              sql = f"UPDATE `stockproject`.`Learning_process` SET `isLearned` = '1', `Time` = '{currentime}'  WHERE (`Learning_process id` = {lsid});"
              db.insert_or_update_data(sql)

        

    return jsonify(status = "Success")

@app.route("/knowledge/getlearningprocess/<string:userid>",methods=['POST'])
def getlearningprocess(userid):
    #1.forearch chapters
    learningResult = []
    sql = f"SELECT * FROM stockproject.chapters"
    datas = db.query_data(sql)
    for chapter in datas:
        print(chapter)
        chapterprocess = {
              "chapterid":None,
              "learningprocess":None
        }
        chapterid = chapter["chapters id"]
        chaptername = chapter['ch_name']
        subchaptersCount = chapter['ch_count']
        print(f"id {chapterid}----- name : {chaptername} ---- count :{subchaptersCount}")
        print(userid)
        sql = f"SELECT * FROM stockproject.Learning_process where Accountid = {userid} and chapter_id = {chapterid}"
        print(sql)
        datas = db.query_data(sql)
        print(datas)
        chapterprocess['chapterid'] = chapterid
        resultcount =  len(datas)
        print(subchaptersCount) 
        calResult = resultcount/subchaptersCount
        chapterprocess["learningprocess"] = int(calResult*100)
        learningResult.append(chapterprocess)
    return learningResult

@app.route("/learningprocess/<string:accountid>",methods=['POST'])
def learningprocess(accountid):
    print(accountid)
    sql = f"SELECT * FROM stockproject.Learning_process where AccountId={accountid} order by chapter_id"
    print(sql)
    datas = db.query_data(sql)

    return datas

@app.route("/quizreview/<string:accountid>",methods=['POST'])
def quizreview(accountid):
  
    sql = f"SELECT * FROM stockproject.Quiz_review where AccountId={accountid} order by chapter_id"
    print(sql)
    datas = db.query_data(sql)
    print(datas)
    return datas

@app.route("/quizinput/",methods=['POST'])
def quizinput():
    #sql = f"SELECT * FROM stockproject.Quiz_review where AccountId={accountid} order by chapter_id"
    #datas = db.query_data(sql)
    #print(datas)
    
    datas= request.json
    print(datas)
    accountid = datas['userid']
    currentime  = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
    chapterid = datas['chapter']
    Score = datas['score']
    print(accountid)
    print(currentime)
    print(chapterid)
    print(Score)
    sql = f"INSERT INTO `stockproject`.`Quiz_review` (`AccountId`, `Time`, `chapter_id`, `Score`) VALUES ({accountid}, '{currentime}', {chapterid}, {Score})"
    print (sql)
    datas = db.insert_or_update_data(sql)
    print(datas)
    return jsonify("Success")


@app.route("/forgetpassword/<string:email>",methods=['POST'])
def forgetpassword(email):
    #email = request.json
    print(email)


    fromaddr = 'StockPlentyoffice@gmail.com'
    toaddr = email
    subject = 'Reset Password'
    body = f'Dear User,\n\nPlease click this link to reset your password.\n\nLink: http://localhost:8080/newpassword/{email} \n\nThank you for using our service.\n\nBest Regards,\nStockPlenty'
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    username = 'StockPlentyoffice@gmail.com'
    password = 'blnouavopulnhgxt'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(username, password)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    print("sussess")
    server.quit()
    return jsonify(status = "Success")




@app.route("/GetStockByIndustry/<string:name>",methods=['POST'])
def GetStockByIndustry(name):
    print(name)
    returndatas = []
    sql = f"SELECT * FROM stockproject.stock where industry = '{name}'"
    print (sql)
    datas = db.query_data(sql)
    for  data in datas:
        symbol = data['symbol']
        sql=f"SELECT * FROM stockproject.company_profiles where ticker = '{symbol}'"
        stockdatas = db.query_data(sql)
        
        if(len(stockdatas)==1):
            stockdata = stockdatas[0]
            print(stockdata['ticker'])
            print(stockdata['name'])
            tickerdata = {
                "stockName":stockdata['ticker'],
                "companyName":stockdata['name']
            }
            returndatas.append(tickerdata)
            
    return returndatas



@app.route("/marketinform/<string:ticker>",methods=['POST'])
def marketinform(ticker):
    print(ticker)
    msft = yf.Ticker(f"{ticker}")
    print(msft)
    
    dayhigh = "{:.2f}".format(msft.fast_info.day_high)
    print(dayhigh)
   
    daylow = "{:.2f}".format(msft.fast_info.day_low)
    print(daylow)
   
    lastprice = "{:.2f}".format(msft.fast_info.last_price)
    print(lastprice)
    previousclose = "{:.2f}".format(msft.fast_info.previous_close)
    print(previousclose)

    lastvolume = "{:.2f}".format(msft.fast_info.last_volume)
    print(lastvolume)

    open = "{:.2f}".format(msft.fast_info.open)
    print(open)

    QuoteType = msft.fast_info.quote_type
    print(QuoteType)

    TenDayAverageVolume = "{:.2f}".format(msft.fast_info.ten_day_average_volume)
    print(TenDayAverageVolume)

    ThreeMonthAverageVolume = "{:.2f}".format(msft.fast_info.three_month_average_volume)
    print(ThreeMonthAverageVolume)

    TwoHundredDayAverage = "{:.2f}".format(msft.fast_info.two_hundred_day_average)
    print(TwoHundredDayAverage)

    YearChange = "{:.2f}".format(msft.fast_info.year_change)
    print(YearChange)

    YearHigh = "{:.2f}".format(msft.fast_info.year_high)
    print(YearHigh)

    YearLow = "{:.2f}".format(msft.fast_info.year_low)
    print(YearLow)

    Shares = "{:.2f}".format(msft.fast_info.shares)
    print(Shares)
    ##data = msft.history(period="1y")
    ##json_str = json.dumps(data.to_dict())
    ##print(json_str)

    sql = f"SELECT * FROM stockproject.company_profiles where ticker = '{ticker}'"
    company_profiles = db.query_data(sql)
    msftinfo = {}
    if(len(company_profiles) == 1):
        companyInfo = company_profiles[0]
        print(companyInfo)
        msftinfo = {
        'dayhigh':dayhigh,
        'daylow':daylow,
        'lastprice':lastprice,
        'previousclose':previousclose,
        'lastvolume':lastvolume,
        'open':open,
        'QuoteType':QuoteType,
        'TenDayAverageVolume':TenDayAverageVolume,
        'ThreeMonthAverageVolume':ThreeMonthAverageVolume,
        'TwoHundredDayAverage':TwoHundredDayAverage,
        'YearChange':YearChange,
        'YearHigh':YearHigh,
        'YearLow':YearLow,
        'Shares':Shares,
        'Company':companyInfo
        }
        return msftinfo
    else:
        return msftinfo
    

@app.route("/GetSETCurrentPrice",methods=['POST'])
def GetSETCurrentPrice():
    
    SETTicker = yf.Ticker("^SET.BK")
    
    dayhigh = "{:.2f}".format(SETTicker.fast_info.day_high)
    print(dayhigh)
   
    daylow = "{:.2f}".format(SETTicker.fast_info.day_low)
    print(daylow)
   
    lastprice = "{:.2f}".format(SETTicker.fast_info.last_price)
    print(lastprice)
    SETInfo = {
        'dayhigh':dayhigh,
         'daylow':daylow,
         'lastprice':lastprice
    }
  
    
    return SETInfo


@app.route('/GetWatchlist',methods=['POST'])
def watchlist():
    datas = request.json
    accountid = datas['accountid']
    sql = f"SELECT * FROM stockproject.watchlist where AccountId = {accountid}"
    print(sql)
    datas = db.query_data(sql)
    print(datas)
    return datas




@app.route('/AddToWatchlist',methods=['POST'])
def AddToWatchlist():
    result = {}
    data= request.json
    searchsql = f"SELECT * FROM stockproject.watchlist where Accountid = {data['accountid']} and ticker = '{data['tickerName']}'"
    searchresult = db.query_data(searchsql)
    print(len(searchresult))
    if len(searchresult)==0:
        currentime  = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
        sql = f"INSERT INTO `stockproject`.`watchlist` (`AccountId`, `ticker`, `timestamp`) VALUES ({data['accountid']}, '{data['tickerName']}','{currentime}')"
        result1 = db.insert_or_update_data(sql)
        print(result1)
        print(data)  
    return result

@app.route('/RemoveFromWatchlist',methods=['POST'])
def RemoveFromWatchlist():
    result = {}
    data= request.json
    print(data)
    sql = f"DELETE FROM `stockproject`.`watchlist` WHERE (`watchlistid` = {data['watchlistid']})"
    sqlresult = db.insert_or_update_data(sql)
    print (sqlresult)
    return result

@app.route('/GetBalance',methods=['POST'])
def GetBalance():
    result = {}
    data= request.json
    print(data)
    sql = f"SELECT AccountId , Balance  FROM stockproject.accounts where AccountId = {data['accountid']})"
    sqlresult = db.query_data(sql)
    print (sqlresult[0])
    if len(sqlresult)== 1:
        return sqlresult[0]     
    return result

@app.route('/BuyStock',methods=['POST'])
def BuyStock():
    result = {}
    data= request.json
    print(data)
    return result

@app.route('/SellStock',methods=['POST'])
def SellStock():
    result = {}
    data= request.json   
    return result


@app.route('/GetBuySellHistory',methods=['POST'])
def GetBuySellHistory():
    result = {}
    data= request.json   
    return result

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8088)
