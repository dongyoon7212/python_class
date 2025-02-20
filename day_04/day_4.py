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

#items() --- -