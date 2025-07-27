# f_string_example.py

from datetime import date

name = "김철수"
age = 25
pi = 3.14159
price = 1234
percent = 0.855
today = date(2025, 7, 20)

print(f"이름: {name}, 나이: {age}")
print(f"원주율: {pi:.2f}")
print(f"가격: {price:,}원")
print(f"퍼센트: {percent*100:.2f}%")
print(f"날짜: {today:%Y년 %m월 %d일}")