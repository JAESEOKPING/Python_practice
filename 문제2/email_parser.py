#email_parser.py

a = str(input("이메일 주소를 입력하세요: "))
b = a.split("@")

print(f"사용자명: {b[0]}")
print(f"도메인: {b[1]}")