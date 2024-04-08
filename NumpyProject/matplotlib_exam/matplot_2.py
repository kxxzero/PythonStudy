# 막대그래프

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv

x=np.arange(3)
years=['2022', '2023', '2024']
values=[100,500,900]
plt.barh(x,values)
plt.xticks(x,years)
plt.show()

np.random.seed(0)
n=50
x=np.random.rand(n)
y=np.random.rand(n)

