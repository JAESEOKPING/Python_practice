# remove_duplicates.py

num_lists = [3, 1, 4, 5, 9, 2, 6, 5, 3]

num_sets = list(set(num_lists))
num_sorted = sorted(num_sets , reverse=False)

print(f'원본 리스트: {num_lists}')
print(f'중복 제거 후: {num_sorted}')