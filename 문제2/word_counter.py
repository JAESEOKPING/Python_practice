#word_counter.py

a = str(input("문장을 입력하세요: "))
b = a.replace("  ","")
c = a.split()

print(f"공백 제거: {b}")
print(f"단어 개수: {len(c)}")