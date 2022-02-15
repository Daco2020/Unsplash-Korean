from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
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
        "./item.html",
        {"request": request},
    )


@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, q: str):
    word = translate_word(q)
    img_url = get_image(word)
    return templates.TemplateResponse(
        "./index.html",
        {"request": request, "title": "콜렉터 덕순이", "keyword": word, "img_url": img_url},
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

