"""
    Before(데이터 전처리) : pandas(numpy) pip install pandas
                        matplotib
                        seaborn
                        wordcloud
                        missingno
                        => 분석 => 시각화
                        -------------------- 데이터 전처리 → 머신러닝(학습)
                                            데이터 전처리 + 머신러닝  = 딥러닝 => 기계에 첨부(AI)

    
    <지하철 데이터 분석>
    1. 데이터 읽기 / 확인
    2. 데이터 시각화
        1) 호선별 이용객 수 분석
        2) 역별 인원 데이터 분석
        3) 평균 승하차
        4) 혼잡 정도 => 위치 좌표 데이터 병합
        5) 특정 호선의 혼잡 정도 지도 출력
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import missingno as msno

# 워드 클라우드 => 뉴스, 댓글 => 요약 => 데이터 마이닝의 기본
# 1. 데이터 읽기
metro_all=pd.read_csv('c:\\pydata\\subway.csv',encoding="cp949")
#print(metro_all)
#dataset => data.go.kr , seoul.data.go.kr
# 상위 5개 => head(10) = default=5
print(metro_all.head())
# 요약
print(metro_all.info())
# 데이터 확인
print(sorted(list(set(metro_all['사용월']))))
print(sorted(list(set(metro_all['호선명']))))
print(sorted(list(set(metro_all['지하철역']))))
print(len(list(set(metro_all['지하철역']))))

# 데이터 전처리
# 2024 => 3
# column 변경 => 불필요한 컬럼 제거
metro_recent=metro_all[metro_all['사용월']==202403]
print(metro_recent)
metro_recent=metro_recent.drop(columns={'작업일자'})
print(metro_recent)

"""
metro_line=metro_recent.groupby(['호선명']).mean().reset_index()
metro_line=metro_line.drop(columns='사용월').set_index('호선명')
metro_line=metro_line.mean(axis=1).sort_values(ascending=False)
print(metro_line)
"""

"""
plt.figure(figsize=(20,10))
plt.rc('font',family='Malgun Gothic')
plt.rcParams['axes.unicode_minus']=False
metro_line.plot(kind="bar")
plt.show()
"""

# 특정 호선에서 역별 평균 승하차 인원 데이터 => 시각화
line = '2호선'
metro_st=metro_recent.groupby(['호선명','지하철역']).mean().reset_index()
print("==================================================")
print(metro_st)
metro_st_line2=metro_st[metro_st['호선명']==line]
print(metro_st_line2)

#승차인원 컬럼만 추출
metro_get_on=pd.DataFrame()
metro_get_on['지하철역']=metro_st_line2['지하철역']
print(metro_recent.columns)
for i in range(int((len(metro_recent.columns)-3)/2)):
    metro_get_on[metro_st_line2.columns[3+2*i]]=metro_st_line2[metro_st_line2.columns[3+2*i]]
metro_get_on=metro_get_on.set_index('지하철역')

print("========================= 승차 인원 ====================")
print(metro_get_on)

metro_get_off=pd.DataFrame()
metro_get_off['지하철역']=metro_st_line2['지하철역']
for i in range(int((len(metro_recent.columns)-3)/2)):
    metro_get_off[metro_st_line2.columns[4+2*i]]=metro_st_line2[metro_st_line2.columns[4+2*i]]
metro_get_off=metro_get_off.set_index('지하철역')

print("========================= 하차 인원 ====================")
print(metro_get_off)
# 역별로 평균 승하차 인원 => 데이터 프레임 => 시각화
df=pd.DataFrame(index=metro_st_line2['지하철역'])
print(df)
df['평균 승차 인원수']=metro_get_on.mean(axis=1).astype(int)
df['평균 하차 인원수']=metro_get_off.mean(axis=1).astype(int)
print(df)
print("==================================================")

top10_on=df.sort_values(by='평균 승차 인원수',ascending=False).head(10)
"""
plt.figure(figsize=(20,10))
plt.rc('font',family='Malgun Gothic')
plt.rcParams['axes.unicode_minus']=False
plt.bar(top10_on.index,top10_on['평균 승차 인원수'])
plt.title('2024년 3월 2호선 승차인원 Top10')
plt.show()
"""

top10_off=df.sort_values(by='평균 하차 인원수',ascending=False).head(10)
"""
plt.figure(figsize=(20,10))
plt.rc('font',family='Malgun Gothic')
plt.rcParams['axes.unicode_minus']=False
plt.bar(top10_off.index,top10_off['평균 하차 인원수'])
plt.title('2024년 3월 2호선 하차인원 Top10')
plt.show()
"""
# 위치 좌표 => 주소 => 지도에 마커
# cctv


# 하차 인원


