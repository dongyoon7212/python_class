# 내장함수

#abs()
#숫자의 절댓값을 리턴하는 함수
print(abs(3))
print(abs(-3))
print(abs(-1.2))

#all()
#all(x)는 반복 가능한 데이터 x를 입력값으로 받으며 이 x의 요소가 모두 참이면 True, 거짓이 하나라도 있으면 False를 리턴
num_list = [1, 2, 3, 4]
print(all(num_list))
num_list = [1, 2, 0 ,4]
print(all(num_list))
num_list = []
print(all(num_list))

#any()
#any(x)는 반복 가능한 데이터 x를 입력으로 받아 x의 요소 중 하나라도 참이 있으면 True를 리턴하고 x가 모두 거짓일 때만 False를 리턴
#all(x)의 반대로 작동
num_list = [1, 2, 3, 4]
print(any(num_list))
num_list = [1, 2, 0 ,4]
print(any(num_list))
num_list = [0, 0, 0 ,0]
print(any(num_list))
num_list = []
print(any(num_list))

#chr()
#chr(i)는 유니코드 숫자 값을 입력받아 그 코드에 해당하는 문자를 리턴
print(chr(97))
print(chr(44032))

#dir()
#객체가 지닌 변수나 함수를 보여 주는 함수
name = "python"
print(dir(name))
num_list = [1, 2, 3, 4]
print(dir(num_list))

#divmod()
#2개의 숫자 a, b를 입력으로 받는다. 그리고 a를 b로 나눈 몫과 나머지를 튜플로 리턴
print(divmod(7, 3))
#(몫, 나머지)

#enumerate()
#순서가 있는 데이터(리스트, 튜플, 문자열)를 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴
for i, name in enumerate(['name', 'age', 'birth']):
    print(i, name)

#eval()
#문자열로 구성된 표현식을 입력으로 받아 해당 문자열을 실행한 결괏값을 리턴하는 함수
print(eval('1+2'))
print(eval('divmod(4, 3)'))

#filter()
#첫 번째 인수로 함수, 두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 데이터를 받는다.
#그리고 반복 가능한 데이터의 요소 순서대로 함수를 호출했을 때 리턴값이 참인 것만 묶어서(걸러 내서) 리턴
def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

#hex(234)
#정수를 입력받아 16진수(hexadecimal) 문자열로 변환하여 리턴하는 함수
print(hex(234))
print(hex(3))

#id()
#객체를 입력받아 객체의 고유 주솟값(레퍼런스)을 리턴하는 함수
a = 3
print(id(3))
b = a
print(id(b))

#map()
#map은 입력받은 데이터의 각 요소에 함수 f를 적용한 결과를 리턴하는 함수
def two_times(x):
    return x*2

print(list(map(two_times, [1, 2, 3, 4])))

#max()
#max(iterable)은 인수로 반복 가능한 데이터를 입력받아 그 최댓값을 리턴하는 함수
print(max([1, 2, 3]))

#min()
#min(iterable)은 max 함수와 반대로, 인수로 반복 가능한 데이터를 입력받아 그 최솟값을 리턴하는 함수
print(min([1, 2, 3]))

#oct()
#oct(x)는 정수를 8진수 문자열로 바꾸어 리턴하는 함수
print(oct(34))
print(oct(12345))

#open()
#open(filename, [mode])은 ‘파일 이름’과 ‘읽기 방법’을 입력받아 파일 객체를 리턴하는 함수이다.
# 읽기 방법(mode)을 생략하면 기본값인 읽기 모드(r)로 파일 객체를 만들어 리턴
# w	쓰기 모드로 파일 열기
# r	읽기 모드로 파일 열기
# a	추가 모드로 파일 열기
# b	바이너리 모드로 파일 열기
file = open("example.txt", "r", encoding="utf-8")
content = file.read()
print(content)
file.close()

with open("example.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

#ord()
#ord(c)는 문자의 유니코드 숫자 값을 리턴하는 함수
print(ord('a'))
print(ord('가'))

#pow()
#pow(x, y)는 x를 y제곱한 결괏값을 리턴하는 함수
print(pow(2, 4))
print(pow(3, 3))

#range()
#range([start,] stop [,step])은 for 문과 함께 자주 사용하는 함수이다.
# 이 함수는 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 리턴
print(list(range(5)))
print(list(range(5, 10)))
print(list(range(1, 10, 2)))
print(list(range(0, -10, -1)))

#round()
#숫자를 입력받아 반올림해 리턴하는 함수
print(round(4.6))
print(round(4.2))
print(round(5.678, 2))

#sum()
#sum(iterable)은 입력 데이터의 합을 리턴하는 함수
print(sum([1,2,3]))
print(sum((4,5,6)))

#zip()
#zip(*iterable)은 동일한 개수로 이루어진 데이터들을 묶어서 리턴하는 함수
print(list(zip([1, 2, 3], [4, 5, 6])))
print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])))
print(list(zip("abc", "def")))

#메소드
num_list = [1, 2, 3, 4]
print(num_list.index(3)) #index
print(num_list.count(2)) #count
name = "이동윤"
