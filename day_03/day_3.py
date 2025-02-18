# 컬렉션

#List
# 리스트 생성
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed_list = ["안녕하세요", 42, 3.14, "Python", 100]

# 요소 접근 (인덱싱)
print(fruits[0])  # apple
print(numbers[-1])  # 5

# 요소 변경
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry']

# 리스트에 요소 추가
fruits.append("grape")  # 마지막에 추가
fruits.insert(1, "mango")  # 특정 위치에 추가
print(fruits)  # ['apple', 'mango', 'blueberry', 'cherry', 'grape']

# 요소 삭제
fruits.remove("cherry")  # 특정 값 삭제
del fruits[0]  # 특정 인덱스 삭제
print(fruits)

# 리스트 슬라이싱
print(numbers[1:4])  # [2, 3, 4]
print(numbers[::-1])  # [5, 4, 3, 2, 1] (역순)


#Tuple
# 튜플 생성
colors = ("red", "green", "blue")
single_tuple = ("hello",)  # 요소가 1개일 때는 꼭 `,`를 붙여야 함

# 요소 접근
print(colors[1])  # green

# 요소 변경 불가
# colors[0] = "yellow"  # 오류 발생!

# 튜플 슬라이싱
print(colors[:2])  # ('red', 'green')
print(colors[::2]) # ('red', 'blue')
print(colors[::-1]) # ('blue', 'green', 'red')

# 튜플 언패킹 (각 변수에 값 할당)
a, b, c = colors
print(a, b, c)  # red green blue
