# map_filter_example.py

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("원본 숫자:", numbers)

squares = list(map(lambda x: x**2, numbers))
print("모든 수의 제곱:", squares)

greater_than_5 = list(filter(lambda x: x > 5, numbers))
print("5보다 큰 수들:", greater_than_5)

greater_than_5_squares = list(map(lambda x: x**2, greater_than_5))
print("5보다 큰 수들의 제곱:", greater_than_5_squares)

