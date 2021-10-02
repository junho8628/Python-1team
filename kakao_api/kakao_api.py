import requests
import json

#1.

with open("kakao_code.json","r") as fp:
    tokens = json.load(fp)


url="https://kapi.kakao.com/v2/api/talk/memo/default/send" # 문서 / 메시지 / REST API / 기본 템플릿으로 메시지 보내기/ sample 검색

# kapi.kakao.com/v2/api/talk/memo/default/send 

# Authorization: Bearer {ACCESS_TOKEN}
headers={
    "Authorization" : "Bearer " + tokens["access_token"]
}


data={
    "template_object": json.dumps({
        "object_type":"text",
        "text":"hello, kakao API",
        "link":{
            "web_url":"www.naver.com"
        }
    })
}

response = requests.post(url, headers=headers, data=data)
response.status_code
