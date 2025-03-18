import math

#올림
print(math.ceil(3.14))

#두 번째 인자의 부호만 취해 첫 번째 인자에 적용
print(math.copysign(3.14, -1))

#절댓값 반환
print(math.fabs(-3.14))

#팩토리얼
print(math.factorial(7))

#내림
print(math.floor(3.78))

#두 수의 최대공약수
print(math.gcd(6, 8))

#정수부분, 소수부분 분리
print(math.modf(3.14))

#0으로 향하는 내림
print(math.trunc(-3.14))
print(math.floor(-3.14))

#log(a, b) b를 밑으로 하는 log a에 대한 로그 값
print(math.log(10, 10))

#원주율
print(math.pi)

import random

#난수
print(random.random())

#randrange
print(random.randrange(1, 100, 2)) #끝값 미포함, step이 존재함
print(random.randint(1, 100)) #양쪽 끝값 포함, step옵션 없음

#suffle
abc = ['a', 'b', 'c', 'd', 'e']
random.shuffle(abc)
print(abc)

#choice
print(random.choice(abc))

menu = '쫄면', '육계장', '비빔밥'
print(random.choice(menu))

from datetime import datetime, timedelta

#현재날짜
now = datetime.now()
print(now)  # 현재 날짜 및 시간

#7일 후 날짜
one_week_later = now + timedelta(days=7)
print(one_week_later)  # 7일 후 날짜

#날짜 형식지정
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)  # 날짜 형식 지정

import os

print(os.getcwd())  # 현재 디렉토리
print(os.listdir())  # 현재 폴더의 파일 목록

if not os.path.exists("new_folder"): #파일 또는 폴더 존재 여부
    os.mkdir("new_folder")  # 새 폴더 만들기

import re

pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
email = "test@example.com"

if re.match(pattern, email):
    print("올바른 이메일 주소입니다.")
else:
    print("잘못된 이메일 주소입니다.")

pattern = r"^010-\d{4}-\d{4}$"
phone = "010-1234-5678"

if re.match(pattern, phone):
    print("올바른 전화번호입니다.")
else:
    print("잘못된 전화번호입니다.")

pattern = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
password = "pass1234"

if re.match(pattern, password):
    print("올바른 비밀번호입니다.")
else:
    print("비밀번호는 영문과 숫자를 포함해 8자 이상이어야 합니다.")