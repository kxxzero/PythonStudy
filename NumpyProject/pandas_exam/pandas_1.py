# SELECT * FROM emp WHERE deptno=30 or job='SALESMAN'
# => print(emp_df[(emp_df['DEPTNO']==30) | (emp_df['JOB']=='SALESMAN']))

# SELECT job, deptno FROM emp WHERE deptno=30 AND (job='SALESMAN' OR deptno=10)

