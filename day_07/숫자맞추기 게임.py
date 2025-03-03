import random

difficulty_list = ["쉬움", "보통", "어려움"] #난이도 리스트
difficulty = "" # 입력받을 난이도 변수
max_try = 0 #최대 시도 횟수
max_range = 0 #최대 숫자 범위

while True: #난이도 선택 유효성 검사
    difficulty = input("난이도를 선택해 주세요. (쉬움, 보통, 어려움) : ")
    if difficulty in difficulty_list:
        break
    else:
        print("쉬움, 보통, 어려움 중에 선택해 주세요.")
        continue

if difficulty == "쉬움": #쉬움을 택했을때 난이도 설정
    max_try = 10
    max_range = 50
elif difficulty == "보통": #보통을 택했을때 난이도 설정
    max_try = 7
    max_range = 70
else: #어려움을 택했을때 난이도 설정
    max_try = 5
    max_range = 100

correct_answer = random.randint(1, max_range) #1 ~ 최대 숫자 범위까지 랜덤 숫자 생성
try_count = 0 #시도한 횟수

print(f"숫자 맞추기 게임을 시작하겠습니다. 난이도 : {difficulty}(1 ~ {max_range}, 최대 시도 횟수-{max_try})") #난이도와 범위 출력

while True:
    print(f"시도 횟수 : {try_count} / {max_try}") # 시도 횟수 출력
    if try_count >= max_try: #시도 횟수 유효성 검사
        print("시도 횟수를 초과하였습니다!")
        print(f"정답 : {correct_answer}")
        break

    input_str = input("숫자를 맞춰보세요 : ") # 문자열로 입력값을 받음
    if input_str.isdigit(): # 숫자 입력 유효성 검사
        guess = int(input_str)
    else: #문자 입력시 다시 처음부터 입력받음
        print("숫자로 입력해주세요!")
        continue

    if guess > max_range:
        print("범위 내의 숫자를 입력해 주세요")
        continue

    try_count += 1 #시도한 횟수 추가

    if correct_answer > guess: #만약 정답이 입력한 숫자보다 클 경우
        print("UP!")
    elif correct_answer < guess: #만약 정답이 입력한 숫자보다 작을 경우
        print("DOWN!")
    else: #만약 정답일 경우
        print(f"정답입니다! {try_count}번 만에 맞추셨어요!")
        break
