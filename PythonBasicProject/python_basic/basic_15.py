import sqlite3

"""
   함수
   def 함수명 : 
    처리 기능
    return 값
"""

def getConnection():
    try:
        conn=sqlite3.connect("memberdb")
    except Exception as e:
        print(e)
    return conn

def createDB():
    conn=getConnection()
    cursor=conn.cursor()
    sql=f"""
            CREATE TABLE member(id text, name text, sex text, address text, phone text)
        """
    cursor.execute(sql)
    print("테이블 생성 완료")
    cursor.close()
    conn.close()

# createDB()

def insert():
    conn=getConnection()
    cursor=conn.cursor()
    id=input("ID 입력:")
    name=input("이름 입력:")
    sex=input("성별 입력:")
    address=input("주소 입력:")
    phone=input("번호 입력:")

#insert
def find(id):
    conn=getConnection()
    cursor=conn.cursor()
    sql="SELECT * FROM member WHERE id={id}"
    cursor.execute(sql)
    find_data=cursor.fetchone()
    cursor.close()
    conn.close()
    return find_data




def memberDelete(id):
    conn=getConnection()
    cursor=conn.cursor()
    sql=f"DELETE FROM member WHERE id='{id}'"
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

def memberUpdate(memberVO):
    conn=getConnection()
    cursor=conn.cursor()
    sql=f"""
            UPDATE member SET
            name=?, sex=?, address=?, phone=?
            WHERE id=?
        """

    cursor.execute(sql, memberVO)
    conn.commit()
    cursor.close()
    conn.close()



cur=selectList()
for row in cur:
    print(row)
