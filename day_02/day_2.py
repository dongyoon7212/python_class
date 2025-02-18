#기본 입출력

#입력받기
# a = input()
# print("내가 입력한 것 :",a)
# b = input("입력해주세요. :")
# print(b)
print("======================================================")

"""
input()으로 입력받은 모든것은 str취급된다.
"""

#출력하기 다양한 방법
last_name = "이" #문자열
first_name = '동윤' #쌍따옴표 따옴표 둘 중 하나 사용
name = last_name + first_name #문자열과 문자열은 더할 수 있다.
age = 27 #int
phone_numeber = "01094027212" #숫자는 맨 앞이 0이 나올 수 없음

print('hi ' + 'hello ' + 'world')
print("hi", "hello", "world") #쉼표에 띄어쓰기가 포함되어있다.
print("내 전화번호는 " + phone_numeber + " 입니다.") #기본적인 출력
#print("제 나이는 " + age + "입니다.") #변수의 타입을 알고 싶을때 type(변수명)
#그럼 어떻게 해야할까?
print("제 나이는 {} 입니다.".format(age)) #옛날 방식
print("제 이름은 {}, 나이는 {} 입니다.".format(name, age))
print("제 이름은 {nm}, 나이는 {ag} 입니다.".format(nm="홍길동", ag=18))
print(f"제 나이는 {age} 입니다.") #f-string이라는 방식
print("제 나이는 %s 입니다." % age) #모든 문자를 문자열로 포맷팅해서 출력
print("제 나이는 %d 입니다." % age) #모든 숫자를 정수형으로 포맷팅해서 출력
print("제 이름은 %s 이고, 나이는 %d 입니다." % (name, age)) #두가지 이상 동시 가능
print("Error is %d%%." % 98) # %기호를 쓰려면 두번써야한다
print("%10s" % "hi") # 문자열 왼쪽 공백 10
print("%-10sHello" % "hi") # 문자열 오른쪽 공백 10
print("%0.4f" % 3.42134234) #앞 0은 자리수를 의미, .4는 소수점 4번째 자리까지 표현
print("%10.4f" % 3.42134234) #10은 자리수를 의미하므로 소수점 4번째 자리까지 표현후 남는 자리만큼 앞에 공백

print("======================================================")
"""
%s	문자열(String)
%c	문자 1개(character)
%d	정수(Integer)
%f	부동소수(floating-point)
%o	8진수
%x	16진수
%%	Literal % (문자 % 자체)
"""

#실습
#본인의 정보를 입력받고 마지막에 출력해보기
# name = input("이름 :")
# age = input("나이 :")
# hobby = input("취미 :")
# address = input("주소 :")

#print(f"제 이름은 {name}이고 나이는 {age}살 입니다. 제 취미는 {hobby}입니다. 그리고 주소는 {address}입니다.")

#문자열의 슬라이싱, 인덱싱
a = "Life is too short, You need Python"

print("======================================================")

#인덱싱
print(a[3]) #네 번째 e
#인덱스는 0부터 센다
print(a[-1]) #-는 거꾸로 n
print(a[-0]) #0은 음수여도 0이다 L

b = a[0] + a[1] + a[2] + a[3]
print(b) #Life

#실습
#단어를 입력받고 첫번째 글자와 마지막 글자를 출력하시오
# word = input("단어를 입력하세요 : ")
# print("첫번째 글자 -", word[0])
# print("마지막 글자 -", word[-1])
print("======================================================")

#슬라이싱
#a[시작번호:끝번호:스텝(간격)]
# 슬라이싱한다고 원본에 영향을 주진 않음
print(a[0:4]) #끝번호는 포함 하지 않는다(끝번호 -1) #Life
print(a[0:3]) #Lif
print(a[0:2]) #Li
print(a[5:7]) #is
print(a[12:17]) #short
print(a[19:]) #끝번호를 생략하면 끝까지 출력 #You need Python
print(a[:17]) #시작번호를 생략하면 처음부터 출력 #Life is too short
print(a[19:-7]) #19에서 -8까지를 의미 -7은 포함 하지 않는다. You need
print(a[::2]) #Lf stosot o edPto
print(a[::-1]) #문자열 뒤집기 #nohtyP deen uoY ,trohs oot si efiL
print("======================================================")

#실습
date = "20250218Rainy"
date1 = "20240824Cloudy"
print("년도 :", date1[0:4])
print("월일 :", date1[4:8])
print("날씨 :", date1[8:])

# text = input("문장을 입력하세요: ")
#
# print("앞 3글자:", text[:3])
# print("뒤 3글자:", text[-3:])
# print("거꾸로 출력:", text[::-1])


#각종 문자열 함수
a = "Life is too short, You need Python"
print(len(a)) #문자열의 길이 34
print(a.count("t")) #특정문자가 몇개 있는지 3개
print(a.index("t")) #특정문자의 인덱스 찾기 8
print(a.index("t", 10, 18)) #특정문자, 시작인덱스, 끝인덱스
print(a.find("t")) #특정문자의 인덱스 찾기 8
print(a.find("t", 10, 18)) #특정문자, 시작인덱스, 끝인덱스
"""
그럼 index랑 find의 차이점
index는 해당 문자가 없으면 오류를 발생
find는 -1을 출력

find는 문자열(str)에만 사용가능
index는 문자열(str), 리스트(list), 튜플(tuple)에서만 사용가능
"""


print(",".join(a)) #문자 합치기 사이에 콤마 추가해서
print(",".join(["a","b","c","d"]))
print(a.upper()) #대문자로
print(a.lower()) #소문자로
#값의 변경이 아닌 리턴이므로 주의하자!!!
print(a[0].isupper()) #대문자여부
print(a[2].islower()) #소문자여부

b = "      hi    "
print(b.lstrip()) #왼쪽 공백제거
print(b.rstrip()) #오른쪽 공백제거
print(b.strip()) #양쪽 공백제거
print(a.replace("short", "long"))
print(a.replace(" ", ""))
print(a.split()) #아무것도 넣지 않으면 공백, 탭, 엔터 기준으로 나눠버린다.
c = "a:b:c:d"
print(c.split(":"))


#실습
email = input("이메일을 입력하세요: ")  # example@gmail.com
user_id = email[:email.index("@")]
print("이메일 아이디:", user_id)

ssn = input("주민등록번호를 입력하세요 (예: 990101-1234567): ")
masked_ssn = ssn[:8] + "******"
print("가려진 주민등록번호:", masked_ssn)