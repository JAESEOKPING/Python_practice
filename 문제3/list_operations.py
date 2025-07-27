# list_operations.py

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

com_lists = list1 + [x for x in list2 if x not in list1]

set_lists = list(set(list1) & set(list2))
set_lists.sort()  

print(f"리스트1: {list1}")
print(f"리스트2: {list2}")
print(f"병합된 리스트: {com_lists}")
print(f"공통 요소: {set_lists}")