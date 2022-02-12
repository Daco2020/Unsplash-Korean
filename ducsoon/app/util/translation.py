import urllib.request
import json


def translate_word(word, CLIENT_ID, CLIENT_SECRET):
    if not word:
        return "검색어를 입력해주세요 :)"

    encText = urllib.parse.quote(word)
    data = "source=ko&target=en&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", CLIENT_ID)
    request.add_header("X-Naver-Client-Secret", CLIENT_SECRET)
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
