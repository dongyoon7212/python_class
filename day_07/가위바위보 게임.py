import random
import time

choices = ["가위", "바위", "보"]
computer_score = 0
user_score = 0

print("\n가위바위보 게임을 시작하겠습니다.\n")


user_choice = ""

while True:
    if computer_score == 5:
        print(f"컴퓨터 승리! 컴퓨터 - {computer_score}, 사용자 - {user_score}")
        break
    elif user_score == 5:
        print(f"사용자 승리! 컴퓨터 - {computer_score}, 사용자 - {user_score}")
        break

    print("==================현재점수===================")
    print(f"컴퓨터 - {computer_score}, 사용자 - {user_score}")
    print("==========================================\n")
    computer_choice = random.choice(choices)

    user_choice = input("가위, 바위, 보 중 선택해 주세요.(그만하려면 종료를 입력해주세요) : ")
    if user_choice == "종료":
        print("===================종료====================")
        print(f"컴퓨터 점수:{computer_score}, 사용자 점수:{user_score}")
        print("==========================================\n")
        break

    if user_choice not in choices and user_choice != "종료":
        print("가위, 바위, 보 또는 종료 중 하나 선택해야 합니다.\n")
        continue

    print("\n과연 승부는......?")
    time.sleep(2)
    if computer_choice == user_choice:
        print("\n무승부 하셨습니다.")
        continue
    elif (computer_choice == "가위" and user_choice == "바위") or \
        (computer_choice == "바위" and user_choice == "보") or \
        (computer_choice == "보" and user_choice == "가위"):
        # (computer_choice == "가위" and user_choice == "바위") or (computer_choice == "바위" and user_choice == "보") or (computer_choice == "보" and user_choice == "가위"):
        print(f"\n이겼습니다!")
        user_score += 1
        continue
    else:
        print("\n졌습니다ㅜㅜ")
        computer_score += 1
        continue
