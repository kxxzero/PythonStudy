import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import csv

# 데이터 읽기
file=open('c:\\pydata\\dage.csv')
data=csv.reader(file)
file=[]

m =[]
f=[]
# for row in data:
#     if '서교동' in row[0]: