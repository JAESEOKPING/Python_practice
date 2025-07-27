# file_write_read.py

lines = [
    "안녕하세요\n",
    "파이썬 파일 처리를 연습하고 있습니다\n",
    "오늘은 좋은 날씨입니다\n"
]

print("파일에 저장할 내용:\n")
for line in lines:
    print(line, end='')

with open("test.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("\n파일에서 읽어온 내용:")
with open("test.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line, end='')