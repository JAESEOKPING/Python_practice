# dict_comprehension.py

squares = {x: x**2 for x in range(1, 6)}
print("1부터 5까지의 제곱 딕셔너리:", squares)

even_squares = {x: x**2 for x in range(2, 11, 2)}
print("짝수만의 제곱 딕셔너리:", even_squares)