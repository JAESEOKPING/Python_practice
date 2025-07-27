#discount_calculator.py

a = int(input("상품 가격을 입력하세요: "))
b = int(input("할인율을 입력하세요(%): "))
c = int((a/100)*b)

print(f"원래 가격: {a}원")
print(f"할인율: {b}%")
print(f"할인 금액: {c}원")
print(f"최종 가격: {a-c}원")