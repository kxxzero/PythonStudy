from bs4 import BeautifulSoup
import requests
import sqlite3
url="https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
data=requests.get(url)
xml=data.text
# print(xml)

#database table 관리
"""
#테이블 삭제
conn=sqlite3.connect("weatherdb") # 테이블 자동 생성
cursor=conn.cursor()
sql="DROP TABLE IF EXISTS weather" # weather라는 테이블이 이미 존재하면 삭제
cursor.execute(sql) # sql 문장 실행
cursor.close()
conn.close()
print("테이블 삭제 완료")
"""

"""
#테이블 생성
conn=sqlite3.connect("weatherdb")
cursor=conn.cursor()
sql="
        CREATE TABLE IF NOT EXISTS weather(
            city text,
            mode text,
            wf text,
            tmin integer,
            tmax integer
        )
    "
cursor.execute(sql)
cursor.close()
conn.close()
print("날씨 데이터베이스 생성")
"""

# database에 data 저장

# site 읽기
soup=BeautifulSoup(xml, "html.parser")
for location in soup.find_all("location"):
    # print(location)
    try:
        city=location.find("city").string # string으로 data를 가져옴
        mode=location.find("mode").string
        wf=location.find("wf").string
        tmin=location.find("tmn").string
        tmax=location.find("tmx").string
        print(city, mode, wf, tmin, tmax)

        # database에 저장
        conn=sqlite3.connect("weatherdb")
        cursor=conn.cursor()
        sql="""
            INSERT INTO weather VALUES(?,?,?,?,?)
            """
        cursor.execute(sql, (city, mode, wf, tmin, tmax)) # Tuple
        conn.commit()
        cursor.close()
        conn.close()
        print("1 row Insert")
    except Exception as e:
        print(e)


conn=sqlite3.connect("weatherdb")
cursor=conn.cursor()
city=input("지역 입력:")
sql=f"SELECT * FROM weather WHERE city='{city}'"
cursor.execute(sql)
data=cursor.fetchone() # 1개만 가져옴
print(f"지역:{data[0]}")
print(f"날씨:{data[2]}")
print(f"온도:{str(data[3])+"/"+str(data[4])}")

