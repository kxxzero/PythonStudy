# if 조건문 => 들여쓰기 => 파이썬, yml
# yml => application.properties => yml
"""
    server
        port=80
    Spring Cloud => MSA
"""

import random
num=random.randrange(1,101)
if(num%2==0):
    print(f"{num}은(는) 짝수입니다.")
else:
    print(f"{num}은(는) 홀수입니다.")
    print("프로그램 종료")

# if
#
# if user==0:
#     print("사용자: 가위")
#     print("비겼다")
