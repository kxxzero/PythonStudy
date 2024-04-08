
# Pandas : 시각화
# 라이브러리 로드
import numpy as np
import pandas as pd
import matplotlib as mp1
import matplotlib.pyplot as plt
import seaborn as sns

# 한글 설정
mp1.rc('font', family="Malgun Gothic")
mp1.rc('axes', unicode_minus=False)

# 차트 스타일 설정
sns.set(font="Malgun Gothic", rc={"axes.unicode_minus": False}, style="darkgrid")
plt.rc('figure', figsize=(10,8))


# 데이터 생성
np.random.seed(0)


"""
    numpy : 난수 생성, 연산 처리 => 배열, 행렬
    pandas : 시리즈(1차원 배열), 데이터프레임(table 형식 : column + row)
    -------------------------
        A      B      C
    -------------------------
        값     값      값        
    -------------------------
"""

# 데이터프레임
df1=pd.DataFrame(np.random.rand(100,3),index=pd.date_range('1/1/2024', periods=100), columns=['A','B','C']).cumsum()

print(df1)

# 시각화
df1.plot()
plt.title("Pandas의 Plot을 이용")
plt.xlabel("시간")
plt.ylabel("데이터")
plt.show()

# 내장되어 있는 데이터 읽기
iris=sns.load_dataset('iris')
print(iris)

s1=iris.sepal_length[:20]
s1.plot(kind="bar", rot=0)
plt.title("내장 데이터 활용 IRIS")
plt.xlabel("데이터")
plt.ylabel("꽃받침의 길이")
plt.show()


df2=iris[:5]
df2.plot.bar(rot=0)
plt.title("내장 데이터 활용 IRIS")
plt.xlabel("데이터")
plt.ylabel("꽃받침의 길이")
plt.ylim(0,7)
plt.show()


# # 평균
# df3.iris.groupby(iris.species).mean()
# print(d3)
# df3.plot.bar(rot=0) # rot:rotate
#
#
# # Pie
# print(titan)
# df4=titan.pclass.value_counts()
# print(df4)
# df4.plot.pie(autopct="%.2f%%")
# plt.title("선실별 승객 수")
# plt.axis('eaqual')
# plt.show()

"""
    Pie, Plot, Bar, Pie, Hist, DataFrame
"""

iris.plot.box()
plt.title("Box를 이용")
plt.xlabel("처리")
plt.ylabel("데이터 값")
plt.show()


"""
    타이타닉 프로그램
    
    survived : 생존 여부
    pclass : 좌석 등급
    sex :
    age :
    who : 사람 구분
    fare : 요금
    embark_town : 탑승 항구
    alive : 생존 여부
    alone : 1인 여부
"""

tips=sns.load_dataset("tips")
print(tips)


ud=np.random.rand(10,12)
sns.heatmap(ud,annot=True)
plt.show()


# 상위 5개 출력
print(tips.head())
pivot=tips.pivot_table(index="day", columns="size", values="tips")
print(pivot)
sns.heatmap(pivot, annot=True)
plt.show()


sns.pairplot(tips)
plt.show()


sns.pairplot(tips, hue="size", palette="rainbow", height="5")
plt.show()


sns.lmplot(x="tatal_bill", y="tip", hue="smoker", height="8", data=tips)
