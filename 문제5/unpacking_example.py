# unpacking_example.py

point = (10, 20)
x, y = point
print(f"좌표: x={x}, y={y}")

data = [1, 2, 3]
a, b, c = data
print(f"리스트 언패킹: a={a}, b={b}, c={c}")

def sum_args(*args):
    return sum(args)
result = sum_args(10, 20, 30)
print(f"가변 인수의 합: {result}")

def print_kwargs(**kwargs):
    print("키워드 인수들:", end=' ')
    print(", ".join([f"{k}={v}" for k, v in kwargs.items()]))
print_kwargs(name="김철수", age=25, city="서울")