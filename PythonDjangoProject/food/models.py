# import => *(전체)
# from => 전체가 아닌 필요한 것만 첨부
import oracledb
from django.db import models

# @Service역할

# Create your models here.
def getConnection():
    try:
        conn=oracledb.connect(user="hr", password="happy", dsn="localhost:1521/XE")
    except Exception as e:
        print(e)
    return conn

def foodListData(page):
    conn=getConnection()
    cursor=conn.cursor()
    rowSize=12
    start=(rowSize*page)-(rowSize-1)
    end=rowSize*page
    sql=f"""
            SELECT fno, name, poster, num
            FROM (SELECT fno, name, poster, rownum as num
            FROM (SELECT fno, name, poster
            FROM food_menu_house
            ORDER BY fno ASC))
            WHERE num BETWEEN {start} AND {end}
        """

    cursor.execute(sql)
    food_data=cursor.fetchall() # 실행한 모든 결과
    cursor.close()
    conn.close()
    return food_data

def foodTotalPage():
    conn=getConnection()
    cursor=conn.cursor()
    sql=f"""
            SELECT CEIL(COUNT(*)/12.0) FROM food_menu_house
        """
    cursor.execute(sql)
    count=cursor.fetchone()
    cursor.close()
    conn.close()

    return count[0]

def foodInfoData(fno):
    try:
        conn=getConnection()
        #cursor : 송수신 => sql 전송 => 실행 결과값을 읽어 옴 : Statement
        cursor=conn.cursor()
        sql=f"""
                SELECT fno, name, poster
                FROM food_menu_house
                WHERE fno={fno}
            """
        cursor.execute(sql)
        info_data=cursor.fetchone()
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)

    return info_data


def foodDetailData(fno):
    try:
        conn=getConnection()
        #cursor : 송수신 => sql 전송 => 실행 결과값을 읽어 옴 : Statement
        cursor=conn.cursor()
        sql=f"""
                SELECT fno, name, poster, address, phone, type, time, theme, seat, score
                FROM food_menu_house
                WHERE fno={fno}
            """
        cursor.execute(sql)
        detail_data=cursor.fetchone()
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)

    return detail_data