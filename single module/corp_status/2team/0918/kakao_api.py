import requests
import json

#1.

with open("kakao_code.json","r") as fp:
    tokens = json.load(fp)


send_url1= "https://kapi.kakao.com//v2/api/talk/memo/send"
# kapi.kakao.com/v2/api/talk/memo/default/send 

# Authorization: Bearer {ACCESS_TOKEN}
headers={
    "Authorization" : "Bearer " + tokens["access_token"]
}



data={
    "template_id" : 61896,
    # "receiver_uuids": '["{}"]'.format(friend_id),
     'template_args' : '{"title":"방금, 신용카드가 결제되었습니다."}'
    }

response = requests.post(send_url1, headers=headers, data=data)
response.status_code


data={
    "template_id" : 61894,
     'template_args' : '{"title":"대도식당 동백지점에서 250,400원 국민카드 결재","BtnName":"매출전표보기"}'
    }

response = requests.post(send_url1, headers=headers, data=data)
response.status_code

data={
    "template_id" : 61910,
    # "receiver_uuids": '["{}"]'.format(friend_id),
     'template_args' : '{"title":"대도식당 동백지점은 사업자 상태는 정상상태이며, 용인시 처인구 동백지구에 위치해 있습니다.","BtnName":"지도로보기"}'
    }

response = requests.post(send_url1, headers=headers, data=data)
response.status_code

data={
    "template_id" : 61911,
    # "receiver_uuids": '["{}"]'.format(friend_id),
     'template_args' : '{"title":"비과세 가맹점입니다. 10% 부가세를 추가적으로 내셨다면 불법입니다.","BtnName":"신고하기"}'
    }

response = requests.post(send_url1, headers=headers, data=data)
response.status_code

data={
    "template_id" : 61918 ,
    # "receiver_uuids": '["{}"]'.format(friend_id),
     'template_args' : '{"title":"자동으로 분류된 계정과목은 접대비 입니다. (가맹점 + 과거이 력 근거)"}'
    }

response = requests.post(send_url1, headers=headers, data=data)
response.status_code

data={
    "template_id" : 61914,
    # "receiver_uuids": '["{}"]'.format(friend_id),
     'template_args' : '{"title":"이 가맹점에서 3일전 (9월 15일 오후 4시) 142,000원을 결제한 이력이 존재합니다.","BtnName":"사용이력 보기"}'
    }

response = requests.post(send_url1, headers=headers, data=data)
response.status_code

data={
    "template_id" : 61896,
    # "receiver_uuids": '["{}"]'.format(friend_id),
     'template_args' : '{"title":"국민카드의 한도는, 1,204,650원이 남았습니다."}'
    }

response = requests.post(send_url1, headers=headers, data=data)
response.status_code

data={
    "template_id" : 61896,
    # "receiver_uuids": '["{}"]'.format(friend_id),
     'template_args' : '{"title":"세부 사용용도를 입력해주세요."}'
    }

response = requests.post(send_url1, headers=headers, data=data)
response.status_code