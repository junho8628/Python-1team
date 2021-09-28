# -*- coding: utf-8 -*-
from urllib.parse import DefragResult
from flask import Flask, render_template, request,redirect, url_for, flash,jsonify, send_file, session,escape
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_,text,update
import json
from datetime import datetime
from sqlalchemy import func
from sqlalchemy.sql.elements import Null
from werkzeug.utils import secure_filename
import os, sys, re, pyautogui
import random, string
import pymysql
import sqlalchemy 
import numpy as np
from itertools import groupby


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
from urllib.request import urlretrieve

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# app = Flask(__name__)
# app.secret_key = "Secret Keyf"
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Exsigk*sk12*32@docs2.zioyou.com:20000/Erp_Credit?charset=utf8"
# # 이곳에서 db 연결
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ErpTax.db'
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# orm db 선언문
# db = SQLAlchemy(app)
# class tblErpCreditCardTrans(db.Model):
#     __tablename__="tblErpCreditCardTrans"
#     TransSeq=db.Column(db.Integer,primary_key = True)
#     CreditCardNo=db.Column(db.String(16))
#     ProcGubun=db.Column(db.String(1))
#     TransDate=db.Column(db.DateTime(timezone=True))
#     InstType=db.Column(db.String(1))
#     MccCode=db.Column(db.String(4))
#     MccName=db.Column(db.String(50))
#     TaxType=db.Column(db.String(20))
#     Amt=db.Column(db.DecimalField(max_digits=17, decimal_places=2))
#     Unc=db.Column(db.DecimalField(max_digits=17, decimal_places=2))
#     Tax=db.Column(db.DecimalField(max_digits=17, decimal_places=2))
#     CurrCode=db.Column(db.String(3))
#     MerchNo=db.Column(db.String(15))
#     MerchBizno=db.Column(db.String(10))
#     MerchName=db.Column(db.String(50))
#     MerchMaster=db.Column(db.String(50))
#     MerchTel=db.Column(db.String(14))
#     MerchZipCode=db.Column(db.String(6))
#     MerchAddr1=db.Column(db.String(100))
#     MerchAddr2=db.Column(db.String(100))
#     ApprNo=db.Column(db.String(100))
#     UseAccCode=db.Column(db.Integer)
#     UseTitle=db.Column(db.String(40))
#     ImgBillUrl=db.Column(db.String(200))
#     FlowProcYN=db.Column(db.String(1))
#     SyncIndex=db.Column(db.String(20))
#     SeqAcquire=db.Column(db.Integer)
#     ApprDate=db.Column(db.DateTime(timezone=True))
#     OrgnCollNo=db.Column(db.String(32))
#     ErpProjectCode=db.Column(db.String(32))
#     def __init__(self,TransSeq,CreditCardNo,ProcGubun,TransDate,InstType,MccCode,MccName,TaxType,Amt,Unc,Tax,CurrCode,MerchNo,MerchBizno,MerchName,MerchMaster,MerchTel,MerchZipCode,MerchAddr1,MerchAddr2,ApprNo,UseAccCode,UseTitle,ImgBillUrl,FlowProcYN,SyncIndex,SeqAcquire,ApprDate,OrgnCollNo,ErpProjectCode):
#         self.TransSeq=TransSeq
#         self.CreditCardNo=CreditCardNo
#         self.ProcGubun=ProcGubun
#         self.TransDate=TransDate
#         self.InstType=InstType
#         self.MccCode=MccCode
#         self.MccName=MccName
#         self.TaxType=TaxType
#         self.Amt=Amt
#         self.Unc=Unc
#         self.Tax=Tax
#         self.CurrCode=CurrCode
#         self.MerchNo=MerchNo
#         self.MerchBizno=MerchBizno
#         self.MerchName=MerchName
#         self.MerchMaster=MerchMaster
#         self.MerchTel=MerchTel
#         self.MerchZipCode=MerchZipCode
#         self.MerchAddr1=MerchAddr1
#         self.MerchAddr2=MerchAddr2
#         self.ApprNo=ApprNo
#         self.UseAccCode=UseAccCode
#         self.UseTitle=UseTitle
#         self.ImgBillUrl=ImgBillUrl
#         self.FlowProcYN=FlowProcYN
#         self.SyncIndex=SyncIndex
#         self.SeqAcquire=SeqAcquire
#         self.ApprDate=ApprDate
#         self.OrgnCollNo=OrgnCollNo
#         self.ErpProjectCode=ErpProjectCode


# options.add_argument('headless')
# options.add_argument("disable-gpu")
# options.add_argument("user-data-dir=C:\\environments\\selenium")
options=webdriver.ChromeOptions()
options.add_argument('window-size=1920x1080') 

driver = webdriver.Chrome('chromedriver.exe', options=options) #또는 chromedriver.exe
driver.maximize_window()
actions = webdriver.ActionChains(driver)
driver.implicitly_wait(15) # 묵시적 대기, 활성화를 최대 15초가지 기다린다.

kbid='zioyou1011'
kbpass='@#ziou0523'

Shinhan='https://biz.kbcard.com/CXORMPIC0001.cms'
driver.get(Shinhan)
time.sleep(3)

#기업 클릭
selecte_box = WebDriverWait(driver, 10).until(
EC.visibility_of_element_located((By.XPATH, '//*[@id="loginGubun02"]')))
selecte_box.click()

# 아이디 클릭
time.sleep(1)
driver.find_element_by_xpath('//*[@id="기업인터넷서비스로그인ID"]').click()
time.sleep(3)
pyautogui.press(['z','i','o','y','o','u','1','0','1','1'],interval=1)
# pyautogui.write('zioyou1011')
# pyautogui.hotkey('z','i','o','y','o','u','1','0','1','1')
# driver.find_element_by_xpath('//*[@id="기업인터넷서비스로그인ID"]')
# driver.find_element_by_name('기업인터넷서비스로그인ID').send_keys(kbid)

# 비밀번호 클릭 (버튼이 한번 더 생겨 두번 눌러줘야함)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="vBizkeypwd"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="vBizkeypwd"]').click()

time.sleep(1)
# driver.find_element_by_xpath('/html/body/div[5]/ul[1]/li[1]').click()
# driver.find_element_by_class_name('sp.kp11').click()



# driver.find_element_by_xpath('//*[@id="doBizIdLogin"]').click()


keypad1 = [
    ["`","1","2","3","4","5","6","7","8","9","0","-","=","backsapce"],
    ["재배열","q","w","e","r","t","y","u","i","o","p","[","]","/"],
    ["caps lock","a","s","d","f","g","h","j","k","l",";","'","입력완료"],
    ["shift","z","x","c","v","b","n","m",",",".","/","닫기"]]

keypad2 = [
    ['~','!','@','#','$','%','^','&','*','(',')','_','+','backsapce'],
    ['재배열','Q','W','E','R','T','Y','U','I','O','P','{','}','|'],
    ['CapsLock','A','S','D','F','G','H','J','K','L',':','"','입력완료'],
    ['Shift','Z','X','C','V','B','N','M','<','>','?','닫기']
    ]
keypad1_virtual=[]
keypad2_virtual=[]

def keypad(num,select_virtual):
    all_list=driver.find_elements_by_xpath('/html/body/div[5]/ul['+num+']/li') # 가상 키보드 전체
    keypad_class=[] # 가상 키보드 클래스 담아놓을 리스트
    for index,value in enumerate(all_list, start=1):
        element1=driver.find_element_by_xpath('/html/body/div[5]/ul['+num+']/li['+str(index)+']').get_attribute('class')
        keypad_class.append(element1.replace(" ", "."))
    for i in range(5):
        keypad_class.remove('logo')

    keypad_class.remove('bar')
    select_virtual.append(keypad_class[0:14])
    select_virtual.append(keypad_class[14:28])
    select_virtual.append(keypad_class[28:41])
    select_virtual.append(keypad_class[41:53])

keypad('1',keypad1_virtual)
keypad('2',keypad2_virtual)
print(keypad1_virtual)
print(keypad2_virtual)

a = np.array(keypad1_virtual, np.string_)
b = np.array(keypad1 , np.string_)
print (a)
print (b)
aindex = np.where(b == 'z')
print(aindex)


# driver.find_element_by_class_name(keypad1_virtual[3][0]).click() # shift
# time.sleep(0.5)
# driver.find_element_by_class_name(keypad2_virtual[0][2]).click() # @
# time.sleep(0.5)
# driver.find_element_by_class_name(keypad1_virtual[3][0]).click()# shift
# time.sleep(0.5)
# driver.find_element_by_class_name(keypad2_virtual[0][3]).click()# #
# time.sleep(0.5)
# driver.find_element_by_class_name(keypad1_virtual[3][1]).click()# z
# time.sleep(0.5)
# driver.find_element_by_class_name(keypad1_virtual[1][8]).click()# i
# time.sleep(0.5)
# driver.find_element_by_class_name(keypad1_virtual[1][9]).click()# o
# time.sleep(0.5)
# driver.find_element_by_class_name(keypad1_virtual[1][7]).click()# u
# time.sleep(0.5)
# driver.find_element_by_class_name(keypad1_virtual[0][10]).click()# 0
# time.sleep(0.5)
# driver.find_element_by_class_name(keypad1_virtual[0][5]).click()# 5
# time.sleep(0.5)
# driver.find_element_by_class_name(keypad1_virtual[0][2]).click()# 2
# time.sleep(0.5)
# driver.find_element_by_class_name(keypad1_virtual[0][3]).click()# 3
# time.sleep(0.5)
# driver.find_element_by_class_name(keypad1_virtual[2][12]).click()# 완료
# time.sleep(0.5)
