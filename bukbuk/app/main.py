from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
from app.util.translation import translate_word
from app.util.crawling import get_image
from config import CLIENT_ID, CLIENT_SECRET

BASE_DIR = Path(__file__).resolve().parent


app = FastAPI()


templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, q: str):
    word = translate_word(q, CLIENT_ID, CLIENT_SECRET)
    img_url = get_image(word)
    return templates.TemplateResponse(
        "./index.html",
        {"request": request, "title": "콜렉터 덕순이", "keyword": word, "img_url": img_url},
    )
