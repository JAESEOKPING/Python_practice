# conditional_expressing.py

score = 85
result = "합격" if score >= 60 else "불합격"
print(f"점수: {score}, 결과: {result}")

age = 17
status = "미성년자" if age < 19 else "성인"
print(f"나이: {age}, 상태: {status}")

numbers = [5, 12, 8, 23, 42]
max_num = max(numbers) if numbers else None
print(f"숫자들의 최대값: {max_num}")

evens = [num for num in numbers if num % 2 == 0]
print(f"양수들: {evens}")
