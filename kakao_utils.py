import json
import datetime
import requests
import os

# 인증 코드 요청하는 url = https://kauth.kakao.com/oauth/authorize?client_id=70047bec78a0feb377cad903923ddf38&response_type=code&redirect_uri=https://localhost.com
# 토큰 업데이트 -> 토큰 저장 필수
# KAKAO_APP_KEY = <REST_API 앱 키를 입력하세요>
# tokens = update_tokens(KAKAO_APP_KEY, TOKEN_FILENAME)
# save_tokens(TOKEN_FILENAME, tokens)

# 저장
def save_tokens(filename, tokens):
    with open(filename, "w") as fp:
        json.dump(tokens, fp)
    
# load
def load_tokens(filename):
    with open(filename) as fp:
        tokens = json.load(fp)

    return tokens

# refresh_token으로 access_token 갱신
def update_tokens(app_key, filename):
    tokens = load_tokens(filename)
    url = "https://kauth.kakao.com/oauth/token"
    data = {
        "grant_type" : "refresh_token",
        "client_id" : app_key,
        "refresh_token" : tokens['refresh_token']
    }
    response = requests.post(url, data=data)

    # 요청 실패
    if response.status_code != 200:
        print(f"error occured. {response.json()}")
        tokens = None
    # 성공하면
    else:
        print(response.json())
        # 기존파일백업
        now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = filename + "." + now
        os.rename(filename, backup_filename)
        # 갱신된 토큰 저장
        tokens['access_token'] = response.json()['access_token']
        save_tokens(filename, tokens)

    return tokens

# 메시지 전송
def send_message(filename, template):
    tokens = load_tokens(filename)

    headers = {
        "Authorization" : "Bearer " + tokens['access_token']
    }

    # JSON format -> string
    payload = {
        "template_object" : json.dumps(template)
    }

    # 카카오톡 메시지 전송
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    res = requests.post(url, data=payload, headers=headers)

    return res