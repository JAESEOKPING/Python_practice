# fruit_search.py

fruit_list = ['사과','바나나','오렌지','포도','딸기']

fruit = input('찾을 과일을 입력하세요: ')

if fruit in fruit_list:
    print(f"'{fruit}'(이)가 목록에 있습니다!")
else:
    print(f"'{fruit}'(이)가 목록에 없습니다!")