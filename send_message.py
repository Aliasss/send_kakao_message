import json
import requests
import kakao_utils
import top_news_crawling
import schedule
import time
import os

def send_message():
    TOKEN_FILENAME = "./kakao_message/kakao_token.json"
    KAKAO_APP_KEY = "해시키"

    news_class = top_news_crawling.news()

    # Load token
    tokens = kakao_utils.load_tokens(TOKEN_FILENAME)

    # 토큰 만료됐을 시 실행 -> update token
    # tokens = kakao_utils.update_tokens(KAKAO_APP_KEY, TOKEN_FILENAME)

    # save token
    # kakao_utils.save_tokens(TOKEN_FILENAME, tokens)

    # template
    template = {
        "object_type" : "list", 
        "header_title" : "TOP 3 뉴스",
        "header_link" : {
            "web_url" : "https://news.naver.com/",
            "mobile_web_url" : "https://news.naver.com/"
        },
        "contents" : [
            {
                "title" : news_class.title()[0],
                "description" : "첫 번째 랭킹 뉴스",
                "image_url" : news_class.image_url()[0],
                "image_width" : 50, "image_height" : 50,
                "link" : {
                    "web_url" : news_class.link()[0],
                    "mobile_web_url" : news_class.link()[0]
                }
            },
            {
                "title" : news_class.title()[1],
                "description" : "두 번째 랭킹 뉴스",
                "image_url" : news_class.image_url()[1],
                "image_width" : 50, "image_height" : 50,
                "link" : {
                    "web_url" : news_class.link()[1],
                    "mobile_web_url" : news_class.link()[1]
                }
            },
            {
                "title" : news_class.title()[2],
                "description" : "세 번째 랭킹 뉴스",
                "image_url" : news_class.image_url()[2],
                "image_width" : 50, "image_height" : 50,
                "link" : {
                    "web_url" : news_class.link()[2],
                    "mobile_web_url" : news_class.link()[2]
                }
            }
        ],
        "buttons" : [
            {
                "title" : "코로나 실시간 확인",
                "link" : {
                    "web_url" : "https://corona-live.com",
                    "mobile_web_url" : "https://corona-live.com"
                }
            }
        ]
        
    }

    # send kakao message
    res = kakao_utils.send_message(TOKEN_FILENAME, template)

    # 요청에 실패하면
    if res.status_code != 200:
        print(f"error. the reason is {res.json()}")
    # 성공하면
    else:
        print('메시지 전송 성공!')

send_message()

# scheduling
# schedule.every(1).minutes.do(send_message)
# while True:
#     schedule.run_pending()
#     time.sleep(1)



