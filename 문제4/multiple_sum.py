# multiple_sum.py

a = [list for list in range(1,101) if list % 3 == 0]

print(f'1부터 100까지 3의 배수: {a}')
print(f'3의 배수의 합: {sum(a)}')
print(f'3의 배수의 개수: {len(a)}')