# split_join_example.py

a = 'Python is awesome programming language'
b = a.split(' ')
c = '-'.join(b)
d = a.upper()

print(f'원본 문자열: {a}')
print(f'분리된 단어들: {b}')
print(f'하이픈으로 연결: {c}')
print(f'대문자로 변환 후 공백으로 연결: {d}')