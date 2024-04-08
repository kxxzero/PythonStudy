# 변수 사용법 => 출력 형식

# 변수 선언
a=100
print(a)
print("a는 %d이다" %a)

b=10
c=20.0
d="홍길동"
print("b=%d, c=%f, d=%s" %(b,c,d))


'''
    정수 : %d
    실수 : $f
    문자열 : %s
    
'''

print("b:{}, c:{}, d:{}".format(b,c,d,))

#데이터베이스 연결
print("b는 {b}, c는 {c}, d는 {d}")
# sql=f"SELECT * FROM emp WHERE empno={empno}"

# 실제 저장된 주소
print(id(b), id(c), id(d))
# 저장된 메모리 주소 => id(), &a

#id 값이 동일한 경우 => 변수 값이 동일할 때
m=3
n=3
print(id(m), id(n))
# 변수의 값이 동일할 경우 변수의 주소 값도 동일

print(m is n)
#같은 값을 가지고 있는지 확인 is

n=10
print(m is n)

k="Hello"
print("k:%s"%k, end="Python\n")
# \n : 한 줄
# \t : tab

print("k:%s" %k, sep="-")

#입력
print("이름 입력:")
name=input()
print(name,"님 로그인 되었습니다.")


num=input()
print(f"num={num}")