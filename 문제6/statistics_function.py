# statistics_functions.py

def get_statistics(numbers):
    from math import sqrt

    n = len(numbers)
    avg = sum(numbers) / n
    maximum = max(numbers)
    minimum = min(numbers)

    # 분산 계산 시 반드시 분모를 n 으로 해야 모집단 표준편차
    variance = sum((x - avg) ** 2 for x in numbers) / n

    std_dev = round(sqrt(variance), 2)  # 소수 둘째 자리까지 반올림

    print(f"숫자들: {numbers}")
    print(f"평균: {avg}")
    print(f"최댓값: {maximum}")
    print(f"최소값: {minimum}")
    print(f"표준편차: {std_dev}")

# 테스트 실행
get_statistics([10, 20, 30, 40, 50])