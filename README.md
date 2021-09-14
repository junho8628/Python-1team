# 파이썬 경진대회 1팀
> 파이썬 경진대회 1팀입니다. 모르는게 있으면 질문하도록 합시다


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
```

## 정보
init.py파일의 33번쨰 줄에 자신이 만든 db이름으로 변경

init.py파일의 150번째 줄에 크롬 드라이버 위치 수정

만약 db에 데이터가 잘 들어갔는지 확인하고 싶을때 init.py 163번줄부터 169번줄 까지 주석풀고 165번쨰줄에 table이름 변경 

## 인증서 등록 방법

![image](https://user-images.githubusercontent.com/51261484/131441018-0e30ed41-3044-4df2-9adf-6d46b2d7b6b3.png)

1. 브라우저 클릭
2. 브라우저로 공동인증서 가져오기 클릭

![image](https://user-images.githubusercontent.com/51261484/131442306-38669fc9-2e65-42ca-ac41-12b7a139a2d4.png)

3. 인증서파일 경로 오른쪽 끝에있는 파일모양 클릭 

![image](https://user-images.githubusercontent.com/51261484/131441913-5cd96570-4963-4e65-9bab-c2023638248a.png)

4. 자기가 인증서 저장해둔 곳으로 이동후 경로지정

![image](https://user-images.githubusercontent.com/51261484/131442061-0f16e652-2dfd-4363-b065-fadbfc6e5c44.png)

5. 인증서 비밀번호 작성(비밀번호: !@#ziou1570 )
6. 브라우저에 인증서 저장에 체크되있는지 확인
7. 확인버튼 클릭

**로그인 되는지 확인하고 로그인이 되는것을 확인했다면 창 닫고 다시 시작**

## 카카오 메세지

https://novice-engineers.tistory.com/9?category=908185

## 카카오 쳇봇
https://luckygg.tistory.com/294


## 개발기간

* 2021/07/27
    * table 생성 및 개발 시작
* 2021/07/29
    * 브라우저에 인증서 가져오기
    * 여러 회사일 경우 이름만 바꾸면 패스워드와 인증서가 자동으로 바뀌게 설정
* 2021/08/02
    * 더블클릭 오류로 데이터를 볼수있는 방법 탐색
    * 상세보기 클릭으로 데이터를 가져오는 방법 채택
* 2021/08/03
    * db에 데이터 축적 시작
    * 승인번호가 안가져와지는 에러 발생
* 2021/08/04
    * 승인번호 안가져와지는 에러 해결
    * 에러 해결후 중복이 언되도록 승인번호를 기준으로 중복값 판단
* 2021/08/05
    * 접속하는 시간이 너무 길어 Explicit Waits 방식 채택
    * 로딩이 끝날때 바로 실행 할수 있도록 설정
* 2021/08/06
    * 가끔씩 로딩을 2번하는 경우가 있어 Explicit Waits가 에러를 발생
    * 몇몇 구간은 sleep으로 처리
* 2021/08/23
    * 소장님께 완료 보고

