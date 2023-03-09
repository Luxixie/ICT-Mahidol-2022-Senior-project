from crypt import methods
from re import A, I
from unittest import result
from urllib import response
from webbrowser import get
from flask import Flask,request,jsonify,session
from flask_cors import *
import db
import json

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
    print(result)
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
         sql = f"SELECT * FROM stockproject.Learning_process where chapter_id = {chapterid} and subchapters_id= {subid} and AccountId = {userid}"
         datas = db.query_data(sql)
         if len(datas) == 0:
            print("insert")
            sql = f"INSERT INTO `stockproject`.`Learning_process` (`AccountId`, `chapter_id`, `subchapters_id`,`isLearned`) VALUES ({userid},{chapterid},{subchapterindex},'1');"
            db.insert_or_update_data(sql)
         elif len(datas) == 1:
              print(datas[0])
              lsid = datas[0]["Learning_process id"]
              print("update")
              print(lsid)
              sql = f"UPDATE `stockproject`.`Learning_process` SET `isLearned` = '1' WHERE (`Learning_process id` = {lsid});"
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
        print(resultcount/subchaptersCount)
        chapterprocess["learningprocess"] = (resultcount/subchaptersCount)*100
        learningResult.append(chapterprocess)
    return learningResult
    
if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8088)
