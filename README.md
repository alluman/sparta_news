# 🆕Spartanews
스파르타 AI 6기 팀 프로젝트 과제

# 📝프로젝트 소개 
레퍼런스 사이트를 만들 수 있는 API 서버 :: 스파르타 뉴스

# 📅개발 기간
* 2024.05.03일 - 2024.05.10일

# 필요한 api
    * 유저 : CRUD
    * Login, Logout jwt token
    * 게시글, 댓글, 답글 : CRUD, 좋아요, 추천
    * 정렬기능

## 🖥️개발 환경
* python : Django, Drf
* DB : Postgresql, redis
* Docker
  
* ~~EC2, front(vue)~~

# 🤝역할 분담
- 이시문
    - 유저 : CRUD
    - Login, Logout jwt token
    - Post CRUD
    - Postgresql, redis, Docker
      
- 양승조
    - News 리스트 보여주기 API
        - 리스트 포인트 많은 순으로 정렬하기
    - 댓글, 답글 : CRUD
    - 좋아요, 추천


# 🆗주요 기능
- Spartanews
    - 게시글 점수에 따라서 뉴스 조회
        - 날짜가 하루 지날때 마다 -5 Point, 댓글 하나당 +3 Point, 좋아요 하나당 +1 Point
- 회원가입
   - id, password, email 을 입력받아 가입
- 로그인
   - 로그인 성공시 jwt 토큰 발급
- 로그아웃
   - jwt 토큰 확인 후 토큰 삭제
- 회원탈퇴
   - 유저 정보 확인 후 회원 정보 삭제
- 프로필
   - 유저 데이터 확인 후 유저 정보 조회
- 프로필 수정
   - password 확인 후 유저 정보 수정
- 뉴스 등록
   - 로그인 상태 확인 후 뉴스 등록
- 뉴스 리스트
   - 포인트 많은 순서대로 정렬된 정보 조회
- 뉴스 디테일
   - 뉴스 세부정보 조회 
- 뉴스 수정
   - post_id 확인 후 정보 수정
- 뉴스 삭제
   - post_id 확인 후 뉴스 삭제
- 댓글 목록
   - 댓글 목록 조회
- 댓글 등록
   - 뉴스 게시글에 댓글 등록
- 댓글 수정
   - 게시글 id 확인 후 댓글 수정
- 댓글 삭제
   - 게시글 id 확인 후 댓글 삭제
- 대댓글 목록
   - 댓글에 달린 자식 댓글 조회
- 대댓글 등록
   - 댓글의 parent_comment 필드를 확인 후 부모 댓글에 대댓글 작성






