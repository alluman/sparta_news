# 🆕Spartanews
스파르타 AI 6기 팀 프로젝트 과제

# 📝프로젝트 소개 
레퍼런스 사이트를 만들 수 있는 API 서버 :: 스파르타 뉴스

# 📅개발 기간
* 2024.05.03일 - 2024.05.10일

# 필요한 api
    accounts - crud, login/logout jwt token
    post, comments, reply crud
    like/upvote 

# 🤝역할 분담
- 이시문
    - 회원가입 / 로그인 / 로그아웃 API
    - News CRUD
    - Postgresql, redis, Docker
      
- 양승조
    - News 리스트 보여주기 API
        - 리스트 포인트 많은 순으로 정렬하기
    - News 댓글 API
        - 대댓글 API

## 🖥️개발 환경
* python : Django
* DB : Postgresql, redis
* Docker

# 🆗주요 기능
- Spartanews
    - 게시글 점수에 따라서 뉴스 조회
        - 날짜가 하루 지날때 마다 -5 Point, 댓글 하나당 +3 Point, 좋아요 하나당 +1 Point


- 최신글
    - 최신 작성 순으로 뉴스 조회
- 댓글
    - 작성한 댓글 조회
- Ask
    - Ask 카테고리 목록 조회
- Show
    - Show 카테고리 목록 조회
      
- Weekly
    - 일주일간 등록된 뉴스 조회
- 글등록
    - 새로운 뉴스 등록
- 검색
    - 뉴스 제목이나 내용을 검색해서 조회
- 로그인
    - 회원가입 / 로그인





