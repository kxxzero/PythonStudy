import oracledb

"""
    Model => DAO, Service, VO, @Controller
            기능별 분리
"""

def getConnection():
        try:
            conn=oracledb.connect(user="hr", password="happy", dsn="localhost:1521/xe")
        except Exception as e:
            print(e)
        return conn
def studentListData():
    conn=getConnection()
    cursor=conn.cursor()
    sql=f"""
            SELECT hakbun, name, kor, eng, math 
            FROM student
        """
    cursor.execute(sql)
    std_data=cursor.fetchall() # 전체 데이터 가져오기
    cursor.close()
    conn.close()
    return std_data

def studentInsert():
    name=input("이름 입력:")
    kor=int(input("국어 점수 입력:"))
    eng = int(input("영어 점수 입력:"))
    math = int(input("수학 점수 입력:"))
    sql=f"""
        INSERT INTO student VALUES(
            std_hak_seq.nextval,:1,:2,:3,:4)
        """
    data=(name, kor, eng, math)
    conn=getConnection()
    cursor=conn.cursor()
    cursor.execute(sql, data)
    conn.commit()
    cursor.close()
    conn.close()

def studentFind(hakbun):
    conn=getConnection()
    cursor=conn.cursor()
    sql=f"""
            SELECT * FROM student WHERE hakbun={hakbun}
        """
    cursor.execute(sql)
    find_data=cursor.fetchone()
    cursor.close()
    conn.close()
    return find_data

def studentDelete(hakbun):
    conn=getConnection()
    cursor=conn.cursor()
    sql=f"""
            DELETE FROM student
            WHERE hakbun={hakbun}
        """
    cursor.excute(sql)
    conn.commit()
    cursor.close()
    conn.close()

# studentInsert()
std_data=studentListData()
for std in std_data:
    print(std)

print("=========================")
hak=int(input("학번 입력:"))
studentDelete(hak)
std_data=studentListData()
for std in std_data:
    print(std)


def studentUpdate(hakbun):
    conn=getConnection()
    cursor=conn.cursor()
    sql=f"""
            UPDATE student SET
            name=:1, kor=:2, eng=:3, math=:4
            WHERE hakbun=:5
        """
    cursor.excute(sql)
    conn.commit()
    cursor.close()
    conn.close()


stdData=('을지문덕', 90,90,90,2)
studentUpdate(stdData);
name=input("이름 입력:")
kor=int(input("국어:"))
eng=int(input("영어:"))
math=int(input("수학:"))
hakbun=int(input("학번:"))

stdData=(name,kor, eng, math, hakbun)
studentUpdate(stdData)
std_data=studentListData()

ste_data=studentListData()
for std in std_data:
    print(std)


find_data=studentFind(hak)
print(f"학번:{find_data[0]}")
print(f"이름:{find_data[1]}")
print(f"국어:{find_data[2]}")
print(f"영어:{find_data[3]}")
print(f"수학:{find_data[4]}")

print(f"총점:{find_data[2]+find_data[3]+find_data[4]}")
print(f"총점:{(find_data[2]+find_data[3]+find_data[4])/3}")


