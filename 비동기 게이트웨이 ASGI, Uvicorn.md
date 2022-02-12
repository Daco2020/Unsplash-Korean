## ASGI란? ASGI를 알아야하는 이유는?
ASGI는 WSGI의 문제점을 개선하기 위해 나왔다.
클라이언트와 서버가 요청을 받고 응답을 하기 위해서 입구 역할이 필요한데 그 중에 하나가 ASGI이다.

WSGI : web server gateway interface
ASGI : 비동기 문법을 제공하기 위해 나온 것
ASGI는 애플리케이션 프로그램(ex. FastAPI)의 실행 결과를 웹 서버에 전달하고, 웹 서버는 클라이언트에게 응답을 전송한다.

서버 게이트웨이 : 서버로 들어가는 입구 역할

## Uvicorn
ASGI 웹 서버(프로세스 관리자, 실행기)
ASGI 웹 애플리케이션을 실행하는 서버
