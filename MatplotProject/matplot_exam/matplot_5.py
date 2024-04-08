import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import csv

"""
    데이터 출처 : data.go.kr => csv 파일(로그인 필요)
"""

file=open('c:\\pydata\\subwaytime.csv')
data=csv.reader(file)
next(data)
next(data)

# 출퇴근 시 가장 많이 승하차 하는 역 확인

for row in data:
    row[4:]=map(int, row[4:]) # map : 지정된 위치의 모든 데이터를 정수형으로 변환
    print(row)



