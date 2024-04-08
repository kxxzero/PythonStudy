#-*- coding:utf-8 -*-
import urllib.request as req
from bs4 import BeautifulSoup
import requests

def request(url):
    response=req.urlopen(url)
    bytes_data=response.read()
    text_data=bytes_data.decode('utf-8')
    return text_data

for page in range(1, 3):
    url=f"https://www.10000recipe.com/recipe/list.html?order=reco&page={page}"
    webpage=request(url)
    # Jsoup.connection(url).get()yyyyyyy                                        b

    # print(webpage) // 확인용

    res=req.urlopen(url)
    soup=BeautifulSoup(res, 'html.parser')
    aTitle=soup.select('ul.common_sp_list_ul  div.common_sp_caption  div.common_sp_caption_tit')
    aChef=soup.select('ul.common_sp_list_ul  div.common_sp_caption  div.common_sp_caption_rv_name a')
    aImage=soup.select('ul.common_sp_list_ul div.common_sp_thumb img[src*="/recipe/"]')

    print(aImage)
    for index in range(0, len(aTitle)):
        print(aTitle[index].text)
        print(aChef[index].text)
        print(aImage[index].get("src"))

    print("=========================")
