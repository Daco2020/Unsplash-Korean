from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent  # 현재 연 파일 경로의 부모 위치를 의미한다.
# print(BASE_DIR) >>> /Users/daco/Study/Unsplash_kor/tutorial/app


app = FastAPI()  # 싱글 톤 패턴

# mount : 미들웨어 / StaticFiles : css, js, 이미지 등 파일을 의미 >>> 여기서는 사용하지 않음
# app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory=BASE_DIR / "templates")  # html파일의 위치를 지정


@app.get("/items/{id}", response_class=HTMLResponse)  # 동적라우팅 : 쿼리파라미터, URL파라미터
async def read_item(request: Request, id: str):  # Request와 str 처럼 타입힌트를 주어야함
    print(dir(request))
    img_link = "https://images.unsplash.com/photo-1577234286642-fc512a5f8f11?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=735&q=80"
    return templates.TemplateResponse(
        "./item.html",
        {
            "request": request,
            "id": id,
            "img_link": img_link,
        },  # 여기서 두번째 인자를 컨텍스트라고 한다. 컨텍스트에는 리퀘스트 인스턴스를 가지고 있어야함.
    )  # 제이슨이 아닌 html형태로 리턴하는 것임


@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, q: str):
    return templates.TemplateResponse(
        "./index.html",
        {"request": request, "title": "콜렉터 덕순이", "keyword": q},
    )
