# 컬렉션

#List
# 리스트 생성
fruits = ["apple", "banana", "cherry"] # 문자열 리스트
numbers = [1, 2, 3, 4, 5] # 숫자 리스트
bools = [True, False, True] # 불리언 리스트
mixed_list = ["안녕하세요", 42, 3.14, "Python", 100] # 혼합 사용가능

# 요소 접근 (인덱싱)
print(fruits[0])  # apple
print(fruits[0][1]) # p 해당 리스트 인덱스 값의 인덱스도 가능
print(numbers[-1])  # 5

# 요소 변경
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry']

# 리스트에 요소 추가
fruits.append("grape")  # 마지막에 추가
fruits.insert(1, "mango")  # 특정 위치에 추가
print(fruits)  # ['apple', 'mango', 'blueberry', 'cherry', 'grape']

# 리스트 더하기
list1 = ["A", "B", "C"]
list2 = ["D", "E"]
print(list1 + list2)

# 리스트 곱하기
print(list1 * 3)

# 리스트에 여러요소 추가
list1.extend(list2)
print(list1)

# 요소 삭제
fruits.remove("cherry")  # 특정 값 삭제
fruits.pop() # 특정 인덱스로 삭제, 인덱스 생략시 마지막 요소 삭제
del fruits[2] # 특정 인덱스로 삭제
print(fruits)

# 리스트 길이 확인
print(len(fruits))

# 리스트 슬라이싱
print(numbers[1:4])  # [2, 3, 4]
print(numbers[::-1])  # [5, 4, 3, 2, 1] (역순)

# 리스트 정렬
numbers.sort() # 기본적으로 오름차순으로 정렬
numbers.sort(reverse=True) # 내림차순 정렬
list1.sort(reverse=True) # 문자열도 가능
ko = ["가", "나", "다"]
ko.sort(reverse=True) # 한글도 ㅇㅋ
print(ko)

numbers2 = sorted(numbers) # 원본 변수는 영향 X 새롭게 변수 할당

numbers.reverse() # 요소 순서 반전

#요소 존재 체크
print("apple" in fruits) #True / False ====== not in 도 가능

#리스트 요소 이어 붙이기
result = "-".join(list1)
print(result)

# 리스트 실습
# cart = []
#
# cart.append(input("추가할 상품: "))
# cart.append(input("추가할 상품: "))
# cart.append(input("추가할 상품: "))
#
# print("\n🛒 장바구니 목록:")
# print(cart)
#
# foods = ["피자", "햄버거", "초밥", "파스타", "치킨"]
#
# print("📌 좋아하는 음식 리스트:", foods)
# index = int(input("몇 번째 음식을 선택할까요? (1~5): ")) - 1  # 사용자 입력을 리스트 인덱스로 변환
#
# print(f"🍽 선택한 음식: {foods[index]}")



#Tuple
# 튜플 생성
colors = ("red", "green", "blue")
numbers = (1, 2, 3, 5, 9)
mixed = ("pink", 1, True)
alphabet = ("a", "a", "b", "c", "c", "d")
single_tuple = ("hello",)  # 요소가 1개일 때는 꼭 `,`를 붙여야 함

# 요소 접근
print(colors[1])  # green

# 요소 변경 불가
# colors[0] = "yellow"  # 오류 발생!

# 튜플 슬라이싱
print(colors[:2])  # ('red', 'green')
print(colors[::2]) # ('red', 'blue')
print(colors[::-1]) # ('blue', 'green', 'red')

# 튜플 count
print(alphabet.count("a"))

# 튜플 index
print(alphabet.index("b"))

# 튜플 언패킹 (각 변수에 값 할당)
a, b, c = colors
print(a, b, c)  # red green blue

#test