# 파이썬 경진대회 피어나(bloom)
> 파이썬 경진대회 피어나(bloom) 팀입니다. 모르는게 있으면 질문하도록 합시다


python selenium을 잘 다루도록 노력합니다

## pip 설치

```sh
pip install selenium
pip install Flask
pip install PyMySQL
pip install SQLAlchemy
pip install Flask-SQLAlchemy
```
## sqlite3 설치 방법

1. https://www.sqlite.org/download.html 접속
2. Precompiled Binaries for Windows 의 3번째 항목 다운
3. 압축 해제 후 sqlite3.exe 복사
4. 복사한 프로그램을 자신이 사용할 폴더 안에 삽입

## chrome driver 다운

1. 크롬 오른쪽 세로 점점점 클릭
2. 도움말 클릭
3. chrome 정보 클릭
4. 버전확인
5. https://chromedriver.chromium.org/downloads 접속
6. 버전에 맞는 드라이버 클릭
7. window 32다운
8. 압축 풀고 안에있는 응용프로그램 복사 후 자신이 쓰고있는 폴더에 붙여 넣기

## sqlite3 db 생성 및 테이블 생성

```sh
# db 생성
./sqlite3 [DB이름].db

# db 생성 후 create
# 홈택스 DB 1
create table tblErpTaxBillTrans (
   TransSeq int primary key,
   FromSaupjaRegN text,
   FromSaupjangNo text,
   FromSaupjaName text,
   FromDaepyoNam text,
   FromSaupjangAd text,
   FromUptae text text,
   FromJongmok text,
   FromEmailAddr1 text,
   ToSaupjaRegNo text,
   ToSaupjangNo text,
   ToSaupjaName text,
   ToDaepyoName text,
   ToSaupjangAddr text,
   ToUptae text,
   ToJongmok text,
   ToEmailAddr1 text,
   ToEmailAddr2 text,
   HomeTaxApprNo text,
   RegDate text,
   AmtUnc text,
   AmtTax text,
   EditSayoo text,
   AmtTot text,
   AmtCash text,
   AmtSupyo text,
   AmtUEum text,
   AmtMisu text,
   GubunRequPay text,
   FlowProcYN text,
   SyncIndex text,
   CorpCode text);
   
# 홈택스 DB 2번
create table tblErpTaxBillTransitem (
    TransSeq int primary key,
    ItemNo int,
    Mm text,
    Dd text,
    Pummok text,
    Spec text,
    Cnt text,
    Unc text,
    Amt text,
    Tax text,
    Bogo text);
    
# kakaoDB
CREATE TABLE kakaoUser (
    UserName text,
    Token text, 
    RefreshToken text, 
    uuid text primary key);
```

## 정보


## 카카오 메세지

https://novice-engineers.tistory.com/9?category=908185

## 카카오 쳇봇
https://luckygg.tistory.com/294


## 개발기간

