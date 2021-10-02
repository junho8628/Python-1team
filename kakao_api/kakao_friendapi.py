import requests
import json

with open("kakao_code.json","r") as fp:
    tokens = json.load(fp)
# print(tokens)
# print(tokens["access_token"])

friend_url = "https://kapi.kakao.com/v1/api/talk/friends"

# GET /v1/api/talk/friends HTTP/1.1
# Host: kapi.kakao.com
# Authorization: Bearer {ACCESS_TOKEN}

headers={"Authorization" : "Bearer " + tokens["access_token"]}

result = json.loads(requests.get(friend_url, headers=headers).text)

print(type(result))
print("=============================================")
print(result)
print("=============================================")
friends_list = result.get("elements")
print(friends_list)
# print(type(friends_list))
print("=============================================")
print(friends_list[0].get("uuid"))
friend_id = friends_list[0].get("uuid")
print(friend_id)

send_url= "https://kapi.kakao.com/v1/api/talk/friends/message/default/send"

data={
    'receiver_uuids': '["{}"]'.format(friend_id),
    "template_object": json.dumps({
        "object_type":"text",
        "text":"방금 신용카드가 결재되었습니다",
        "link":{
            "web_url":"www.daum.net",
            "web_url":"www.naver.com"
        },
        "button_title": "바로 확인"
    })
}

response = requests.post(send_url, headers=headers, data=data)
response.status_code

send_url1= "https://kapi.kakao.com/v1/api/talk/friends/message/send"
data={
    "template_id" : 60954,
    "receiver_uuids": '["{}"]'.format(friend_id),
     'template_args' : '{"title":"가맹점 정보","describe":"설명"}'
    }

response = requests.post(send_url1, headers=headers, data=data)
response.status_code

data={
    'receiver_uuids': '["{}"]'.format(friend_id),
    "template_object": json.dumps({
        "object_type":"text",
        "text":"가맹점은 정상영업상태이며 용인시 처인구 동백지구에 위치해있습니다. 비과세 가맹접이고,(아이디어)입니다",
        "link":{
            "web_url":"www.daum.net",
            "web_url":"www.naver.com"
        },
        "button_title": "바로 확인"
    })
}

response = requests.post(send_url, headers=headers, data=data)
response.status_code

data={
    'receiver_uuids': '["{}"]'.format(friend_id),
    "template_object": json.dumps({
        "object_type":"text",
        "text":"자동으로 분류된 계정과목은 '접대비' 이며 과거, 3일전 10000원이 결재된 이력이 존재 합니다. 사용용도를 입력해주세요",
        "link":{
            "web_url":"www.daum.net",
            "web_url":"www.naver.com"
        },
        "button_title": "바로 확인"
    })
}

response = requests.post(send_url, headers=headers, data=data)
response.status_code
