from django.db import models
import oracledb

# Create your models here.
def getConnection():
    try:
        conn=oracledb.connect(user="hr", password="happy", dsn="localhost:1521/XE")
    except Exception as e:
        print(e)
    return conn

def mainRecipeData():
    try:
        conn=getConnection() # Connection
        cursor=conn.cursor() # PrepareStatement => SQL 전송 => 결과값 받기
        sql="""
            SELECT no, title, poster, chef, rownum
            FROM (SELECT no, title, poster, chef
            FROM recipe ORDER BY no ASC)
            WHERE rownum<=5
            """
        cursor.execute(sql)
        recipe_list=cursor.fetchall()
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)
    return recipe_list

def mainFoodData():
    try:
        conn=getConnection() # Connection
        cursor=conn.cursor() # PrepareStatement => SQL 전송 => 결과값 받기
        sql="""
            SELECT fno, name, poster, rownum
            FROM (SELECT fno, name, poster
            FROM food_menu_house ORDER BY fno ASC)
            WHERE rownum<=8
            """
        cursor.execute(sql)
        food_list=cursor.fetchall()
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)
    return food_list


def mainChefData():
    conn=getConnection()
    cursor=conn.cursor()
    sql="""
        SELECT chef, poster
        """


def todayFoodData():
    conn=getConnection()
    cursor-conn.cursor()
    sql="""
        SELECT 'http://www.menupan.com'||poster, name, address, rownum
        FROM food_menu_house
        WHERE rownum<=1    
        """
    cursor.execute(sql)
    today_house=cursor.fetchone()


import os
import sys
import urllib.request
import json
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
query='검색할 단어'
encText = urllib.parse.quote(query)
url = "https://openapi.naver.com/v1/search/news?query=" + encText # JSON 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
    news_data=json.dumps(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)

return news_data