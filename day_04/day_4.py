#딕셔너리

profile = {
    "name": "이동윤",
    "나이": 27,
    "취미": ["영화보기", "여행하기"],
    2: 3,
    3: [1,2,3]
}

print(profile["name"])
print(profile["취미"][0])
profile["나이"] = 28
print(profile)
profile["직업"] = "강사"
print(profile)
del profile["직업"]
print(profile)
#profile.clear() #전체삭제
#print(profile)

print(profile.keys()) #key 불러오기
key_list = list(profile.keys())
key_list.append("전화번호")
print(key_list)

print(profile.values()) #value 불러오기
value_list = list(profile.values())
value_list.append("1234")
value_list.remove("이동윤")
print(value_list)

print(profile.items()) #키값 형태 불러오기
item_list = list(profile.items())
item_list.append(("직업", "강사"))
print(item_list)

python_grade = {
    "kelly" : "B",
    "json" : "A",
    "ian" : "C",
    "elly" : "D"
}

print(sorted(python_grade.items())) #키 기준 오름차순 정렬
print(sorted(python_grade.items(), reverse=True)) #키 기준 내림차순 정렬

print(sorted(python_grade.items(), key=lambda x: x[1]))
print(sorted(python_grade.items(), key=lambda x: x[1], reverse=True))

# student = {}
# name = input("학생 이름을 입력하세요: ")
# score = int(input(f"{name}의 점수를 입력하세요: "))
# student[name] = score  # 딕셔너리에 저장
# #{'이동윤': 100}
# print(student)

#세트
fruits = {"사과", "바나나", "오렌지"}
print(fruits)
string_set = set("hello")
print(string_set)
nums = {1, 2, 2, 3, 3, 3, 4} #중복이 제거됨
print(nums)
num_list = [1, 2, 3, 3, 4, 4]
list_set = set(num_list)
print(list_set)

empty_set = set()  # 빈 세트
#빈 세트를 만들 때는 {}이 아니라 set()을 사용

s = {1, 2, 3}
s.add(4) #한개만 추가할때
print(s)

s.update([5, 6, 7]) #여러개 추가할때
print(s)

s.remove(3)  # 존재하지 않는 값 제거 시 오류 발생
s.discard(10)  # 존재하지 않는 값 제거 시 오류 없음
print(s)

s.clear()
print(s)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A | B)
print(A.union(B)) # 합집합

print(A & B)  # 출력: {4, 5}
print(A.intersection(B)) # 교집합

print(A - B)  # 출력: {1, 2, 3} (A에만 있는 요소)
print(A.difference(B)) # 차집합


color_str_set = {"b", "l", "u", "e"}
print(color_str_set.pop())
print(color_str_set)

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common = set(list1) & set(list2) #공통요소찾기
print(common)