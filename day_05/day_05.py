#대입연산자
x = 10
x += 5   # x = x + 5 (15)
x *= 2   # x = x * 2 (30)
#x /= 5   # x = x / 5 (6.0)
x //= 5   # x = x // 5 (6)
print(x)

#비교연산자
x = 10
y = 20
z = 10
print(x == z) #True
print(x < y)  #True
print(x == y) #False
print(x != y) #True
print(x <= y) #True
print(x >= z) #True

#논리연산자
a = True
b = False
print(not a and b)  # False
print(a or b)   # True
print(not a)    # False

#조건연산자
a = 10
b = 20

max_value = a if a > b else b
print(max_value)  # 20

#여러개 조건
score = 85
grade = "A" if score >= 90 else ("B" if score >= 80 else "C")
print(grade)  # B

#홄수 판별
num = 7
result = "짝수" if num % 2 == 0 else "홀수"
print(result)  # 홀수

#일반 조건과 비교
if a > b:
    max_value = a
elif a<b :
    print(a)
else:
    max_value = b

max_value = a if a > b else b