# number_sum.py

total = 0

while True:
    a = int(input('숫자를 입력하세요 (0을 입력하면 종료):'))
    if a != 0:
        total += a
    else:
        break

print(f'입력된 숫자들의 합: {total}')
