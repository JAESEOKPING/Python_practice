# module_usage.py

import datetime
import random

now = datetime.datetime.now()
print("현재 날짜와 시간:", now.strftime("%Y-%m-%d %H:%M:%S"))

print("포맷된 날짜:", now.strftime("%Y년 %m월 %d일 %A"))


rand_int = random.randint(1, 10)
print("\n임의의 숫자:", rand_int)


rand_float = round(random.uniform(1.0, 10.0), 2)
print("임의의 실수:", rand_float)


fruits = ['포도', '사과', '오렌지', '바나나', '딸기']


print("\n임의의 리스트 요소:", random.choice(fruits))


random.shuffle(fruits)
print("\n섞인 리스트:", fruits)