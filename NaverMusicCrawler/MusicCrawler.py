import os
import requests
import sys
import json
from bs4 import BeautifulSoup

Base_Dir = os.path.dirname('./NaverMusicCrawler/__File__/')

print("Start Crawling")
req = requests.get('https://music.naver.com/listen/top100.nhn?domain=TOTAL')
req.encoding = None
html = req.content #html요소 전부 가져오기
soup = BeautifulSoup(html, 'html.parser') #html 파싱
datas = soup.select(
    '#content > div.NE\=a\:t1a > div._tracklist_mytrack.tracklist_table.tracklist_type1 > table > tbody > tr > td.name > a._title > span'
    )
data = {}

for i in range(len(datas)):
    rank = i+1
    name = datas[i].get_text()
    print(str(rank) + ". " + name)
    data[rank] = name

with open(os.path.join(Base_Dir, 'musicRank.json'), 'w+',encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii = False, indent='\t')
    
print("Crawling Complete")