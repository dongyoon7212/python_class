
"""

변수

 => 어떠한 값들을 상자에 담아 이름을 붙이는 것

변수를 왜 써야하는가?
예를 들어 아주 긴 이름이 있는데 매번 쓰기엔 효율적이지 않음
-코드의 재사용성
-가독성

변수를 선언해놓고 여러번 반복해서 사용하거나 예약어에 사용

~~

변수에 이름 짓는 법

*****스네이크 표기법*****
-주로 python에서 쓰임
last_name = "이"

카멜 표기법 (단봉낙타표기법)
-주로 Java에서 쓰임
lastName = "이"

파스칼 표기법 (쌍봉낙타표기법)
-주로 Java에서 쓰임
LastName = "이"
"""

"""
규칙
1. 변수의 첫 글자는 숫자가 될 수 없다
ex) 1_class = "setting" X
=> first_class = "setting" O
2. _를 제외한 특수문자는 사용할 수 없다.
ex) my_@mail = "~~@naver.com" X
3. 파이썬 예약어는 사용할 수 없다.
ex) if = "~~"
=> if_condition = "~~"
4. 누가봐도 어떤 값을 가지고 있는지 알 수 있도록


"""

#변수 선언 + 문자열

last_name = "이" #문자열
first_name = '동윤' #쌍따옴표 따옴표 둘 중 하나 사용
name = last_name + first_name #문자열과 문자열은 더할 수 있다.
#a = name - last_name #문자열에서 뺄셈은 할 수 없다.
#print(name * 3) #문자열을 곱해서 여러번 출력할 수 있다. 단 나누기는 안됨

# 여러줄로 문자열을 쓸때
str1 = """
안녕하세요
반가워요
"""
str2 = '''
안녕하세요
반가워요
'''

long_str = "안녕하세요\n반갑습니다." #\t

# 문자열에 쌍따옴표나 따옴표를 포함시킬때
str3 = "\"안녕하세요\""
str4 = "동윤's class"
str5 = '"안녕하세용"'


#숫자열 정수 실수
age = 27 #int
phone_numeber = "01094027212" #숫자는 맨 앞이 0이 나올 수 없음
height = 173.4 #float

#num1 = 10
#num2 = 30

#print(f"num1 + num2 = {num1 + num2}") #덧셈
#print("num1 + num2 = ",num1 + num2)
#print(f"num2 - num1 = {num2 - num1}") #뺄셈
#print(f"num1 * num2 = {num1 * num2}") #곱셈
#print(f"num2 / num1 = {num2 / num1}") #나눗셈 (실수 몫)
#print(f"num2 % num1 = {num2 % num1}") #나머지
#print(f"num2 // num1 = {num2 // num1}") #나눗셈 (정수 몫)

print(int(1.9)) # 1
print(int(True)) # 1
print(int(False)) # 0
print(int('100')) # 100

num1 = 2.1
num2 = 4.2
print(f"num1 + num2 = {num1 + num2}") #덧셈
#print("num1 + num2 = ",num1+num2)
#print(f"num2 - num1 = {num2 - num1}") #뺄셈
#print(f"num1 * num2 = {num1 * num2}") #곱셈
#print(f"num2 / num1 = {num2 / num1}") #나눗셈 (실수 몫)
#print(f"num2 % num1 = {num2 % num1}") #나머지
#print(f"num2 // num1 = {num2 // num1}") #나눗셈 (정수 몫)

"""
결과가 딱 안맞게 떨어지는 이유
컴퓨터는 이진수만 저장을 하게 되는데 소수는 정확하게 떨어지는 이진법으로 저장 불가능
그래서 근사값을 저장하고 연산을 하게 되면서 실제의 값보다 아주 조금 더 큼
반올림(round)를 하던 decimal(하나의 모듈, 즉 소프트웨어)을 사용하던 해결
decimal은 속도가 느린대신 정확함(회계 금융 정밀연산 등 사용)
일반적인 float계산은 정확하진 않지만 속도가 빠름(머신러닝, 일반적인 계산)
0.1 + 0.2 = 0.30000000000000004
0.00011001100110011... (0.1)
+ 0.0011001100110011... (0.2)
=  0.0100110011001100... (약간의 오차 포함)
"""

print(float(1)) # 1.0
print(float(True)) # 1.0
print(float(False)) # 0.0
print(float('3.14')) # 3.14
print(float('100')) # 100.0

#복소수형?
z = 3 + 4j
print(z.imag)
print(z.real)


#불리언
"""
참과 거짓의 변수는 is 또는 has 또는 can 등 을 앞에 붙여주는게 국룰(부정문은 쓰지 않는다)
ex) is_empty = True O is_not_empty = False X
"""

is_mz = True #True / False Boolean
str = "python" #True
str = "" #False
list = [1, 2, 3] #True
list = [] #False
tuple = {} #False
dict = {} #False
num = 0 #False

print(bool(list))

#만약 변수의 타입을 알고싶다면
print(type(num))



#실습
#내 정보 출력해보기 문자열, int, float, boolean 포함
