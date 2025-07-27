# list_conprehension_example.py

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('원본 리스트:',num)

even_num = [x for x in num if x % 2 == 0]
print('짝수들:',even_num)

even_square = [x**2 for x in even_num]
print('짝수의 제곱:',even_square)