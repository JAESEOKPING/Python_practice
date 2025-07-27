# any_all_example.py

num_list1 = [2, 4, 6, 8, 10]
num_list2 = [1, 3, 5, 7, 12]

# 첫 번째 리스트
print(f"숫자 리스트: {num_list1}")
print("모든 수가 짝수인가?", all(n % 2 == 0 for n in num_list1))
print("하나라도 10보다 큰 수가 있는가?", any(n > 10 for n in num_list1))

# 두 번째 리스트
print(f"\n숫자 리스트2: {num_list2}")
print("모든 수가 짝수인가?", all(n % 2 == 0 for n in num_list2))
print("하나라도 10보다 큰 수가 있는가?", any(n > 10 for n in num_list2))