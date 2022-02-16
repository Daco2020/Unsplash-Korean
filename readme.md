## 'Unsplash korean'
'Unsplash'사이트의 이미지를 한글로 검색하여 가져오는 웹 서비스 입니다. </br> </br> </br>
[![Unsplash 한글 검색기](https://user-images.githubusercontent.com/76890895/154288593-acbc3ba9-59d0-4d87-8eb6-629b5ed2f267.png)](https://youtu.be/m61ROPZI9nQ)
 </br>
 시연영상
 </br>
  </br>
   </br>
 
## 사용기술
언어 : Python </br>
프레임워크 : FastAPI, Uvicorn</br>
데이터베이스 : MongoDB, ODMantic</br>
</br>
## 주요과제 
[x] 쿼리에서 키워드 받아오기</br>
[x] 키워드를 PAPAGO API를 활용하여 영문으로 번역하기</br>
[x] 번역된 키워드로 언스플래시 검색하기</br>
[x] 반환된 값에서 이미지 값만 추출하기</br>
[] 한글과 영문 키워드를 디비에 저장하고 '검색 수' 추가하기</br>
[x] '이미지'와 '검색 수' 값을 템플릿에 넘겨 반환하기</br>
</br>

## 예외처리
[x] 검색어가 없다면 사용자에게 요구하기</br>
[] 이미지가 없다면 사용자에게 알려주기</br>
</br>
## 업데이트 사항
2022년 2월 14일 파파고 API 연결 및 키워드 번역 성공</br>
2022년 2월 16일 Unsplash 이미지 크롤링 및 프론트 화면 구현 완료</br>
</br>
## 추가구현 예정
[] 1차 코드 최적화</br>
[] 이미지 최대 20개 노출 -> 추후 20개 이상, 페이지 단위로 노출 필요</br>
[] 전체 이미지 다운로드 기능 추가</br>
[] EC2 배포
