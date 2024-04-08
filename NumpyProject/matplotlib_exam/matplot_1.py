"""
    1. pip install matplotlib
    => 데이터는 pandas => 연산 처리 numpy
    => 시각화 matplotlib

"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv

file=open("c:\pydata\EMP.csv")
emp=csv.reader(file)
data=[]

for i in emp:
    data.append(i[5])
plt.plot(data)
plt.show()

# 축 레벨 설정
plt.plot([1,2,3,4],[1,4,9,10], label="Price($)")
plt.legend()
plt.show()

# 축 범위 설정
plt.plot([1,2,3,4],[1,4,9,16])
plt.xlabel('ename')
plt.ylabel('sal')
plt.xlim([0,10])
plt.ylim([0,20])
plt.show()

plt.plot([1,2,3],[4,4,4], '-', color="C0", label="Solid")
plt.plot([1,2,3],[3,3,3], '--', color="C0", label="Dashed")
plt.plot([1,2,3],[2,2,2], ':', color="C0", label="Dotted")
plt.plot([1,2,3],[1,1,1], '-.', color="C0", label="DashDot")
plt.legend()
plt.show()

plt.plot([1,2,3],[4,4,4], 'bo-')
"""
    bo / bv / b*
    'r', 'g', 'v' / 'm', 'c', 'k', 'w'
"""
plt.show