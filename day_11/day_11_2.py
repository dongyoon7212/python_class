import requests

response = requests.get("https://www.naver.com/")
print(response.status_code)  # 200 (정상 응답)
#print(response.text)  # 페이지 일부 출력

import pandas as pd

df = pd.read_csv("data.csv")  # CSV 파일 읽기
print(df)  # 상위 5개 데이터 출력
print(df.describe())  # 데이터 요약 통계 출력

"""
count	해당 열의 데이터 개수
mean	평균값
std	표준 편차 (데이터의 분산 정도)
min	최소값
25%	1사분위(25% 지점)
50%	중앙값(50% 지점, 중위수)
75%	3사분위(75% 지점)
max	최대값
"""

print(df["Age"])  # Age 컬럼만 출력
print(df[["Age", "Salary"]])  # 여러 컬럼 선택

import matplotlib.pyplot as plt

# 연령대별 연봉 평균 그래프
# df.groupby("Age")["Salary"].mean().plot(kind="bar")
# plt.title("연령별 평균 연봉")
# plt.show()

import numpy as np

#1차원 배열
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)  # [1 2 3 4 5]
print(type(arr1))  # <class 'numpy.ndarray'>

#2차원 배열
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)

#0으로 채운 다차원 배열
zeros = np.zeros((3, 4))  # 3행 4열
print(zeros)

#1로 채운 다차원 배열
ones = np.ones((2, 3))
print(ones)

#특정한 값으로 채운 다차원 배열
filled = np.full((2, 2), 7)  # 7로 채운 2x2 배열
print(filled)

#연속된 값으로 채운 다차원 배열
arr = np.arange(1, 10, 2)  # 1부터 9까지 2씩 증가
print(arr)  # [1 3 5 7 9]

#랜덤 다차원 배열
random_int = np.random.randint(1, 100, (2, 2))  # 1~100 사이 정수 2x2 배열
print(random_int)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print(arr1 + arr2)  # [5 7 9] (덧셈)
print(arr1 - arr2)  # [-3 -3 -3] (뺄셈)
print(arr1 * arr2)  # [4 10 18] (곱셈)
print(arr1 / arr2)  # [0.25 0.4  0.5] (나눗셈)

import seaborn as sns
#
# categories = ["A", "B", "C", "D"]
# values = [3, 7, 1, 8]
#
# plt.bar(categories, values, color=["red", "blue", "green", "purple"])
# plt.title("Bar Chart Example")
# plt.show()

# x = np.random.rand(50)
# y = np.random.rand(50)
#
# plt.scatter(x, y, color="r", alpha=0.5)  # 투명도(alpha) 조절
# plt.title("Scatter Plot Example")
# plt.show()

df = pd.read_csv("tips.csv") #파일 불러오기
print(df)

plt.figure(figsize=(8, 5))

sns.scatterplot(x="total_bill", y="tip", hue="sex", data=df, palette="Set1")

"""
1) x="total_bill" → X축 설정
X축에 total_bill 컬럼 값 배치
즉, 총 결제 금액을 X축에 나타냄
🔹 2) y="tip" → Y축 설정
Y축에 tip 컬럼 값 배치
즉, 팁 금액을 Y축에 나타냄
🔹 3) hue="sex" → 색상 그룹화
성별(sex)에 따라 다른 색상으로 표시
hue는 데이터를 카테고리별로 색상을 다르게 표현할 때 사용됨
즉, sex 값이 Male이면 하나의 색상, Female이면 다른 색상으로 나타남
🔹 4) data=df → 데이터셋 지정
산점도에 사용할 DataFrame을 설정
df는 pandas.DataFrame 형태의 데이터셋 (예: tips.csv)
🔹 5) palette="Set1" → 색상 테마 적용
"Set1"은 Seaborn의 색상 테마
"coolwarm", "viridis", "pastel" 등 다양한 팔레트 가능

"""

plt.title("Scatter Plot: Total Bill vs Tip")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")

plt.show()

