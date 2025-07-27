# factorial_functions.py

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

nums = [5, 7]
for n in nums:
    print(f"{n}! (재귀) = {factorial_recursive(n)}")
    print(f"{n}! (반복) = {factorial_iterative(n)}")