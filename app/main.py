import random
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.models import mongodb
from app.models.keword import KeywordModel
from app.util.translation import translate_word
from app.util.crawling import get_image


BASE_DIR = Path(__file__).resolve().parent


app = FastAPI()


templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        "./index.html",
        {"request": request},
    )


@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, q: str):
    word = translate_word(q)
    image_url_list = get_image(word)
    random.shuffle(image_url_list)
    return templates.TemplateResponse(
        "./index.html",
        {"request": request, "title": "Unsplash 한글 검색기", "keyword": word, "image_url_list": image_url_list},
    )



# 서버가 시작 되었을 때 사용되는 이벤트
@app.on_event("startup")
def on_app_start():
    print("서버가 시작되었습니다.")
    mongodb.connect()


# 서버가 종료 되었을 때 사용되는 이벤트
@app.on_event("shutdown")
def on_app_shutdown():
    print("서버가 종료되었습니다.")
    mongodb.close()

