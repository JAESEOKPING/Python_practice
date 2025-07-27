# csv_grade_processor.py

import csv

grades = [
    ["이름", "점수"],
    ["김철수", 85],
    ["이영희", 92],
    ["박민수", 78],
    ["최수진", 95]
]

with open("grades.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(grades)

print("학생 성적이 grades.csv에 저장되었습니다.\n")

students = []
scores = []

with open("grades.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        students.append(row[0])
        scores.append(int(row[1]))

print("성적 분석 결과:")
for name, score in zip(students, scores):
    print(f"{name}: {score}점")

average = sum(scores) / len(scores)
print(f"전체 평균: {average:.1f}점")