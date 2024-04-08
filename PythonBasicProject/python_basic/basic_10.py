"""
변수 / 연산자 / 제어문 / 배열
------------------------- 함수
변수 :
    변수명=값 => 값에 따라서 자동 지정
    문자열 => "", ''
    숫자 => 1-, 10.5
    bool => True, False

연산자 :
    산술 => +, -, *, /(무조건 실수값), %, //(몫), **(제곱근)
    비교 => == ,!=, <, >, <=, >=
    논리 => and, or, not
    대입 => +=, -= => 증감 연산자는 존재하지 않음

제어문 : 들여쓰기 매우 중요(괄호 없음)
    if문
        if 조건문:
            처리 문장

    if~else문
        if 조건문 :
            처리 문장
        else:
            처리 문장
            
    if~elif~elif~else문
        if 조건문 :
            처리 문장
        elif 조건문 :
            처리 문장
        elif 조건문 :
            처리 문장
        else :
            처리 문장

반복문 :
    while
        초기값
        while 조건문:
            반복 처리 문장
            증가식

    for
        for 변수 in 리스트:
            처리 문장
        for 변수 in range(시작 번호, 끝 번호): => 마지막은 제외
            처리 문장


<< 함수  / 클래스 >>

함수 (= 자바의 메소드)
    = 1개의 기능을 수행
    = 명령문을 모아서 처리(재사용 목적)
        => 변수 선언 / 제어문 처리 / 연산 처리
    = 사용자 정의 함수 / 라이브러리(이미 제작된 소스를 불러와서 사용)
        형식) def func(매개변수...): // 자바(void)
                처리 문장

    ------------------------------
        결과값         사용자 요청
       (리턴형)        (매개변수)
    ------------------------------
          O              O
        => 형식)
            def 함수명(매개변수...):
                처리 문장
                return 값
    ------------------------------
          O              X
        => 형식)
            def 함수명():
                처리 문장
                return 값
    ------------------------------
          X              O
        => 형식)
            def 함수명(매개변수...):
                처리 문장
    ------------------------------
          X              X
        => 형식)
            def 함수명():
                처리 문장
    ------------------------------

    매개변수 :
    = default 변수 => 매개변수는 나중에 설정
        예)
        def 함수명(매개변수=10, 매개변수=20, 매개변수=30): # default값을 지정한 매개 변수
            처리 문장
            print("", end="\n")
    = 가변 매개변수
        예)
        def 함수명(*args):
                 ---> 포인터
            => 함수명(1)
            => 함수명(1,2)
            => 함수명 (1,2,3...)
"""

# 같은 이름의 함수명이 많이 존재할 때 아래와 같은 형식으로 호출
from random import randrange

# 리턴형 x, 매개변수 x 함수
def gugudan():
    for i in range(1, 10):
        for j in range(1, 10):
            print(f"{j}*{i}={j*i}", end="\t")
            print('') # 다음줄로 넘김)

gugudan()


def sort():
    data=[30,40,10,50,20]
    print(f"변경 전:{data}")
    print("===== 이중 for문으로 정렬 =====")
    for i in range(len(data)-1):
        for j in range(i, len(data)):
            if data[i]>data[j]:
                temp=data[i]
                data[i]=data[j]
                data[j]=temp
    print(data)
sort()


print("===== sort ASC 정렬 =====")
data=[30,40,10,50,20]
data.sort()
print(data)

print("===== sort DESC 정렬 =====")
data.sort(reverse=True)
print(data)


def gugudan2(dan):
    for i in range(1,10):
        print(f"{dan}*{i}={dan*i}")

dan=(int(input("2~9까지 정수 입력:")))
gugudan2(dan)


# 리턴형 O, 매개변수 x 함수
def getName():
    return '홍길동'

name=getName()
print(f"받은 값:{name}")


# 리턴형 O, 매개변수 O 함수
def plus(a,b):
    c=a+b
    return c

a=int(input("1~100 사이의 정수 입력:"))
b=int(input("1~100 사이의 정수 입력:"))
c=plus(a,b)
print(f"결과값:{c}")


# default 매개변수
"""
    def func(a,b=10, c=20)
        처리 문장
    
    func(100,200,300) => a=100, b=200, c=300
    func(100) => a=100, b=10, c=20
    func(100,200) => a=100, b=200, c=20
    
    def func(a=10, b=20):
    func() => a=10, b=20
    func(100) => a=100, b=20
    func(100, 200) => a=100, b=200
"""

# default 매개변수의 값은 맨 앞부터가 아닌 맨 뒤에서부터 값을 지정해야 함
def func(a,b,c=100): 
    print(f"a={a}, b={b}, c={c}")

func(10,20,30)
func(100,200)



# 가변형 매개변수
def func1(*args):
    print(args)
    print(list(args)) # 배열로 변경해서 처리
    sum=0
    for i in args:
        sum+=i # 값 누적
    print(f"총합:{sum}")

func1()
func1(1,2)
func1(1,2,3,4,5)


# Tuple : ()
# List : []