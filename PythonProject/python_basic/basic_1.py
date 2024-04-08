"""
    1. import
    2. def 함수(): => class
                    ========== 객체 지향 프로그램
      ========== 함수 지향 프로그램
                 변수 선언
                 연산 처리 / 제어문 처리
                 라이브러리 함수 호출
                 
    3. 호출
    = 객체지향 프로그램(OOP)
        - 크롤링
        - CSV => 읽기/쓰기 => 공공포털
        - CSV 제어
        - Pandas => 통계(Numpy) = 시각화(marplotlib)
        - 머신 러닝
    =============== 브라우저 : React (웹 프로그램 : 장고)

    1. 객체 지향의 객체란?
    2. 구성 요소
        1) 멤버 변수 : state(상태)
        2) 멤버 메소드 : 동작, 요청 처리 => 다른 클래스와 통신(소프트웨어 : 메세지)
        3) 생성자 : 객체 생성(멤버 변수의 초기화)
        4) 소멸자 : 객체 메모리 해제 => 가비지 컬렉션
    3. 클래스 선언
        클래스명 식별자
        1) 알파벳으로 시작(대소문자 구분), _ , 한글 시작(_: 주로 임시 파일명에 사용)
        2) 숫자 사용 가능
        3) 예약어 사용 불가
    4. 재사용 기법
        1) 상속
        2) 오버로딩 / 오버라이딩
        3) 캡슐화
    5. 클래스의 종류
        1) 추상 클래스
        2) 인터페이스
    6. 예외 처리
    7. 라이브러리 사용법
        1) 크롤링
        2) IO
        3) CSV

    class Member:
        id=''
        name=''
        sex=''
        addr=''
        tel=''

"""


class Student:
    hakbun = ''
    name = ''
    kor = '0'
    eng = '0'
    math = '0'

std=Student()
#멤버변수 초기화


class Member:
    # 멤버 변수 선언 위치
    name="홍길동"
    sex="남자"
    
    # 생성자 / 소멸자 
    def __init__(self, name, sex): # self = this
        self.name=name
        self.sex=sex
        print("객체 메모리 할당: 생성자 함수")
    def __del__(self): # 소멸자 함수
        print("객체 메모리 해제: 소멸자 함수")
        
    # 사용자 정의 함수
    def memberPrint(self):
        print(f"이름:{self.name}")
        print(f"성별:{self.sex}")

name=input("이름 입력:")
sex= input("성별 입력:")
hong=Member(name, sex)

# 출력
hong.memberPrint()

# 캡슐화
class Sawon:
    def __init__(self, name, dept):
        self._name=name
        self._dept=dept
    # getter/setter
    def getName(self):
        return self._name
    def getDept(self):
        return self._dept
    def setName(self, name):
        self._name=name
    def setDept(self, dept):
        self._dept=dept
        

sawon=Sawon("홍길동", "개발부")
print(f"이름:{sawon.getName()}")
print(f"부서:{sawon.getDept()}")


"""
    1. 변수는 데이터형을 사용하지 않음 => 확인 시 type(변수명)
        = 정수형 : int => int()
        = 실수형 : float => float()
        = 문자형 : str => str()
        = 논리형 : bool => bool() => 0,0.0이 아닌 수는 True
    2. 연산자
        //, **, /(실수)
        and, or, not
        => 증감연산자(++, --)는 존재하지 않음
    3. 
        for 변수 in 리스트, 튜플
        for 변수 in range()
    4. 함수
        def 함수명():
            처리 문장
    5. 예외 처리
        try:
            처리 문장
        except Exception as e:
            오류 처리
    =========================> 클래스화
    
"""

