## 'Unsplash korean'
'Unsplash'사이트의 이미지를 한글로 검색하여 가져오는 웹 서비스 입니다.

## 사용기술
언어 : Python </br>
프레임워크 : FastAPI, Uvicorn</br>
데이터베이스 : MongoDB, ODMantic</br>

## 진행상황
주요과제
[x] 쿼리에서 키워드 받아오기</br>
[x] 키워드를 PAPAGO API를 활용하여 영문으로 번역하기</br>
[] 번역된 키워드로 언스플래시 검색하기</br>
[] 반환된 값에서 이미지 값만 추출하기</br>
[] 한글과 영문 키워드를 디비에 저장하고 '검색 수' 추가하기</br>
[] '이미지'와 '검색 수' 값을 템플릿에 넘겨 반환하기</br>
</br>
예외처리</br>
[] 검색어가 없다면 사용자에게 요구하기</br>
[] 이미지가 없다면 사용자에게 알려주기</br>

