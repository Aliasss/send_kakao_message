## 랭킹뉴스 3개를 크롤링하여 카카오톡 나에게로 보내기
### kakao developers Hash Api key 활용

(1) kakao_token.py로 토큰 받아서 저장  
(2) send_message.py 실행
- 단, 토큰이 만료되었으면 토큰 update하고
- 토큰 save  

(3) 콘텐츠의 링크는 kakao developers-플랫폼-사이트 도메인에 추가되어 있어야 함

  
<Br>  
  
exe 파일 생성(https://blog.daum.net/geoscience/1625)  
(1) send_message.py가 있는 디렉토리에서 터미널 실행  
(2) pyinstaller --noconsole --onefile send_message.py  
(3) dist 폴더에 exe 파일 생성  
(4) 스케줄링 : https://blog.daum.net/geoscience/1626  
(5) exe 파일 -> 시작프로그램으로 위치 옮긴 후에  
(6) 작업관리자 확인!  
