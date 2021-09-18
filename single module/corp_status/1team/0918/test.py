import requests

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = '8c2972daafdf239a443d7943c89253d9'
redirect_uri = 'https://example.com/oauth'
authorize_code = 'G3nGuuTmx3rSaoXdeb3dNv8CXYpUF4JFYndl0I-skucy4_eZ9sYFWujEgjqMW62Az1oGJgo9dJcAAAF790vkAQ'

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

# import json

# with open("D:\python\kakao\kakao_code.json","r") as fp:
#     ts = json.load(fp)
# print(ts)
# print(ts["access_token"])