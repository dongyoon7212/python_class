import random
import time

choices = ["가위", "바위", "보"]
computer_score = 0
user_score = 0

print("\n가위바위보 게임을 시작하겠습니다.\n")


user_choice = ""

while True:
    if computer_score == 5: # 컴퓨터가 5번 먼저 이겼을때
        print(f"컴퓨터 승리! 컴퓨터 - {computer_score}, 사용자 - {user_score}")
        break
    elif user_score == 5: # 사용자가 5번 먼저 이겼을때
        print(f"사용자 승리! 컴퓨터 - {computer_score}, 사용자 - {user_score}")
        break

    print("==================현재점수===================")
    print(f"컴퓨터 - {computer_score}, 사용자 - {user_score}") # 매 라운드 마다 현재 점수 출력
    print("==========================================\n")
    computer_choice = random.choice(choices) # 랜덤으로 컴퓨터의 선택

    user_choice = input("가위, 바위, 보 중 선택해 주세요.(그만하려면 종료를 입력해주세요) : ") #선택 입력받기
    if user_choice == "종료": # 만약 종료를 입력했을때
        print("===================종료====================")
        print(f"컴퓨터 점수:{computer_score}, 사용자 점수:{user_score}")
        print("==========================================\n")
        break

    if user_choice not in choices and user_choice != "종료": # 만약 선택이 잘못되었을때(선택 유효성 검사)
        print("가위, 바위, 보 또는 종료 중 하나 선택해야 합니다.\n")
        continue

    print("\n과연 승부는......?")
    time.sleep(2) # 2초 지연
    if computer_choice == user_choice: #컴퓨터의 선택과 사용자의 선택이 같을때
        print("\n무승부 하셨습니다.")
        continue
    elif (computer_choice == "가위" and user_choice == "바위") or \
        (computer_choice == "바위" and user_choice == "보") or \
        (computer_choice == "보" and user_choice == "가위"): # 사용자가 이기는 경우
        # (computer_choice == "가위" and user_choice == "바위") or (computer_choice == "바위" and user_choice == "보") or (computer_choice == "보" and user_choice == "가위"):
        print(f"\n이겼습니다!")
        user_score += 1
        continue
    else: #나머지 컴퓨터가 이기는 경우
        print("\n졌습니다ㅜㅜ")
        computer_score += 1
        continue
