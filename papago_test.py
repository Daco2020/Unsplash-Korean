import urllib.request
import sys
import os

import json


"https://openapi.naver.com/v1/papago/n2mt?source=ko&target=en&text=음식"


client_id = "d7fdlpDnLDNd8ijtcVPg"
client_secret = "3FpGQv4QAK"
encText = urllib.parse.quote("사랑")
data = "source=ko&target=en&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode == 200):
    response_body = json.loads(response.read())

else:
    print("Error Code:" + rescode)

keyword = response_body['message']['result']['translatedText']


print(keyword)
unsplash_url = "https://unsplash.com/s/photos/"
request = urllib.request.Request(unsplash_url)


# print(request)
# rescode = response.getcode()
# if(rescode == 200):
#     response_body = json.loads(response.read())
# print(response_body)
