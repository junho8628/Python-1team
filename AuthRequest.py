# -*- coding: utf-8 -*-
from urllib.parse import DefragResult
from flask import Flask, render_template, request,redirect, url_for, flash,jsonify, send_file, session,escape
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_,text,update
from sqlalchemy.sql.elements import Null
import os, sys, re, time, random, string, pymysql, sqlalchemy, json, requests
# from requests.api import request
from selenium import webdriver

from SingleModule import kakao_template # 카카오 템플릿 메시지 전송 python
from SingleModule import hometax as HT # 홈텍스 크롤링 python

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
    Token = db.Column(db.String(200))
    RefreshToken = db.Column(db.String(200))
    uuid = db.Column(db.String(200),primary_key=True)
    def __init__(self, UserName, Token, RefreshToken, uuid) :
        self.UserName = UserName
        self.Token = Token
        self.RefreshToken = RefreshToken
        self.uuid = uuid

class tblErpTaxBillTrans(db.Model):
    __tablename__="tblErpTaxBillTrans"
    TransSeq=db.Column(db.Integer,primary_key = True)
    FromSaupjaRegN=db.Column(db.String(20))
    FromSaupjangNo=db.Column(db.String(10))
    FromSaupjaName=db.Column(db.String(30))
    FromDaepyoNam=db.Column(db.String(30))
    FromSaupjangAd=db.Column(db.String(100))
    FromUptae=db.Column(db.String(30))
    FromJongmok=db.Column(db.String(30))
    FromEmailAddr1=db.Column(db.String(100))
    ToSaupjaRegNo=db.Column(db.String(20))
    ToSaupjangNo=db.Column(db.String(10))
    ToSaupjaName=db.Column(db.String(30))
    ToDaepyoName=db.Column(db.String(30))
    ToSaupjangAddr=db.Column(db.String(100))
    ToUptae=db.Column(db.String(30))
    ToJongmok=db.Column(db.String(30))
    ToEmailAddr1=db.Column(db.String(100))
    ToEmailAddr2=db.Column(db.String(100))
    HomeTaxApprNo=db.Column(db.String(40))
    RegDate=db.Column(db.String(10))
    AmtUnc=db.Column(db.String(13))
    AmtTax=db.Column(db.String(13))
    EditSayoo=db.Column(db.String(40))
    AmtTot=db.Column(db.String(13))
    AmtCash=db.Column(db.String(13))
    AmtSupyo=db.Column(db.String(13))
    AmtUEum=db.Column(db.String(13))
    AmtMisu=db.Column(db.String(13))
    GubunRequPay=db.Column(db.String(4))
    FlowProcYN=db.Column(db.String(1))
    SyncIndex=db.Column(db.String(20))
    CorpCode=db.Column(db.String(6))
    def __init__(self,TransSeq,FromSaupjaRegN,FromSaupjangNo,FromSaupjaName,FromDaepyoNam,FromSaupjangAd,FromUptae,FromJongmok,FromEmailAddr1,ToSaupjaRegNo,ToSaupjangNo,ToSaupjaName,ToDaepyoName,ToSaupjangAddr,ToUptae,ToJongmok,ToEmailAddr1,ToEmailAddr2,HomeTaxApprNo,RegDate,AmtUnc,AmtTax,EditSayoo,AmtTot,AmtCash,AmtSupyo,AmtUEum,AmtMisu,GubunRequPay,FlowProcYN,SyncIndex,CorpCode):
        self.TransSeq=TransSeq
        self.FromSaupjaRegN=FromSaupjaRegN
        self.FromSaupjangNo=FromSaupjangNo
        self.FromSaupjaName=FromSaupjaName
        self.FromDaepyoNam=FromDaepyoNam
        self.FromSaupjangAd=FromSaupjangAd
        self.FromUptae=FromUptae
        self.FromJongmok=FromJongmok
        self.FromEmailAddr1=FromEmailAddr1
        self.ToSaupjaRegNo=ToSaupjaRegNo
        self.ToSaupjangNo=ToSaupjangNo
        self.ToSaupjaName=ToSaupjaName
        self.ToDaepyoName=ToDaepyoName
        self.ToSaupjangAddr=ToSaupjangAddr
        self.ToUptae=ToUptae
        self.ToJongmok=ToJongmok
        self.ToEmailAddr1=ToEmailAddr1
        self.ToEmailAddr2=ToEmailAddr2
        self.HomeTaxApprNo=HomeTaxApprNo
        self.RegDate=RegDate
        self.AmtUnc=AmtUnc
        self.AmtTax=AmtTax
        self.EditSayoo=EditSayoo
        self.AmtTot=AmtTot
        self.AmtCash=AmtCash
        self.AmtSupyo=AmtSupyo
        self.AmtUEum=AmtUEum
        self.AmtMisu=AmtMisu
        self.GubunRequPay=GubunRequPay
        self.FlowProcYN=FlowProcYN
        self.SyncIndex=SyncIndex
        self.CorpCode=CorpCode

class tblErpTaxBillTransitem(db.Model):
    __tablename__="tblErpTaxBillTransitem"
    TransSeq=db.Column(db.Integer,primary_key = True)
    ItemNo=db.Column(db.Integer)
    Mm=db.Column(db.String(2))
    Dd=db.Column(db.String(2))
    Pummok=db.Column(db.String(200))
    Spec=db.Column(db.String(20))
    Cnt=db.Column(db.String(50))
    Unc=db.Column(db.String(50))
    Amt=db.Column(db.String(50))
    Tax=db.Column(db.String(50))
    Bogo=db.Column(db.String(200))
    def __init__(self,TransSeq,ItemNo,Mm,Dd,Pummok,Spec,Cnt,Unc,Amt,Tax,Bogo):
        self.TransSeq=TransSeq
        self.ItemNo=ItemNo
        self.Mm=Mm
        self.Dd=Dd
        self.Pummok=Pummok
        self.Spec=Spec
        self.Cnt=Cnt
        self.Unc=Unc
        self.Amt=Amt
        self.Tax=Tax
        self.Bogo=Bogo
        
@app.route("/") #기본화면
def index():
    all_data = kakaoUser.query.all()
    return render_template("list.html",all_data=all_data)

@app.route("/KakaoAccept") #카카오 메세지 동의 버튼 클릭
def Accept():
    return render_template("Accept.html",client_id=client_id)

@app.route('/oauth',methods=['GET','POST'])
def getAccept():
    parameter = request.args.get('code') #authorization_code
    print(parameter)


    Token_url = "https://kauth.kakao.com/oauth/token" # 액세스 토큰 + 리프레쉬토큰 URL
    data = {
        "grant_type" : "authorization_code",
        "client_id" : client_id,
        "redirect_url" : "https://localhost:3000",
        "code" : parameter
    }
    response = requests.post(Token_url, data=data)
    tokens = response.json()
    print(tokens)

    with open("kakao_code.json", "w") as fp: # 액세스토큰 + 리프레쉬토큰 등 json 저장
        json.dump(tokens, fp)
    return redirect("/")

@app.route('/UpdateRefreshKey') # 두달에 한번 RefreshKey값 재발급
def RefreshUpdate():
    return redirect("https://kauth.kakao.com/oauth/authorize?client_id="+client_id+"&redirect_uri=https://example.com/oauth&response_type=code&scope=talk_message,friends")

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



#------------------------------
# 아직 개발중
@app.route("/hometaxCrawling") #홈택스 크롤링
def hometax():
    try :
        HT.homtax_crawling()
    except:
        pass
    return redirect("/")
#------------------------------

if __name__=="__main__":
    app.run(port=3000,debug=True)