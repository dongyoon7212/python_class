#사용자 함수

#기본적인 사용자 함수 정의
def func1():
    print("Hello World")

func1()
#================================================
def plus():
    a = 2
    b = 3
    print(a + b)

plus()
#================================================

#매개변수가 있는 사용자 함수 정의
def hello(name):
    print(f"안녕하세요 {name}입니다")

hello("이동윤")
#================================================
def plus(a, b):
    print(a + b)

plus(3, 5)
plus(15, 87)
plus(142, 421)
#================================================
def profile(name="게스트"): #기본값 설정
    print(f"안녕하세요 {name}님")

profile()
profile("이동윤")
#================================================
def introduce(name, age): #키워드 인수
    print(f"제 이름은 {name}이고 나이는 {age}입니다.")

introduce(name="이동윤", age=27)
#================================================

#리턴값이 있는 사용자 함수 정의
def plus(a, b):
    return a + b

result = plus(10, 20)
print(result)
#================================================
def multiple_seven(num):
    return num * 7

print(multiple_seven(4))
result = multiple_seven(7)
print(result)
#================================================
def check_divide_seven(num): #7의 배수 확인
    if num % 7 == 0:
        return True
    else:
        return False

print(check_divide_seven(7))
print(check_divide_seven(18))
print(check_divide_seven(49))
#================================================
def factorial(num): #팩토리얼
    sum = 1

    for n in range(num):
        #print(f"n : {n}")
        sum = sum * (n + 1)
        #print(f"sum : {sum}")
    return sum

print(factorial(7))
#================================================
def cal_average(scores):
    sum = 0

    for score in scores:
        sum += score

    average = sum / len(scores)

    return average

score_list_1 = [55, 70, 100]
score_list_2 = [100, 99, 88]
score_list_3 = [80, 70, 60]

print(cal_average(score_list_1))
print(cal_average(score_list_2))
print(cal_average(score_list_3))
#================================================

#콜백함수
#함수를 매개변수로 전달하여 필요할 때 호출하도록 하는 개념
#어떤 함수가 실행되는 동안 미리 정의된 다른 함수를 호출하여 실행하는 역할

def calculator(x, y, operation):
    return operation(x, y)

def plus(x, y):
    return x + y

def minus(x, y):
    return x - y

def multiple(x, y):
    return x * y

def divide(x, y):
    return x / y

plus_result = calculator(2, 3, plus)
minus_result = calculator(2, 3, minus)
multi_result = calculator(2, 3, multiple)
divide_result = calculator(2, 3, divide)

print(plus_result)
print(minus_result)
print(multi_result)
print(divide_result)

#================================================

import time

def timer(pause_second, callback):
    print("타이머가 시작됩니다.")
    print(pause_second, "초 뒤에 요청하신 함수가 호출됩니다.")

    #time.sleep(pause_second)
    callback()
    print("타이머가 종료됩니다.")

def hello():
    print("hello world")

timer(5, hello)

#================================================
#람다 함수(익명 함수)
#특정 범위 내에서만 사용되거나 호출되는 횟수가 한 번인 경우에 매우 유용
#lamda 매개변수1, 매개변수2, ...:함수 내부 코드
def add(x, y):
    return x + y

print(add(3, 5))  # 8

# 람다 함수로 변환
add_lambda = lambda x, y: x + y
print(add_lambda(3, 5))  # 8

#================================================
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))  # 모든 요소를 제곱
print(squared)  # [1, 4, 9, 16, 25]
#================================================

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # 짝수만 필터링
print(even_numbers)  # [2, 4, 6, 8, 10]
#================================================

parity = lambda x: "짝수" if x % 2 == 0 else "홀수"
print(parity(5))  # 홀수



#실습

#두 수를 입력받고 두 수의 합을 출력하시오
def add_numbers(a, b):
    return a + b

x = int(input("숫자 a:"))
y = int(input("숫자 b:"))
print(add_numbers(x, y))  # 3

#짝수인지 홀수인지 판별하는 함수를 만드시오
def is_even(n):
    return n % 2 == 0

print(is_even(4))  # True
print(is_even(7))  # False
print(is_even(0))  # True


#리스트 중 가장 큰 수를 찾는 함수를 만드시오
list_1 = [3, 1, 9, 7, 5]
list_2 = [-10, -3, -1, -20]

def find_max(lst):
    max_value = lst[0]
    for num in lst:
        if num > max_value:
            max_value = num
    return max_value

print(find_max(list_1))  # 9
print(find_max(list_2))  # -1

#3의 배수만 lamda로 골라보시오
numbers = [1, 3, 6, 9, 12, 15, 18, 21]
