import urllib.request
import json
from app.config import NAVER_API_ID, NAVER_API_SECRET


def translate_word(word):
    if not word:
        return "검색어를 입력해주세요 :)"

    encText = urllib.parse.quote(word)
    data = "source=ko&target=en&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", NAVER_API_ID)
    request.add_header("X-Naver-Client-Secret", NAVER_API_SECRET)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()

    if rescode == 200:
        response_body = json.loads(response.read())
    else:
        print("Error Code:" + rescode)

    keyword = response_body["message"]["result"]["translatedText"]

    if "." in keyword:
        keyword = keyword.replace(".", "")

    return keyword
