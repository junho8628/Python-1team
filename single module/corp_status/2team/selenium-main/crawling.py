# -*- coding: utf-8 -*-
from urllib.parse import DefragResult
from flask import Flask, render_template, request,redirect, url_for, flash,jsonify, send_file, session,escape
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_,text,update
from sqlalchemy import func
from sqlalchemy.sql.elements import Null
from datetime import datetime
import os, sys, re, random, string, pymysql, sqlalchemy, json, time, os
from itertools import groupby
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from urllib.request import urlretrieve
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

app = Flask(__name__)
app.secret_key = "Secret Key" #보안키 설정 (암호화)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///exam.db' # ///뒷 부분은 본인의 db파일 이름을 사용하면 됌. *현재 sqlite3 사용중 -> 추후 mariadb로 변경 예정
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
class tblErpTaxBillTrans(db.Model): #db 테이블 연결
    __tablename__="tblErpTaxBillTrans"
    TransSeq=db.Column(db.Integer,primary_key = True)
    FromSaupjaRegNo=db.Column(db.String(20))
    FromSaupjangNo=db.Column(db.String(10))
    FromSaupjaName=db.Column(db.String(30))
    FromDaepyoName=db.Column(db.String(30))
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
    def __init__(self,TransSeq,FromSaupjaRegNo,FromSaupjangNo,FromSaupjaName,FromDaepyoName,FromSaupjangAd,FromUptae,FromJongmok,FromEmailAddr1,ToSaupjaRegNo,ToSaupjangNo,ToSaupjaName,ToDaepyoName,ToSaupjangAddr,ToUptae,ToJongmok,ToEmailAddr1,ToEmailAddr2,HomeTaxApprNo,RegDate,AmtUnc,AmtTax,EditSayoo,AmtTot,AmtCash,AmtSupyo,AmtUEum,AmtMisu,GubunRequPay,FlowProcYN,SyncIndex,CorpCode):
        self.TransSeq=TransSeq
        self.FromSaupjaRegNo=FromSaupjaRegNo
        self.FromSaupjangNo=FromSaupjangNo
        self.FromSaupjaName=FromSaupjaName
        self.FromDaepyoName=FromDaepyoName
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

@app.route("/") #기본화면
def index():
    all_data = tblErpTaxBillTrans.query.order_by(tblErpTaxBillTrans.RegDate.desc()).all() #현재 DB에 들어있는 데이터를 날짜기준 내림차순으로 가져와서 넘겨줌
    return render_template("list.html",all_data=all_data)

@app.route("/crawling") # url창에 127.0.0.1/crawling으로 하면 selenium 실행되며 자동 크롤링 시작
def scrape():
    options=webdriver.ChromeOptions()
    # options.add_argument('headless') #headless 설정시 크롬창은 열리지 않지만 백그라운드로 실행
    options.add_argument("disable-gpu") #그래픽카드 가속 사용안함
    options.add_argument("user-data-dir=C:\\environments\\selenium") #selenium의 실행데이터 저장되는 위치 (여기에 공인인증서 브라우저 저장 데이터가 들어감)
    driver = webdriver.Chrome('C:/Users/user/OneDrive/바탕 화면/my/selenium/chromedriver.exe', options=options) #각자 (경로)/chromedriver.exe하면 됌
    driver.maximize_window() #전체화면으로 실행
    actions = webdriver.ActionChains(driver) # 마우스 클릭 이동 및 키보드 입력등을 체인으로 묶어주는 ActionChains
    driver.implicitly_wait(15) # 묵시적 대기, 활성화를 최대 15초가지 기다린다.
    hometex='https://www.hometax.go.kr/websquare/websquare.html?w2xPath=/ui/pp/index.xml' #URL
    driver.get(hometex)
    
    time.sleep(3)
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "textbox81212912"))) #메인화면 로그인 버튼
    element.click()

    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "txppIframe"))) #로그인화면 iframe
    driver.switch_to.frame(element) #iframe 스위치 (change)

    time.sleep(2)
    selecte_box=driver.find_element_by_xpath('//*[@id="anchor22"]') #로그인화면 로그인 버튼
    selecte_box.click()
    time.sleep(4)

    #로그인
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "dscert"))) #인증서 선택창 iframe 로딩 대기
    driver.switch_to.frame(element)
    selecte_box=driver.find_element_by_xpath('//*[@id="stg_web_kftc"]').click() #저장위치 브라우저 선택
    
    # 인증서 리스트 로딩 대기
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[9]/div[2]/div[2]/div[1]/div[6]/div/div[2]/div/div[4]/div[2]/div/table/tbody/tr/td"))) 
    #공인인증서 선택
    companyName='지오유' #회사이름
    if companyName=='지오유':
        findName='(주)지오유(zioyou)0004681103055148'
        inputPass='!@#ziou1570'
    elif companyName=='이가자연면':
        findName='(주)이가자연면_0001588512'
        inputPass='dlrkaus#357'

    driver.find_element_by_css_selector('[title^="'+str(findName)+'"]').click() #공인인증서 클릭

    selecte_box=driver.find_element_by_xpath('//*[@id="input_cert_pw"]').send_keys(inputPass) #비밀번호 입력
    selecte_box=driver.find_element_by_xpath('//*[@id="btn_confirm_iframe"]') #iframe 전환
    selecte_box.click()
    driver.switch_to.default_content() #현재 iframe 탈출

    try : #팝업창이 존재하면 팝업창 닫기
        element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "UTXPPABB29_iframe")))
        driver.switch_to.frame(element)
        driver.find_element_by_xpath('//*[@id="btnCloseInvtSpec"]').click() #팝업창 닫기버튼
        driver.switch_to.default_content()
    except: #없으면 패스
        pass

    time.sleep(2)

    # #조회클릭
    selecte_box = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="group1300"]'))) #조회/ 발급 
    selecte_box.click()
    time.sleep(1)
    element = driver.find_element_by_id("txppIframe") #조회/발급 iframe
    driver.switch_to.frame(element)

    selecte_box=driver.find_element_by_xpath('//*[@id="sub_a_0104020000"]') #목록조회 클릭
    selecte_box.click()
    time.sleep(1)
    selecte_box=driver.find_element_by_xpath('//*[@id="sub_a_0104020100"]') #발급 목록 조회 클릭
    selecte_box.click()
    driver.switch_to.default_content()

    # #인증서 종료후
    # driver.switch_to_window(driver.window_handles[0])
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'txppIframe')))
    driver.switch_to.frame(element)

    #3개월 클릭
    time.sleep(2)
    # selecte_box=driver.find_element_by_xpath('//*[@id="btnChk3"]')
    selecte_box = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="btnChk3"]')))
    selecte_box.click()
    #조회하기 클릭
    selecte_box=driver.find_element_by_xpath('//*[@id="group1744"]')
    selecte_box.click()
    time.sleep(3)

    all_table_list=driver.find_elements_by_xpath('/html/body/div[1]/div[4]/div[3]/div[5]/div/div[2]/div/table/tbody/tr') # 목록 테이블 데이터

    # 목록 리스트 수평 스크롤바 오른쪽으로 이동
    driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN) 
    datalist = driver.find_element_by_xpath('//*[@id="resultGrid_scrollX_right"]')
    driver.execute_script("arguments[0].scrollBy(1500,0)",datalist)

    time.sleep(2)
    number=driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[3]/div[7]/div/div/div[2]/p/span[7]') #페이지 (쪽) 수 가져오기
    divide=int(number.text)//10+2

    def reply():
        for i in range(3,13): # 3~12e
            time.sleep(2)
            try:
                liclick=driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[3]/div[7]/div/div/div[1]/ul/li['+str(i)+']') #(페이지 넘김)
                print(liclick.text)
                liclick.click()
            except:
                print('done')
                return 'ok'
            for index,value in enumerate(all_table_list, start=1): #테이블

                print(index)
                time.sleep(3)
                try:
                    element1=driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[3]/div[5]/div/div[2]/div/table/tbody/tr['+str(index)+']/td[25]/span/button') # 해당 리스트의 상세보기 버튼
                    element1.click()
                except:
                    print('doneli')
                    return
                time.sleep(3)
                element = driver.find_element_by_id("UTEETBDA38_iframe") # 상세조회 iframe 이동
                driver.switch_to.frame(element)

                HomeTaxApprNo=driver.find_element_by_xpath('//*[@id="etanInputboxId"]').get_attribute("value") #승인번호
                
                ApprNoData=tblErpTaxBillTrans.query.filter(tblErpTaxBillTrans.HomeTaxApprNo==HomeTaxApprNo).first() # 현재 승인번호와 일치하는게 있는지 확인
                print(HomeTaxApprNo,ApprNoData)

                coun=db.session.query(func.max(tblErpTaxBillTrans.TransSeq)).scalar() #거래 순번 최댓값
            
                #######
                # DB에 값이 존재하지 않으면서 새로운 데이터를 받을때 (첫 시도일때)

                if coun==None: # DB에 값이 존재하지 않는 상태
                    TransSeq=1

                #######
                # DB에 값이 존재하면서 새로운 값을 받을때 (새로운 날짜 업데이트시)

                elif coun is not None: # DB에 기존 값이 존재하는 상태
                    TransSeq=coun+1 
                    
                    if ApprNoData is None: #없으면 넘어가고 있다면 break로 탈출
                        print('pass')
                        pass
                    else:
                        print('break')
                        break

                ######

                FromSaupjaRegNo=driver.find_element_by_xpath('//*[@id="textbox1062"]').text
                FromSaupjangNo=driver.find_element_by_xpath('//*[@id="textbox1063"]').text
                FromSaupjaName=driver.find_element_by_xpath('//*[@id="textbox1065"]').text
                FromDaepyoName=driver.find_element_by_xpath('//*[@id="textbox1066"]').text
                FromSaupjangAd=driver.find_element_by_xpath('//*[@id="textbox1067"]').text
                FromUptae=driver.find_element_by_xpath('//*[@id="textbox1068"]').text
                FromJongmok=driver.find_element_by_xpath('//*[@id="textbox1069"]').text
                FromEmailAddr1=driver.find_element_by_xpath('//*[@id="textbox1070"]').text
                ToSaupjaRegNo=driver.find_element_by_xpath('//*[@id="textbox1071"]').text
                ToSaupjangNo=driver.find_element_by_xpath('//*[@id="textbox1128"]').text
                ToSaupjaName=driver.find_element_by_xpath('//*[@id="textbox1073"]').text
                ToDaepyoName=driver.find_element_by_xpath('//*[@id="textbox1074"]').text
                ToSaupjangAddr=driver.find_element_by_xpath('//*[@id="textbox1075"]').text
                ToUptae=driver.find_element_by_xpath('//*[@id="textbox1076"]').text
                ToJongmok=driver.find_element_by_xpath('//*[@id="textbox1077"]').text
                ToEmailAddr1=driver.find_element_by_xpath('//*[@id="textbox1078"]').text
                ToEmailAddr2=driver.find_element_by_xpath('//*[@id="textbox1079"]').text
                
                RegDate=driver.find_element_by_xpath('//*[@id="textbox1090"]').text
                AmtUnc=driver.find_element_by_xpath('//*[@id="textbox1091"]').text
                AmtTax=driver.find_element_by_xpath('//*[@id="textbox1092"]').text
                EditSayoo=driver.find_element_by_xpath('//*[@id="textbox1093"]').text
                AmtTot=driver.find_element_by_xpath('//*[@id="textbox1120"]').text
                AmtCash=driver.find_element_by_xpath('//*[@id="textbox1121"]').text
                AmtSupyo=driver.find_element_by_xpath('//*[@id="textbox1122"]').text
                AmtUEum=driver.find_element_by_xpath('//*[@id="textbox1123"]').text
                AmtMisu=driver.find_element_by_xpath('//*[@id="textbox1124"]').text
                GubunRequPay=driver.find_element_by_xpath('//*[@id="textbox1126"]').text
                FlowProcYN=None
                SyncIndex=None
                CorpCode=None
                print(HomeTaxApprNo)

                inputDb = tblErpTaxBillTrans(TransSeq,FromSaupjaRegNo,FromSaupjangNo,FromSaupjaName,FromDaepyoName,FromSaupjangAd,FromUptae,FromJongmok,FromEmailAddr1,ToSaupjaRegNo,ToSaupjangNo,ToSaupjaName,ToDaepyoName,ToSaupjangAddr,ToUptae,ToJongmok,ToEmailAddr1,ToEmailAddr2,HomeTaxApprNo,RegDate,AmtUnc,AmtTax,EditSayoo,AmtTot,AmtCash,AmtSupyo,AmtUEum,AmtMisu,GubunRequPay,FlowProcYN,SyncIndex,CorpCode) 
                db.session.add(inputDb)
                db.session.commit()
                print('데이터 추가 완료')

                selecte_box=driver.find_element_by_xpath('/html/body/div[1]/div[5]/a/input') #닫기버튼 
                selecte_box.click()
                driver.switch_to.default_content()
                element = driver.find_element_by_id("txppIframe")
                driver.switch_to.frame(element)
            
    for i in range(1,divide): # 페이지 넘김 번호 
        reply()
        time.sleep(2)
        try:
            leftbtn=driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[3]/div[7]/div/div/div[1]/ul/li[13]') # 다음 페이지로이동
            leftbtn.click()
        except:
            print('done!')
            break
    driver.quit()
    # return redirect(url_for('index'))
if __name__=="__main__":
    app.run(debug=True)