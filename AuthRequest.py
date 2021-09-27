# -*- coding: utf-8 -*-
from urllib.parse import DefragResult
from flask import Flask, render_template, request,redirect, url_for, flash,jsonify, send_file, session,escape
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_,text,update
from datetime import datetime
from sqlalchemy.sql.elements import Null
import os, sys, re, time, random, string, pymysql, sqlalchemy, json, requests
# from requests.api import request
from selenium import webdriver
from SingleModule import kakao_template # 카카오 템플릿 메시지 전송 python


app = Flask(__name__)
app.secret_key = "Secret Key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kakaoAuth.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

client_id = "8c2972daafdf239a443d7943c89253d9" # REST API 키
authorization_code ='' # URL을 통해 가져오는 키

db = SQLAlchemy(app)
class kakaoUser(db.Model): # DB 테이블
    __tablename__ = "kakaoUser"
    UserName = db.Column(db.String(20))
    ToKen = db.Column(db.String(200))
    RefreshToken = db.Column(db.String(200))
    uuid = db.Column(db.String(200),primary_key=True)
    def __init__(self, UserName, ToKen, RefreshToken, uuid) :
        self.UserName = UserName
        self.ToKen = ToKen
        self.RefreshToken = RefreshToken
        self.uuid = uuid


@app.route("/") #기본화면
def index():
    all_data = kakaoUser.query.all()
    return render_template("list.html",all_data=all_data)

@app.route("/KakaoAccept") #카카오 메세지 동의 버튼 클릭
def Accept():
    login_url = "https://kauth.kakao.com/oauth/authorize?client_id="+client_id+"&redirect_uri=https://example.com/oauth&response_type=code&scope=talk_message,friends"

    driver = webdriver.Chrome('../chromedriver.exe') #또는 chromedriver.exe
    driver.maximize_window() # 전체화면
    driver.implicitly_wait(15) # 묵시적 대기, 활성화를 최대 15초가지 기다린다.
    driver.get(login_url)

    while 1 : # 무한반복하며 5초마다 현재 url 인식
        current_url = driver.current_url
        if "?code=" in current_url : # 현재 url에 ?code=이 포함되있으면 break
            break
        time.sleep(5)
    
    driver.quit() # 창 닫음

    return render_template("Accept.html",client_id=client_id)

@app.route('/UpdateRefreshKey') # 두달에 한번 RefreshKey값 재발급
def RefreshUpdate():
    login_url = "https://kauth.kakao.com/oauth/authorize?client_id="+client_id+"&redirect_uri=https://example.com/oauth&response_type=code&scope=talk_message,friends"

    driver = webdriver.Chrome('../chromedriver.exe') #또는 chromedriver.exe
    driver.maximize_window() # 전체화면
    driver.implicitly_wait(15) # 묵시적 대기, 활성화를 최대 15초가지 기다린다.
    driver.get(login_url)

    while 1 : # 무한반복하며 5초마다 현재 url 인식
        current_url = driver.current_url
        if "?code=" in current_url : # 현재 url에 ?code=이 포함되있으면 break
            break
        time.sleep(5)
    driver.quit() # 창 닫음

    current_url = current_url.split('=') # authorization_code 추출
    authorization_code = current_url[1]

    Token_url = "https://kauth.kakao.com/oauth/token" # 액세스 토큰 + 리프레쉬토큰 URL
    data = {
        "grant_type" : "authorization_code",
        "client_id" : client_id,
        "redirect_url" : "https://localhost:3000",
        "code" : authorization_code
    }
    response = requests.post(Token_url, data=data)
    tokens = response.json()
    print(tokens)

    with open("kakao_code.json", "w") as fp: # 액세스토큰 + 리프레쉬토큰 등 json 저장
        json.dump(tokens, fp)

    return redirect("/")

@app.route('/UpdateAccessToken') # 12시간마다 Access토근 갱신
def ReAccessToken():
    with open("kakao_code.json", "r") as fp:
        ts = json.load(fp)
        access_token = ts["access_token"] # 유효기간 12시간 미만, 보안상 사용자를 인증하고 API호출 권한을 부여함
        refresh_token = ts["refresh_token"] # 유효기간 2달, 위의 토큰을 갱신하는 용도, 매번 정보 입력하거나 로그인하지 않고 위토큰을 발급받게 함
        
    url = "https://kauth.kakao.com/oauth/token"
    data = {
        "grant_type": "refresh_token",
        "client_id": client_id,
        "refresh_token": refresh_token
    }
    response = requests.post(url,data=data)
    tokens = response.json()

    with open("kakao_Access_code.json", "w") as fp: # 갱신된 Access 토근 저장
        json.dump(tokens, fp)

    return redirect("/")

@app.route('/listUpdate') # 친구 목록 리스트 새로고침
def RedirectList():
    with open("kakao_code.json", "r") as fp:
        ts = json.load(fp)
        access_token = ts["access_token"] # 유효기간 12시간 미만, 보안상 사용자를 인증하고 API호출 권한을 부여함
        refresh_token = ts["refresh_token"] # 유효기간 2달, 위의 토큰을 갱신하는 용도, 매번 정보 입력하거나 로그인하지 않고 위토큰을 발급받게 함

    friend_url = "https://kapi.kakao.com/v1/api/talk/friends" #친구 목록 가져오기
    header = {"Authorization": 'Bearer ' + access_token}
    result = json.loads(requests.get(friend_url, headers=header).text)

    friends_list = result.get("elements") # 친구 목록 list
    for friend in friends_list : #list for문 돌리면서 하나씩 저장
        friend_uuid = friend.get("uuid") # 유저 아이디 
        friend_name = friend.get("profile_nickname") # 유저 닉네임
        
        uuidCheck = kakaoUser.query.filter(kakaoUser.uuid == friend_uuid).first() # uuid 겹치는값 존재여부 확인

        if uuidCheck is None : # uuid가 존재하지 않을때 추가 
            inputfriend = kakaoUser(friend_name,access_token,refresh_token,friend_uuid)
            db.session.add(inputfriend)
            print(access_token)
            print('친구 추가')

    db.session.commit()
    return redirect("/")

@app.route("/SendMe",methods=['GET','POST']) # 나에게 메시지 전송
def Send_Me():
    msg_content=request.form['Content'] # Web에서 작성한 전송할 내용

    with open("kakao_Access_code.json","r") as fp:
        tokens = json.load(fp)
    headers={"Authorization" : "Bearer " + tokens["access_token"]}
    send_url= "https://kapi.kakao.com/v2/api/talk/memo/send" # 나에게 사용자정의 템플릿 보내기 URL

    data={
        "template_id" : 61896,
        'template_args' : '{"title":"'+msg_content+'"}'
    }

    response = requests.post(send_url, headers=headers, data=data)
    print(response.status_code)

    return redirect("/")

@app.route("/SendFriend",methods=['GET','POST']) #친구에게 메시지 전송
def Send_Friend():
    msg_user = request.form['SendUser'] # Web에서 선택한 전송할 대상
    msg_content=request.form['Content'] # Web에서 작성한 전송할 내용

    msg_send_user = kakaoUser.query.filter(kakaoUser.UserName == msg_user).first()

    with open("kakao_Access_code.json","r") as fp:
        tokens = json.load(fp)
    headers={"Authorization" : "Bearer " + tokens["access_token"]}
    send_url= "https://kapi.kakao.com/v1/api/talk/friends/message/send" #친구에게 사용자정의 템플릿 보내기 URL
    data={
        'receiver_uuids': '["{}"]'.format(msg_send_user.uuid),
        "template_id" : 61896,
        'template_args' : '{"title":"'+msg_content+'"}'
    }

    response = requests.post(send_url, headers=headers, data=data)
    print(response.status_code)

    return redirect("/")

@app.route("/click_friend",methods=['POST','GET']) # 클릭한 친구에게 메시지 전송
def clickmsg():
    clickFriend = request.form.getlist('result[]')
    for clickFriendList in clickFriend:
        with open("kakao_Access_code.json","r") as fp:
            tokens = json.load(fp)
        headers={"Authorization" : "Bearer " + tokens["access_token"]}
        url= "https://kapi.kakao.com/v1/api/talk/friends/message/send"

        kakao_template.kakao_msg_template(url,headers,clickFriendList)

    return 'ok'


if __name__=="__main__":
    app.run(debug=True)
    from .SingleModule import kakao_template