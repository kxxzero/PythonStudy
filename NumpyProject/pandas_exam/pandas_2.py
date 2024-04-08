"""
    between ~ and => 데이터프레임['컬럼'].between(값1, 값2)
    in            => 데이터프레임['컬럼']

"""
import pandas as pd

emp=pd.read_csv('c:\pydata\EMP.csv')
print(emp)

print(emp[['EMPNO', 'ENAME', 'DEPTNO']][emp['DEPTNO'].isin([10,20,30])])

print(emp[['EMPNO', 'ENAME', 'JOB', 'SAL', 'COMM']][emp['COMM'].isull()])



