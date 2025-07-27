#character_counter.py

a = str(input("문자열을 입력하세요: "))
b = str(input("찾을 문자를 입력하세요: "))
c = a.count(b)

print(f"문자 '{b}'이 {c}번 나타납니다.")
