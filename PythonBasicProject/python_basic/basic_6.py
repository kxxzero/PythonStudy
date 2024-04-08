"""
<반복문>

while : 반복 회수가 없는 경우
    형식) 
        초기값
        while 조건 :  => false면 종료
            실행 문장
            증가식

for : 반복 횟수가 있는 경우
    형식)
        for 받는 변수 in 범위 => for-each => list, 튜플
            실행 문장
        => for(데이터 변수:배열, 컬렉션)
"""

#while
i=1 #초기값
while i<=10:
    print(f"i={i}")
    i=i+1

print("=========================")

i=1
while i<=10:
    print("i=%d" %i)
    i+=1

print("=========================")


# <1~100 사이의 총합, 짝수합, 홀수합>
i=1
sum=odd=even=0
while i<=100:
    if i%2==0:
        even+=i
    else:
        odd+=i
    sum+=i
    i+=1
print("짝수의 합:%d" %even)
print("홀수의 합:%d" %odd)
print("전체 합:%d" %sum)


# <입력값을 받아서 구구단을 출력>
dan=int(input("2~9사이의 정수 입력:"))
i=1
while i<=9:
    print(f"{dan}*{i}={dan*i}")
    i+=1

print("=========================")


import random
com=random.randrange(1,101) # 1~101 사이의 난수 발생
print(f"난수값:{com}")


# while True: #무한루프
#     user=int(input("1~100 사이의 정수 입력:"))
#     count+=1
#     if user<1 or user>100:
#         print("잘못된 입력입니다. 1~100사이의 정수만 입력 가능")
#         continue # 다시 while의 조건문으로 이동
#     if com>user:
#         print("f{user}보다 큰 수를 입력하세요.")
#     elif

"""
    자바 : 임베디드(모바일), 웹 => flutter, react native
    
    C/C++ : 기계에 들어가는 프로그램(하드웨어)
    C# : 애플리케이션(자바 유사)
    
    Kotlin : 모바일(스프링 자바 가능)
    var a=10, val a=10
    
    fun aaa():string
    {
    }
    
    python : 데이터 수집, 통계, AI
    스칼라 : 빅데이터 분석 => 하둡, 스파크, MapReduce
    GO : 구글(자바 = 제임스 고슬링) => 운영체제가 개발
    AngularJS = VueJS
"""


for i in range(1,6):
    print('★'*i)

for i in range(1,6):
    print('★'*(6-i))


for i in range(1,6):
    print(' '*(5-i)+'★' * i)