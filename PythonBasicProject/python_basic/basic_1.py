"""

파이썬 자료형
    = 정수 : int
    = 실수 : float
    = 문자형 : string
    = 논리형 : bool
    = 집합 자료형
        - 리스트형 : 중복 허용, 값 변경 가능 => [] (자바의 ArrayList와 같은 역할)
        - 튜플형 : 데이터베이스 출력, 중복 허용, 한 번 지정한 값은 변경 불가 => ()
        - 셀형 : 중복 불가 => {} => Set
        - 딕트형 :  key+value => Map

파이썬 : 함수 지향 언어 + 객체 지향 언어
    = 함수 지향 언어 => def 함수명:
    = 객체 지향 언어
    
    *** 주의점 : 들여쓰기 필수
             
    
    1. 변수 : 데이터 저장 => 데이터형이 없음
        예) a=10

    2.
        데이터 저장 ==========> 데이터 처리 ==========> 데이터 출력
                            연산자, 제어문
                           (모듈화 => 함수)
                           
    3. 변수 변경 가능 => RAM(휘발성) => 프로그램 종료 시 자동 삭제
        => 파이썬에서 변수는 저장값 자체를 기억하지 않고 객체 주소를 기억함
            예) class 'int' class str class 'bool' =>  형변환 함수 
                => 모든 변수가 참조형 기억 주소로 되어 있음
                
    4. 식별자
        1) 알파벳으로 시작(한글도 가능하나 권장하지 않음)
        2) 대소문자 구분
        3) 숫자 사용 가능(맨 앞 사용 금지)
        4) 키워드는 사용 할 수 없음(import, if, else 등...)
    
    5. 변수 선언 => 변수명=값
        예) a=10
        b='hello' => string "",''
        c=True => True/False
        d=10.5 => float
        --------------------type(변수명)

    6. 입출력
        print() / input()

"""

# 변수 선언과 출력 => 데이터형 확인

age=30
name='홍길동'
height=180.20
data=False

print(age)
print(type(age))
print(name)
print(type(name))
print(height)
print(type(height))
print(data)
print(type(data))

# 배열형
print([1,2,3])

