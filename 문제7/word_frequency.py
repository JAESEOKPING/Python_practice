# word_frequency.py

from collections import Counter
import re

filename = "sample.txt"

with open(filename, "r", encoding="utf-8") as f:
    text = f.read()

words = re.findall(r'[가-힣\w]+', text)

word_counts = Counter(words)

print("단어 빈도 분석 결과:")
for word, count in word_counts.most_common():
    print(f"{word}: {count}번")