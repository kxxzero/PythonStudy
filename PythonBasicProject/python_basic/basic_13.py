import oracledb
conn=oracledb.connect(user="hr", password="happy", dsn="localhost:1521/XE")
# conn=DriverManager.getConnection(URL, user, pwd)

cursor=conn.cursor()
# ps=conn.preparedStatement()

page=int(input("페이지 입력:"))
rowSize=10;
start=(rowSize*page)-(rowSize-1)
end=rowSize*page

sql=f"""
    SELECT fno, name, address, type, num 
    FROM (SELECT fno, name, address, type, rownum as num 
    FROM (SELECT fno, name, address, type, 
    FROM food_menu 
    ORDER BY fno ASC))
    WHERE num BETWEEN {start} AND {end}
    """

cursor.execute(sql)

for row in cursor:
    print(row)

cursor.close()
conn.close()