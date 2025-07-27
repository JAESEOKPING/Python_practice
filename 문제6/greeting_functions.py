# greeting_functions.py

def greeting(name="John", title="님", end_message=""):
    # 영어 이름 John만 영어 인사 처리
    if name == "John":
        return "Hello, John!"
    msg = f"안녕하세요, {name}{title}!"
    if end_message:
        msg += f" {end_message}"
    return msg

# 출력 예시
print(greeting("김철수", "님"))             
print(greeting())                       
print(greeting("이영희", "님", "좋은 하루 되세요!"))