import csv
import matplotlib.pyplot as plt
import random

file=open('c:\\pydata\\seoul.csv')
data=csv.reader(file)
next(data)
result=[]
for row in data:
    month=row[0].split('-')[1]
    if row[-1]!='':
        result.append(float(row[-1]))
plt.hist(result, bins=100, color='r')
plt.show()

file=open("c:\\pydata\\seoul.csv")
data=csv.reader(file)
next(data)
result=[]
for row in month:
    if row[-1]!='':
        if month=='04':
            a.append(float(row[-1]))
        if month=='05':
            b.append(float(row[-1]))
    plt.hist(a, bins=100, color='r', label='4월')
    plt.hist(b, bins=100, color='g', label='5월')
    plt.legend()
    plt.show()
