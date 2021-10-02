import requests

url = 'https://kauth.kakao.com/oauth/token' #문서 / 카카오 로그인 / REST API / 토큰받기 / sample 검색
rest_api_key = '2cfcef6a59cfb96e207837bb99b11005' # 내 어플리캐이션 rest key
redirect_uri = 'https://example.com/oauth' # 내 어플리케이션 / 카카오 로그인 / Redirect URl

# code 받는법 client_id수정 : https://kauth.kakao.com/oauth/authorize?client_id={내 어플리케이션 restkey}&redirect_uri=https://example.com/oauth&response_type=code
# 수정후 수정된 url로 검색할 시 위에 url 박스에 code= 뒤에 code값이 무작위로 생성 그거 복사한다음 아래있는 authorize_code에 붙여넣기
authorize_code = 'ytkr7G2h4899ihYBPUo-dvsDbTn_o_YhwRDaLnRkv3lM4kEFivk1KgomVuBHlJdlEV1TTAo9dZoAAAF73J-J3w' # 문서 / 카카오 로그인 / REST API / 인가토큰 받기/Request 검색


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
#1.
# with open(r"E:\othertest\selenium_use\kakao_code.json","w") as fp:
#     json.dump(tokens, fp)

with open("kakao_code.json","w") as fp:
    json.dump(tokens, fp)
# import json
# #1.
# with open(r"E:\othertest\selenium_use\kakao_code.json","r") as fp:
#     ts = json.load(fp)
# print(ts)
# print(ts["access_token"])

