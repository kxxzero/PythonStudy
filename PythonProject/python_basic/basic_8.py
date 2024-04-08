import python_basic
#import com.sist.dao.*
from _overlapped import NULL
from python_basic.basic_7 import Human
#import com.sist.dao.Human

class Sawon(Human):
    dept=''
    loc=''
    def __init__(self, dept, loc):
        self.dept=dept
        self.loc=loc
    # 상속 받는 메소드 재정의
    def run(self):
        print("학생이 달린다")
    def eat(self):
        print("학생이 먹는다")
