# KB국민은행 S/W 경진대회 : 무증빙 A.I
> KB국민은행 S/W 경진대회 피어나(Bloom) 팀입니다. 모르는게 있으면 질문하도록 합시다


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
카카오 톡이 보내지지 않을경우 Access_Token을 갱신해주시기 바랍니다. (유효기간 12시간)   
Access_Token이 갱신되지 않을경우 refresh_Token을 갱신해주시기 바랍니다. (유효기간 2달)

------------------
![image](https://user-images.githubusercontent.com/69878816/135555357-9664b575-812d-4081-92cb-87bf0978a437.png)
+ 사용자(결재자,이용자)가 메시지 전송을 동의할때 보낼 url 입니다. 해당 동의를 해야 kakao api로 메시지 전송이 가능합니다.  

![image](https://user-images.githubusercontent.com/69878816/135556704-14ef392e-19b9-4f55-a353-8383a1d49153.png)
+ 사용자 리스트의 체크박스에 선택된 사람에게 결재 메시지를 수동으로 전송할 수 있습니다.

![image](https://user-images.githubusercontent.com/69878816/135556827-4d9ef0a5-15c6-47cb-9e78-a0343e584832.png)
+ 사용자 리스트를 다시 로딩합니다. (새로고침)

![image](https://user-images.githubusercontent.com/69878816/135575870-1ca8f7ec-1d58-43bb-8f17-3ba4d2d6d1c9.png)
+ Refresh Token을 재발급 합니다. (유효기간이 두달이므로 주기적으로 해야합니다.)

![image](https://user-images.githubusercontent.com/69878816/135699959-2035d6a7-1e4a-4a59-9481-56f053a67f3e.png)
+ Access Token을 재발급 합니다. (유효기간이 12시간이므로 하루에 적어도 한번은 재발급이 필요합니다.)
## 카카오 메세지

https://novice-engineers.tistory.com/9?category=908185

## 카카오 봇
https://luckygg.tistory.com/294

## 결과화면 예제
![image](https://user-images.githubusercontent.com/51261484/135700432-37614279-4031-4957-a864-0f5fdc95d9db.png)

![image](https://user-images.githubusercontent.com/51261484/135700458-f016825b-a56e-4bcf-86a7-0a587545e586.png)

![image](https://user-images.githubusercontent.com/51261484/135700486-2877326a-ae0f-438a-9eeb-be2da1301431.png)

## 결과화면
![image](https://user-images.githubusercontent.com/69878816/135700258-afa28ae4-d720-4332-8256-2122fbf52b06.png)
