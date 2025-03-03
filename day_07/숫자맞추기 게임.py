import random

difficulty_list = ["쉬움", "보통", "어려움"]
difficulty = ""
max_try = 0
max_range = 0

while True:
    difficulty = input("난이도를 선택해 주세요. (쉬움, 보통, 어려움) : ")
    if difficulty in difficulty_list:
        break
    else:
        print("쉬움, 보통, 어려움 중에 선택해 주세요.")
        continue

if difficulty == "쉬움":
    max_try = 10
    max_range = 50
elif difficulty == "보통":
    max_try = 7
    max_range = 70
else:
    max_try = 5
    max_range = 100

correct_answer = random.randint(1, max_range) #1 ~ 100까지 랜덤 숫자 생성
try_count = 0 #시도한 횟수

print(f"숫자 맞추기 게임을 시작하겠습니다. 난이도 : {difficulty}(1 ~ {max_range})")

while try_count < max_try:
    print(f"시도 횟수 : {try_count} / {max_try}")
    input_str = input("숫자를 맞춰보세요 : ") # 문자열로 입력값을 받음
    if input_str.isdigit(): # 문자 입력 방지
        guess = int(input_str)
    else: #문자 입력시 다시 처음부터 입력받음
        print("숫자로 입력해주세요!")
        continue

    try_count += 1 #시도한 횟수 추가

    if correct_answer > guess: #만약 정답이 입력한 숫자보다 클 경우
        print("UP!")
    elif correct_answer < guess: #만약 정답이 입력한 숫자보다 작을 경우
        print("DOWN!")
    else: #만약 정답일 경우
        print(f"정답입니다! {try_count}번 만에 맞추셨어요!")
        break
