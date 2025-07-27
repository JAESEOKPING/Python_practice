# grade_calculator.py

a = int(input('점수를 입력하세요: '))

if a>=90:
    print(f'점수 {a}점의 학점은 A입니다.')
elif a>=80:
    print(f'점수 {a}점의 학점은 B입니다.')
elif a>=70:
    print(f'점수 {a}점의 학점은 C입니다.')
elif a>=60:
    print(f'점수 {a}점의 학점은 D입니다.')
else:
    print(f'점수 {a}점의 학점은 F입니다.')