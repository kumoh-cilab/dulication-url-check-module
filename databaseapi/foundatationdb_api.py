import fdb

# TODO 파이썬 파일을 실행하는 환경에서 fdb client를 설치해야함.
fdb.api_version(730)
db = fdb.open()

print("a")