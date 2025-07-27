# list_analysis.py

num_list = [15, 3, 27, 8, 19, 12, 31]
a = 2

num_sorted = sorted(num_list, reverse=True)
second_largest = num_sorted[a-1]

print(f'숫자 목록: {num_list}')
print(f'최댓값 {max(num_list)}')
print(f'최솟값 {min(num_list)}')
print(f'두 번째로 큰 값 {second_largest}')
