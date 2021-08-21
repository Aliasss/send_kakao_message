import requests
from bs4 import BeautifulSoup
import datetime
import pandas as pd
import numpy as np
import json

# 네이버의 경우 robot.txt가 뉴스 크롤링 막음.
# 브라우저 콘솔창에서 navigator.userAgent로 유저 에이전트 스트링 확인 후 헤더 전송

class news:

    url = 'https://news.naver.com/main/ranking/popularDay.naver?mid=etc&sid1=111'
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}
    req = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')

    def title(self):
        titles = []
        for title in self.soup.select("div.rankingnews_box_wrap._popularRanking > div > div > ul > li > div"):
            titles.append(title.text)

        return titles

    def link(self):
        links = []
        for link in self.soup.select("div.rankingnews_box_wrap._popularRanking > div > div > ul > li > div > a"):
            links.append("https://news.naver.com" + link['href'])
        
        return links

    def image_url(self):
        images = []
        for image in self.soup.select("div.rankingnews_box_wrap._popularRanking > div > div > ul > li > a > img"):
            images.append(image['src'])

        return images


# news = news()
# # titles = news.title()[0]
# links = news.link()[0]
# # images = news.image_url()[0]
# print(links)
