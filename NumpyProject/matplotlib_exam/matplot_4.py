import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

file=open('c:\pydata\seoul.csv', 'r', encoding='cp949') # r: 읽기 전용 / cp949 : 한글
data=csv.reader(file) # 전체 읽기
header=next(data) # 데이터 맨 윗줄에 제목이 저장되어 있어 그 다음 줄부터 불러와야 함

max_temp=-999
max_date=''
for row in data:
    if row[-1] == '':
        row[-1] = -999
    row[-1]=float(row[-1])

    if max_temp < row[-1] :
        max_date = row[0]
        max_temp = row[-1]
    print(row)

print(f"가장 기온이 높은 날: {max_date}")
print(f"가장 높은 온도 : {max_temp}, 날짜: {max_date}")
file.close()

print("=========================")

file=open('c:\pydata\seoul.csv', 'r', encoding='cp949')
data=csv.reader(file)
next(data)
result=[]

for row in data:
    if row[-1] != '': # 값이 누락된 데이터는 제외
        result.append(float(row[-1]))
print(len(result)) # 39168개

plt.plot(result)
plt.show()
file.close()

print("=========================")

s='1907-10-01'
print(s.split("-")[0])
print(s.split("-")[1])
print(s.split("-")[2])

# 2024년 4월 5일 날씨 예측
file=open('c:\pydata\seoul.csv', 'r', encoding='cp949')
data=csv.reader(file)
next(data)
hi=[]
low=[]
result=[]

for row in data:
    if row[-1] !='': # 값이 공백인 데이터 제외
        if row[0].split('-')[1]=='04' and row[0].split('-')[2]=='05':
            hi.append(float(row[-1]))
            low.append(float(row[2]))
# print(result)
# arr=np.array(result)
# print(arr.mean())
plt.plot(hi, 'hotpink')
plt.plot(low, 'skyblue')
plt.show()
file.close()