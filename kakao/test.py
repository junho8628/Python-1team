import requests

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = 'b8c277a56b50c2e119d4c0b969f10866'
redirect_uri = 'https://example.com/oauth'
authorize_code = 'Y53MG7MnMJTaoonIVhSlrjpJ0Lcynpy0dp5hWozOVv-0dCuDcmxJB7WXfJNxrnmlp2NnzgopcJ4AAAF7w6c3cQ'

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