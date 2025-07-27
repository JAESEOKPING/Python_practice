# student_sort.py

students_list = {'김철수': {'나이' : 20, '학과' : '컴퓨터공학과'},
                '박민수': {'나이' : 21, '학과' : '경영학과'},
                '이영희': {'나이' : 24, '학과' : '영어영문학과'},
                '최수진': {'나이' : 23, '학과' : '수학과'}}

list_sort = sorted(students_list.items(), key=lambda item: item[1]['나이'], reverse=False)

print("나이 순으로 정렬된 학생 목록:\n")
for name,info in list_sort:
    age = info['나이']
    major = info['학과']
    print(f'{name} ({age}세) - {major}')

