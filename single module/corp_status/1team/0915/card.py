# -*- coding: utf-8 -*-
from urllib.parse import DefragResult
from flask import Flask, render_template, request,redirect, url_for, flash,jsonify, send_file, session,escape
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_,text,update
import json
from datetime import datetime
from sqlalchemy import func
from sqlalchemy.sql.elements import RANGE_CURRENT, Null
from werkzeug.utils import secure_filename
import os, sys, re
import random, string
import pymysql
import sqlalchemy 
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

app = Flask(__name__)
app.secret_key = "Secret Keyf"
# 이곳에서 sqlite3 연결
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# orm db 선언문1
db = SQLAlchemy(app)
class HomeTaxData(db.Model):
    __tablename__="HomeTaxData"
    BusinessNumber = db.Column(db.Integer, primary_key=True)
    BusinessState = db.Column(db.String(100))
    def __init__(self , BusinessNumber , BusinessState):
        self.BusinessNumber = BusinessNumber
        self.BusinessState = BusinessState

@app.route("/")
def index():
    all_data=HomeTaxData.query.all()
    return render_template("list.html",all_data=all_data)
  
if __name__=="__main__":
    app.run(debug=True)

options=webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument('window-size=1920x1080') 
options.add_argument("disable-gpu")
options.add_argument("user-data-dir=C:\\environments\\selenium")
# chrome 드라이버 chrome 버전에 맞게 다운후 위치변경
driver = webdriver.Chrome('chromedriver.exe', options=options) #또는 chromedriver.exe
driver.maximize_window()
actions = webdriver.ActionChains(driver)
driver.implicitly_wait(15) # 묵시적 대기, 활성화를 최대 15초가지 기다린다.

hometex='https://www.hometax.go.kr/websquare/websquare.wq?w2xPath=/ui/pp/index.xml&tmIdx=0&tm2lIdx=&tm3lIdx='
driver.get(hometex)

time.sleep(3)

data = driver.find_element_by_xpath('//*[@id="textbox81212923"]')
data.click()

driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)

element = WebDriverWait(driver, 10).until(
EC.visibility_of_element_located((By.ID, "txppIframe")))
driver.switch_to.frame(element)

find = driver.find_element_by_xpath('//*[@id="sub_a_0108010000"]')
find.click()

time.sleep(3)

inputData = driver.find_element_by_xpath('//*[@id="bsno"]').send_keys('142-81-36612')

dataClick = driver.find_element_by_xpath('//*[@id="trigger5"]')
dataClick.click()

time.sleep(2)

number = driver.find_element_by_xpath('//*[@id="grid2_cell_0_0"]/span').text
print(number)
state = driver.find_element_by_xpath('//*[@id="grid2_cell_0_1"]/span').text
print(state)

inputDB = HomeTaxData(number,state)
db.session.add(inputDB)
db.session.commit()