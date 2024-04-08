class Human:
    name=''
    sex=''
    age=0
    def __init__(self, name, sex, age):
        self.name=name
        self.sex=sex
        self.age=age
    def run(self):
        pass
    def eat(self):
        pass

class Student(Human):
    school=''
    subject=''
    def __init__(self, school, subject):
        self.school=school
        self.subject=subject
        #오버라이딩
        """
            상속 조건
            메소드명이 동일
            매개변수가 동일
            리턴형 동일
        """
        def run(self):
            print("달린다")
        def eat(self):
            print("먹는다")

std=Student('SIST', '파이썬')
std.name='홍길동'
std.age=20
std.sex='남자'
print(f"이름:{std.name}")
print(f"나이:{std.age}")
print(f"성별:{std.sex}")