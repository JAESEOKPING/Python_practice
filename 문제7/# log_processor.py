# log_processor.py

log_data = """2025-07-20 10:30:00 - ERROR - 데이터베이스 연결 실패
2025-07-20 11:45:00 - ERROR - 파일을 찾을 수 없음
2025-07-20 09:15:00 - WARNING - 메모리 사용량이 높습니다
2025-07-20 12:00:00 - WARNING - 디스크 공간 부족
2025-07-20 13:00:00 - INFO - 백업 완료
2025-07-20 13:10:00 - INFO - 서비스 시작"""

with open("log.txt", "w", encoding="utf-8") as f:
    f.write(log_data)

print("로그 파일이 생성되었습니다.\n")

def filter_logs(level):
    logs = []
    with open("log.txt", "r", encoding="utf-8") as f:
        for line in f:
            if f" - {level} -" in line:
                logs.append(line.strip())
    return logs

print("ERROR 레벨 로그들:")
for log in filter_logs("ERROR"):
    print(log)
print()

print("WARNING 레벨 로그들:")
for log in filter_logs("WARNING"):
    print(log)