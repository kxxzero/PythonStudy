import oracledb
conn=oracledb.connect(user="hr", password="happy", dsn="localhost:1521/xe")
cursor=conn.cursor()
cursor.execute("SELECT empno, ename, job, sal FROM emp")
emp_data=cursor.fetchmany() # fetchmany : 여러 개 가져오기 / fetchone : 1개 가져오기
cursor.close()

print(emp_data) # 튜플(1개의 Row) 형태로 출력
"""
    List : []
    Tuple : () => ~VO와 같은 역할
"""
for empno, ename, job, sal in emp_data:
    print(empno, ename, job, sal)
