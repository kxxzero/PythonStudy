from django.db import models
#VueJS
import oracledb
from web import models

def recipeListData(page):
    try:
        conn=models.getConnection()
        cursor=conn.cursor()
        rowSize=20
        start=(rowSize*page)-(rowSize-1)
        end=rowSize*page
        sql=f"""
                SELECT no, title, poster, chef, num
                FROM (SELECT no, title, poster, chef, rownum as num
                FROM (SELECT no, title, poster, chef
                FROM recipe
                WHERE no IN(SELECT no FROM recipe
                INTERSECT SELECT no FROM recipeDetail)
                ORDER BY no ASC))
                WHERE num BETWEEN {start} AND {end}                
            """
        # INTERSECT : 교집합 => 상세보기
        cursor.execute(sql)
        recipe_list=cursor.fetchall() # () => 여러 개, () 1개면 fetchone()
        # selectList . selectOne => MyBatis, JPA(X) => ORM
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)

def recipeTotalPage():
    try:
        conn=models.getConnection()
        cursor=conn.cursor()
        sql="""
                SELECT CEIL(COUNT(*)/20.0)
                FROM recipe
                WHERE no IN(SELECT no FROM recipe
                INTERSECT SELECT no FROM recipeDetail)
            """
        cursor.execute(sql)
        total=cursor.fetchone()
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)

    return total[0]



def recipeFindData(page, fd):
    try:
        conn=models.getConnection()
        cursor=conn.cursor()
        rowSize=20
        start=(rowSize*page)-(rowSize-1)
        end=rowSize*page
        sql=f"""
                SELECT no, title, poster, chef, num
                FROM (SELECT no, title, poster, chef, rownum as num
                FROM (SELECT no, title, poster, chef
                FROM recipe
                WHERE no IN(SELECT no FROM recipe
                INTERSECT SELECT no FROM recipeDetail)
                AND title LIKE '%'||'{fd}'||'%'
                ORDER BY no ASC))
                WHERE num BETWEEN {start} AND {end}                
            """
        # INTERSECT : 교집합 => 상세보기
        cursor.execute(sql)
        recipe_list=cursor.fetchall() # () => 여러 개, () 1개면 fetchone()
        # selectList . selectOne => MyBatis, JPA(X) => ORM
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)

def recipeFindTotalPage(fd):
    try:
        conn=models.getConnection()
        cursor=conn.cursor()
        sql=f"""
                SELECT CEIL(COUNT(*)/20.0)
                FROM recipe
                WHERE no IN(SELECT no FROM recipe
                INTERSECT SELECT no FROM recipeDetail)
                AND title LIKE '%'||'{fd}'||'%'
            """
        cursor.execute(sql)
        total=cursor.fetchone()
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)

    return total[0]


def recipeChefList(page):
    try:
        conn=models.getConnection()
        cursor=conn.cursor()
        rowSize = 20
        start = (rowSize * page) - (rowSize - 1)
        end = rowSize * page

        sql=f"""
                SELECT cno, chef, poster, mem_cont1, mem_cont2, mem_con3, mem_con7, num
                FROM (SELECT cno, chef, poster, mem_cont1, mem_cont2, mem_con3, mem_con7, rownum as num
                FROM (SELECT cno, chef, poster, mem_cont1, mem_cont2, mem_con3, mem_con7
                from CHEF
                ORDER BY cno ASC
                WHERE num BETWEEN {start} AND {end}
            """
        cursor.execute(sql)
        chef_list=cursor.fetchall()
        cursor.close()
        conn.close()

    except Exception as e:
        print(e)

    return chef_list

def recipeChefTotalPage():
    try:
        conn=models.getConnection()
        cursor=conn.cursor()
        sql="""
                SELECT CEIL(COUNT(*)/20.0) FROM chef
            """
        cursor.execute(sql)
        total=cursor.fetchone()
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)

    return total[0]


def recipe_detail(no):
    conn=models.getConnection()
    cursor=conn.cursor()
    sql=f"""
            SELECT * FROM recipedetail
            WHERE no={no}
        """
    cursor.execute(sql)
    recipe_detail=cursor.fetchone()



# from django.db import models
# from web import models
# import oracledb
#
# def recipeListData(page):
#     try:
#         conn=models.getConnection()
#         cursor=conn.cursor()
#         rowSize=20
#         start=(rowSize*page)-(rowSize-1)
#         end=rowSize*page
#
#         sql=f"""
#                 SELECT no, title, poster, chef
#                 FROM (SELECT no, title, poster, chef, rownum as num
#                 FROM (SELECT no, title, poster, chef
#                 FROM recipe ORDER BY no ASC))
#                 WHERE num BETWEEN {start} AND {end}
#             """
#
#         # 실행
#         cursor.execute(sql)
#         # 데이터 받기
#         recipe_list=cursor.fetchall()
#         cursor.close()
#         conn.close()
#     except Exception as e:
#         print(e)
#     return recipe_list
#
# def recipeTotalPage():
#     try:
#         conn=models.getConnection()
#         cursor=conn.cursor()
#         sql="""
#             SELECT CEIL(COUNT(*)/20.0) FROM recipe
#             """
#         cursor.execute(sql)
#         total=cursor.fetchone()
#         cursor.close()
#         conn.close()
#     except Exception as e:
#         print(e)
#
#     return total[0]
#
#
# def recipeCount():
#     try:
#         conn=models.getConnection()
#         cursor=conn.cursor()
#         sql="""
#             SELECT COUNT(*) FROM recipe
#             """
#         cursor.execute(sql)
#         total=cursor.fetchone()
#         cursor.close()
#         conn.close()
#     except Exception as e:
#         print(e)
#
#     return total[0]
#
#
#
# def recipeFindData(page, title):
#     try:
#         conn=models.getConnection()
#         cursor=conn.cursor()
#         rowSize=20
#         start=(rowSize*page)-(rowSize-1)
#         end=rowSize*page
#
#         sql=f"""
#                 SELECT no, title, poster, chef
#                 FROM (SELECT no, title, poster, chef, rownum as num
#                 FROM (SELECT no, title, poster, chef
#                 FROM recipe
#                 WHERE title LIKE '%'||'{title}'||'%'
#                 ORDER BY no ASC))
#                 WHERE num BETWEEN {start} AND {end}
#             """
#
#         # 실행
#         cursor.execute(sql)
#         # 데이터 받기
#         recipe_list=cursor.fetchall()
#         print(recipe_list)
#         cursor.close()
#         conn.close()
#     except Exception as e:
#         print(e)
#     return recipe_list
#
#
# def recipeFindTotalPage(title):
#     try:
#         conn=models.getConnection()
#         cursor=conn.cursor()
#         sql=f"""
#             SELECT CEIL(COUNT(*)/20.0) FROM recipe
#             WHERE title LIKE '%'||'{title}'||'%'
#             """
#         cursor.execute(sql)
#         total=cursor.fetchone()
#         cursor.close()
#         conn.close()
#     except Exception as e:
#         print(e)
#
#     return total[0]
#
# def recipeFindCount(title):
#     try:
#         conn=models.getConnection()
#         cursor=conn.cursor()
#         sql=f"""
#             SELECT COUNT(*) FROM recipe
#             WHERE title LIKE '%'||'{title}'||'%'
#             """
#         cursor.execute(sql)
#         total=cursor.fetchone()
#         cursor.close()
#         conn.close()
#     except Exception as e:
#         print(e)
#
#     return total[0]