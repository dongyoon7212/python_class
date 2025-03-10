import random
import json


def review():
    with open("review_note.json", "r", encoding="utf-8") as review_file:
        word_list = list(json.load(review_file))

    incorrect_count = 0
    for i in range(0, len(word_list)):
        print("=============================")
        print(f"{word_list[i]["meaning"]}")
        input_eng = input("영어 : ")
        if input_eng == word_list[i]["word"]:
            print("정답입니다.")
        elif input_eng != word_list[i]["word"]:
            print("오답입니다.")
            print(f"정답 : {word_list[i]["word"]}")
            incorrect_count += 1

    if incorrect_count == 0:
        print("오답 노트 단어를 모두 맞췄습니다!")


def study(level):
    review_list = []

    with open("words.json", "r", encoding="utf-8") as file:
        word_list = list(json.load(file))
        filtered_word_list = list(filter(lambda x: x["level"] == level, word_list))

        count = 0
        while count < 10:
            select_no = random.randint(0, len(filtered_word_list) - 1)

            print("=============================")
            print(f"{filtered_word_list[select_no]["meaning"]}")
            input_eng = input("영어 : ")
            if input_eng == filtered_word_list[select_no]["word"]:
                print("정답입니다.")
            elif input_eng != filtered_word_list[select_no]["word"]:
                print("오답입니다.")
                print(f"정답 : {filtered_word_list[select_no]["word"]}")
                review_list.append(filtered_word_list[select_no])

            count += 1

        with open("review_note.json", 'w') as review_file:
            json.dump(review_list, review_file, indent=4, ensure_ascii=False)

while True:
    print("\n===== 📜 레벨 =====")
    print("""
        1. 초등
        2. 중고
        3. 전문
        4. 오답노트
        """)

    choice = input("레벨을 선택하세요: ")
    if choice == "1":
        study("초등")
    elif choice == "2":
        study("중고")
    elif choice == "3":
        study("전문")
    elif choice == "4":
        review()
    else:
        print("다시 선택해 주세요.")
        continue


