# system_info.py

import os
import sys

print(f"현재 작업 디렉토리: {os.getcwd()}")
print(f"Python 버전: {sys.version}")
print(f"운영체제: {os.name}")

path_env = os.environ.get('PATH', '')
print(f"환경 변수 PATH 일부: {':'.join(path_env.split(':')[:3])}")

dir_path = "/Users/username/documents"
file_name = "report.txt"
file_path = os.path.join(dir_path, file_name)
ext = os.path.splitext(file_name)[1]

print("\n파일 경로 정보:")
print(f"- 디렉토리: {dir_path}")
print(f"- 파일명: {file_name}")
print(f" - 확장자: {ext}")

file_exists = os.path.exists(file_path)
print(f"파일 존재 여부: {file_exists}")

# os.getcwd(): 현재 작업중인 디렉토리
# sys.version: Python 해석기 버전
# os.name: 운영체제 타입
# os.environ: 환경 변수
# os.path.join: 경로 합치기
# os.path.splitext: 확장자 분리
# os.path.exists: 파일 존재 여부