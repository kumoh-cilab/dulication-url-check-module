# 🖥️ 중복 체크 시간 측정&비교 모듈 


## 🌱 프로젝트 소개 
Python을 기반으로 여러 DB의 조회(중복 체크)성능을 측정 및 비교하는 모듈입니다. 

--- 
## 🌱 개발환경 

---
- Python 3.10


---

## 🌱 사용한 Database

- foundationDB
- python-diskcache 
- faster 
- databute 

--- 


## 🌱 프로젝트 구조 

---

## 🌱 기타 


--- 

- foundationdb를 실행하기 위해서 파이썬 파일을 실행하는 환경에 foundationDB Client를 설치해야 합니다. 

- foundation-db는 분산환경에서 동작하는 key-value database... MongoDB와의 차이점은 트랜젝션 ACID를 지원한다는 것..? - 속도 측면에서 이점은 잘모르겠음 

- python-diskcache는 디스크 기반의 캐싱 라이브러리로, 메모리의 데이터를 캐싱하는 것이 아닌, 디스크의 데이터를 캐싱하여 사용->메모리 캐시 보단 느리지만 일반 DB보단 빠를듯


