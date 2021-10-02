# 국세청 첫 로그인 세팅하기

selenium으로 자동 로그인을 진행하기 위해 첫 실행은 직접 해줘야합니다.    
따라서 로그인 과정을 알려드리도록 하겠습니다. 

### 1. selenium실행하여 chromedriver로 국세청까지 들어가기.
+ 해당 부분은 업로드 되있는 python 파일 실행하면 자동으로 진행될것입니다.
+ 안될경우 바로바로 질문해주시기 바랍니다.

### 2. 로그인 클릭하기 
![login1](https://user-images.githubusercontent.com/69878816/131447805-0f3520a7-9660-4d15-8856-e635e5d23280.png)
![login2](https://user-images.githubusercontent.com/69878816/131448178-51888311-ac56-4b1a-b547-1c6a2992ad95.png)
  
공인인증서는 브라우저에서 읽어오는 방식으로 사용합니다.
---
![login3](https://user-images.githubusercontent.com/69878816/131449178-79ce4c44-b6f9-40f5-bc77-72ea54d45d7a.png)


### 3.공인인증서 
공인인증서를 브라우저로 가져오는 작업을 하겠습니다. 
![login4](https://user-images.githubusercontent.com/69878816/131449308-df60a9f4-d35d-4d56-aed0-091d447623ee.png)  
![login5](https://user-images.githubusercontent.com/69878816/131449510-3ad1b2d1-9170-4057-8299-44db16967234.png)  
+ 이 이후 각자 공인인증서 파일(.p12)의 경로로 이동하여 선택후 인증서 비밀번호를 입력하고 확인을 누르시면 됩니다.
+ 브라우저에 인증서 저장은 체크해주도록 합니다.
+ 이후 보이는 화면은 확인을 눌러줍니다.  
![login6](https://user-images.githubusercontent.com/69878816/131449974-8ddafd3e-e17a-4eaa-93ea-e1cd26b150c6.png)  
+ 이후 나오는 연결하기는 하지 않고 닫기 또는 내리기를 눌러주면 로그인 세팅은 종료됩니다.
+ 이후 창을 닫고 selenium을 다시 실행하면 로그인도 진행이 될 것입니다.

