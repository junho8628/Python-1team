import requests

url = 'https://kauth.kakao.com/oauth/token' #문서 / 카카오 로그인 / REST API / 토큰받기 / sample 검색
rest_api_key = '6ae276f9f771f2e43af49ff089efebe9' # 내 어플리캐이션 rest key
redirect_uri = 'https://example.com/oauth' # 내 어플리케이션 / 카카오 로그인 / Redirect URl

# code 받는법 client_id수정 : https://kauth.kakao.com/oauth/authorize?client_id={내 어플리케이션 restkey}&redirect_uri=https://example.com/oauth&response_type=code&scope=talk_message,friends
# 수정후 수정된 url로 검색할 시 위에 url 박스에 code= 뒤에 code값이 무작위로 생성 그거 복사한다음 아래있는 authorize_code에 붙여넣기

authorize_code = 'yDYx04IQD8z-HP8z7T4lVOKAXCjIWMi5hhZv4zypsp4oRRf-Vyz1i1hZ9iBfz-xT8swI8wopb7kAAAF7vv7zxw' # 문서 / 카카오 로그인 / REST API / 인가토큰 받기/Request 검색

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# json 저장
import json
with open("kakao_code.json","w") as fp:
    json.dump(tokens, fp)
