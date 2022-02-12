
## 서버열기
- FastAPI 설치
- Uvicorn 설치
- app폴더 생성
- app폴더 안에 main.py 생성
- 루트 디렉토리에 server.py 생성
- 서버 작동여부 확인 ( 명령어 : uvicorn app.main:app --reload )


## 동적라우팅이란?

동적라우팅이란 직접적인 경로 설정없이 목적지까지 도달할 수 있도록 하는 것을 의미한다.
라우터의 경로에 특정 값을 넣어 해당되는 자원으로 연결하는 것.
ex1. Query parameters
ex2. URL parameters (@app.get("/items/{item_id}"))





