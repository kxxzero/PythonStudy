import csv
import matplotlib.pyplot as plt
import random

file=open('c:\\pydata\\seoul.csv')
data=csv.reader(file)
next(data)
month=[
    [],[],[],[],[],[],
    [],[],[],[],[],[]
]
result=[]
for row in data:
    if row[-1]!='':
        month[int(row[0].split('-')[1]-1)]
plt.boxplot(result)
plt.show()

result=emp.groupby('JOB')['SAL'].sum().reset_index()
colors=sns.color_palette()
print(colors)
print(result)
result['SAL'].plot.pie(labels=emp['JOB'], colors=colors)

