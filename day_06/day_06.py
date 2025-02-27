#조건문
"""
if 조건:
    실행할 코드
"""
#if문
num = int(input("숫자를 입력하세요: "))

if num > 0:
    print("이 숫자는 양수입니다!")

num = int(input("숫자를 입력하세요: "))

#if-else문
if num > 0:
    print("이 숫자는 양수입니다!")
else:
    print("이 숫자는 0이거나 음수입니다!")


#if-elif-else문
score = int(input("시험 점수를 입력하세요: "))

if score >= 90:
    print("A 학점입니다!")
elif score >= 80:
    print("B 학점입니다!")
elif score >= 70:
    print("C 학점입니다!")
elif score >= 60:
    print("D 학점입니다!")
else:
    print("F 학점입니다! 더 노력하세요!")

#실습예제
#1.
num = int(input("숫자를 입력하세요: "))

if num % 2 == 0:
    print("짝수입니다!")
else:
    print("홀수입니다!")

#2.
age = int(input("나이를 입력하세요: "))
student = input("학생인가요? (yes/no): ")

if age >= 18 and student == "yes":
    print("당신은 성인 학생입니다!")
else:
    print("당신은 성인 학생이 아닙니다!")



#반복문(while)
"""
while 조건:
    실행할 코드
    (조건을 변경하는 코드)
"""
#예시 1번
num = 1  # 초기값 설정

while num <= 5:  # 조건이 True일 동안 반복
    print("숫자:", num)
    num += 1  # 조건을 변경하는 코드 (없으면 무한 루프!)

#예시 2번
user_input = ""

while user_input != "exit":
    user_input = input("종료하려면 'exit'을 입력하세요: ")

#break 사용하기
num = 1

while num <= 10:
    print(num)

    if num == 5:  # num이 5가 되면 반복 종료
        break

    num += 1

#continue 사용하기
num = 0

while num < 10:
    num += 1

    if num % 3 == 0:
        continue  # 3의 배수는 출력하지 않고 건너뜀

    print(num)

#while문 안에 while문
dan = 1
while dan <= 9:
    n = 1
    while n <= 9:
        print(f"{dan}x{n}={dan*n}")
        n += 1
    dan += 1

#실습문제
#1. 1부터 100까지 짝수만 출력하기
num = 2

while num <= 100:
    print(num)
    num += 2

num = 1

while num <= 100:
    if num % 2 == 0:  # 짝수인지 확인
        print(num)
    num += 1

#2. 5의 배수 출력 (30에서 멈추기)
num = 5

while num <= 50:
    print(num)

    if num == 30:  # 30에서 멈추기
        break

    num += 5

#3. 1부터 50까지 숫자 중 3의 배수 건너뛰기 (continue)
num = 0

while num < 50:
    num += 1

    if num % 3 == 0:  # 3의 배수 건너뛰기
        continue

    print(num)

#for문
"""
for 변수 in 반복할_객체:
    실행할_코드
"""
#리스트 순회
fruits = ["사과", "바나나", "체리"]

for fruit in fruits:
    print(fruit)

#딕셔너리 순회
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}

for key in scores:
    print(key, "의 점수는", scores[key])

#튜플 순회
a_tuple = ("안녕", "하세요", "반갑습니다")
for a in a_tuple:
    print(a)

#세트 순회
a_set = {"사과", "바나나", "체리", "딸기", "오렌지"}
sorted(a_set)
for a in a_set:
    print(a)

#세트 정렬 추가 설명
numbers = {3, 1, 4, 1, 5, 9, 2}
sorted_numbers = sorted(numbers)

print(sorted_numbers)  # [1, 2, 3, 4, 5, 9] (리스트로 변환되어 정렬됨)
print(type(sorted_numbers))  # <class 'list'>

words = {"banana", "apple", "cherry", "kiwi"}
sorted_words = sorted(words, key=len)

print(sorted_words)  # ['kiwi', 'apple', 'banana', 'cherry'] (길이 순 정렬)

#세트 정렬 후 반복
numbers = {5, 10, 15, 20}

for num in sorted(numbers):  # 오름차순 정렬
    print(num)

#예제2
word = "Python"

for char in word:
    print(char)

#예제3
for i in range(5):  # 0부터 4까지 미만임
    print(i)

#예제4
for i in range(2, 10, 2):  # 2부터 10 미만까지, 2씩 증가
    print(i)

#break
for num in range(1, 10):
    if num == 5:
        break  # 5가 되면 반복 종료
    print(num)

#continue
for num in range(1, 10):
    if num == 5:
        continue  # 5는 건너뛰고 계속 반복
    print(num)

#실습문제
#1.  1부터 100까지 짝수만 출력하기
for i in range(2, 101, 2):
    print(i)

#2. 리스트의 합 구하기
numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num

print("리스트의 합:", total)

#3. 구구단
for dan in range(1, 10):
    for n in range(1, 10):
        print(f"{dan}x{n}={dan*n}")

#4. 평균구하기
scores = [80, 90, 75, 88, 92]
total = 0

for score in scores:
    total += score

average = total / len(scores)
print("평균 점수:", average)


#숫자 맞추기
import random

target = random.randint(1, 100)  # 1~100 사이 랜덤 숫자 생성
attempts = []  # 시도한 숫자 저장 리스트

while True:
    guess = int(input("숫자를 맞혀보세요 (1~100): "))
    attempts.append(guess)  # 시도한 숫자 저장

    if guess < target:
        print("너무 작아요! 다시 시도하세요.")
    elif guess > target:
        print("너무 커요! 다시 시도하세요.")
    else:
        print(f"정답입니다! 정답: {target}")
        break

print("총 시도한 숫자 목록:")
for attempt in attempts:  # for문을 이용해 시도한 숫자 출력
    print(attempt, end=" ")
