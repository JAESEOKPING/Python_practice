# shopping_cart.py

shopping_dict = {'사과' : {'수량' : 2, '가격' : 1000},
                '바나나' : {'수량' : 3, '가격' : 800},
                '오렌지' : {'수량' : 1, '가격' : 1500}}

print('쇼핑 카트:')
total = 0
for name,info in shopping_dict.items():
    quantity = info['수량']
    price = info['가격']
    it_to = quantity*price
    print(f'{name}:{quantity}개 (개당 {price}원) = {it_to}원')
    total += it_to

print(f'총 가격: {total}')

