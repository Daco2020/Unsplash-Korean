import requests
from bs4 import BeautifulSoup 


def fetch(session, url):
    with session.get(url) as response:
        return response.text


def get_image(word):
    if word != "검색어를 입력해주세요 :)":
        url = "https://unsplash.com/s/photos/" + word
        
        with requests.Session() as session:
            html_doc = fetch(session, url)
            
        soup = BeautifulSoup(html_doc, "html.parser") 
        soup.prettify()
        
        image_url_list = []
        for link in soup.find_all('img'):
            image_url = link.get('src')
            if "images.unsplash.com/photo-" in image_url and "q=80" in image_url:
                image_url_list.append(image_url)
                
        # 중복 url 제거를 위해 set 이용
        return list(set(image_url_list)) 
    
    return []
