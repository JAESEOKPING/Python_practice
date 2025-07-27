# zip_example.py

students = ['김철수','이영희','박민수','최수진']
score = [85, 92, 78, 95]

print('\n학생과 점수 매칭:')
for i in zip(students, score):
    print(f'{i[0]}: {i[1]}점')


joined = dict(zip(students,score))

print('점수별 학생 딕셔너리:',joined)