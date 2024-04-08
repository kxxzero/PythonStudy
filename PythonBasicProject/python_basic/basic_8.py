"""
문자열 / 리스트(배열) / for...
    문자열
        1) 대소문자 변환
            - upper() : 대문자 변환
            - lower() : 소문자 변환
        2) 공백 제거
            - rstrip() : 오른쪽 공백 제거
            - lstrip() : 왼쪽 공백 제거
            - strip() : 좌우 공백 제거
        3) 대소문자 반대로 변환
            - swapcase()
        4) 문자 길이
            - len()
        5) 시작 문자
            - startswith()
        6) 첫번째 나오는 문자의 위치
            - find()
        7) 지정된 문자의 개수
            - count()
        8) 문자 분리
            - split()
        9) 문자 위치
            - index()
    -------------------------
    배열([]) : List 구조
        예) 숫자
            nums=[1,2,3,4,5...]
            names=["홍길동","심청이","박문수"...]

        1) 마지막 추가
            - append()
        2) 지정한 위치에 추가
            - insert(번호, 값)
        3) 마지막에 여러 개 추가
            - extend()
        4) 데이터 삭제
            - remove()
"""

# 문자열
data=" Hello Python"
print(data)
print(data.upper())
print(data.lower())

# 문자 길이
print(len(data))

# 공백 제거
print(data.rstrip())
print(data.lstrip())
print(data.strip())

print(data.swapcase()) # 대문자 => 소문자 / 소문자 => 대문자
print(data.startswith(" H")) # " H"로 시작하는 데이터가 있는지 확인
print(data.find("l")) # 앞에서부터 "l"의 위치값 확인
print(data.count("o")) # "o" 문자의 개수
print(data.split(" ")) # 공백을 기준으로 문자열을 잘라서 배열 리턴
print(data.index("e")) # "e"의 인덱스 값 위치 확인

# 배열
names=["홍길동", "심청이", "이순신", "춘향이", "박문수"]
print(names)
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print("==========")

#for-each
for name in names:
    print(name)

print("===== 데이터 추가 =====")
names.append("강감찬")
for name in names:
    print(name)

print("===== 지정된 위치에 추가 =====")
names.insert(1, '김두한')
for name in names:
    print(name)

print("===== 마지막에 여러 개 동시 추가 =====")
names.extend(["김유신","을지문덕"])
for name in names:
    print(name)

print("===== 데이터 삭제 =====")
names.remove("을지문덕")
for name in names:
    print(name)

print("===== 데이터 정렬(ASC) =====")
names.sort() # reverse=False => 생략 가능
for name in names:
    print(name)

print("===== 데이터 정렬(DESC) =====")
names.sort(reverse=True)
for name in names:
    print(name)

"""
함수 / 데이터베이스
"""