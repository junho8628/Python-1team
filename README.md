# 파이썬 경진대회 1팀
> 파이썬 경진대회 1팀입니다. 모르는게 있으면 질문하도록 합시다


python selenium을 잘 다루도록 노력합니다

## pip 설치

```sh
pip install selenium
```
## sqlite3 설치 url

https://www.sqlite.org/download.html


## sqlite3 db 생성

```sh
./sqlite3 [DB이름]
```

## sqlite3 table 생성

```sh
# db 접속
./sqlite3 [DB이름].db

# db 접속 후 create
create table tblErpTaxBillTrans (
   TransSeq int primary key,
   FromSaupjaRegNo text,
   FromSaupjangNo text,
   FromSaupjaname text,
   FromDaepyoName text,
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

init.py파일의 180번째 줄에 크롬 드라이버 위치 수정

만약 db에 데이터가 잘 들어갔는지 확인하고 싶을때 init.py 163번줄부터 169번줄 까지 주석풀고 165번쨰줄에 table이름 변경 

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

