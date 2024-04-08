import oracledb

# 오라클 연결 => Connection
conn=oracledb.connect(user="hr", password="happy", dsn="localhost:1521/xe")

# 커서 생성
cursor=conn.cursor()

# SQL 문장
sql=f"""
        SELECT empno, ename, job, hiredate, sal, dname, loc
        FROM emp, dept
        WHERE emp.deptno=dept.deptno
    """
# 실행
cursor.execute(sql)

# 결과값 받기
emp_data=cursor.fetchmany()

# 출력
for emp in emp_data:
    print(emp)

for row in cursor:
    for i in range(len(row)):
        print(row[i], end=" ")
    print('')

#닫기
cursor.close()

"""
    SQL 종류
        DML : 웹 프로그램의 핵심
            = SELECT : 데이터 검색
                형식) 
                    SELECT * column1, column2...
                    FROM (table_name|view_name|SELECT~~)
                    [
                        WHERE 조건문
                            - 연산자
                                산술연산자 | 논리연산자 | 비교연산자
                                BETWEEN ~ AND
                                IN
                                LIKE
                                IS NULL / IS NOT NULL
                            - 내장 함수
                                문자 : substr, length, rpad, instr
                                숫자 : ceil, round, trunc
                                날짜 : sysdate => now(), month_between
                                변환 : to_char => datetime.format()
                                기타 : nvl => isnull
                                그룹 함수
                        GROUP BY 그룹 컬럼
                        HAVING 그룹 조건
                        ORDER BY 컬럼
                    ]
            = INSERT : 데이터 추가
                - INSERT INTO table VALUES(값...) => 컬럼 전체 값 설정
                - INSERT INTO table(column1...) VALUES(값...) => default가 많은 경우
            = UPDATE : 데이터 수정
                - UPDATE table SET column=값, column=값... WHERE 조건
            = DELETE : 데이터 삭제
                - DELETE FROM table WHERE 조건
            -------------------------> CURD
        DDL :
            = CREATE
            = ALTER
            = DROP
            = TRUNCATE
            = RENAME
            *** 제약 조건
                - CHECK
                - PRIMARY KEY
                - FOREIGN KEY
                - UNIQUE
                - NOT NULL
        DCL: 
            = GRANT
            = REVOKE
        TCL :
            = COMMIT
            = ROLLBACK       
"""
