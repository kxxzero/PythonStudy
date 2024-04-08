import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import csv

file=open('c:\\pydata\\age.csv')
data=csv.reader(file)
# for row in data:
#     if '서울특별시 마포구 상암동(1144074000)'==row[0]:
#         print(row)

for row in data:
    if '서교동' in row[0]:
        for i in row[3:]: # 3번째 이후부터
            print(i)

# df dongFind(dong) :
#     result=[]
#     for now in data:
#         if dong in row[0]:
#             for i in row[3:]:
#                 result.append(i)
#
#     print(result)
#
#     plt.style.use("ggplot")
#     plt.rc('font', family="Malgun Gothic")
#     plt.title(dong+"지역 인구 구조")
#
#     plt.plot(result)
#     plt.show()
#     file.close()
# dong=input("동 입력:")
# dongFind(dong)
