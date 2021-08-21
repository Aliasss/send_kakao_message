import json
import requests
import datetime
import os

# 인증 코드 요청하는 url = https://kauth.kakao.com/oauth/authorize?client_id=70047bec78a0feb377cad903923ddf38&response_type=code&redirect_uri=https://localhost.com

code =  "XrBP5NuUbH8Ng-1TX6re1LUE45Ej1U8txc-ZC1aGUaFgKEvoiBP52YFapV1fnmOYthJNoQo9dJkAAAF7Y5oUcw"

def get_token():
    url = "https://kauth.kakao.com/oauth/token"

    data = {
        "grant_type" : "authorization_code",
        "client_id" : "70047bec78a0feb377cad903923ddf38",
        "redirect_uri" : "https://localhost.com",
        "code" : code
    }

    response = requests.post(url, data=data)

    # 요청에 실패한다면
    if response.status_code != 200:
        print(f"error occured. because of {response.json()}")
    # 성공하면
    else: 
        tokens = response.json()
        return tokens

# 저장
def save_tokens(filename, tokens):
    with open(filename, "w") as fp:
        json.dump(tokens, fp)


tokens = get_token()
TOKEN_FILENAME = "./kakao_message/kakao_token.json"

# 토큰 저장
save_tokens(TOKEN_FILENAME, tokens)
