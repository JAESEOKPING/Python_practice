# multiplication_table.py

a = int(input('몇 단을 출력할까요? '))

print(f'{a}단 구구단:')
for x in range(1,10):
    print(f'{a} X {x} = {a*x}')