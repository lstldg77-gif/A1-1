1단계: 개발 환경 준비하기
먼저 코드를 작성하고 관리할 도구들을 점검합니다.

VSCode 설치 및 설정: VSCode를 켜고 좌측 확장(Extensions) 아이콘에서 Python과 Korean Language Pack을 검색해 설치합니다.

버전 확인: 터미널(콘솔)을 열어 아래 명령어를 입력해 정상 설치되었는지 확인합니다.

Bash
python --version  # 3.10 이상이어야 함
git --version
Git 초기 설정: 터미널에 내 이름과 이메일을 등록하고 기본 브랜치 이름을 설정합니다.

Bash
git config --global user.name "내이름"
git config --global user.email "내이메일@email.com"
git config --global init.defaultBranch main
2단계: Git 저장소(Repository) 생성 및 첫 커밋
GitHub 홈페이지에서 새로운 Public 저장소를 만듭니다. (예: prompt-manager)

컴퓨터에 작업 폴더를 만들고 VSCode로 엽니다.

터미널에서 아래 순서대로 입력해 초기 설정을 마칩니다.

Bash
git init
git remote add origin <내_GitHub_저장소_URL>
.gitignore 파일(파이썬 실행 찌꺼기 등을 제외하는 파일)과 프로젝트 제목을 적은 README.md 파일을 만듭니다.

첫 코드를 작성하고 add, commit, push를 수행합니다.

3단계: 파이썬 프로그램 작성하기 (핵심)
모든 코드를 한 파일에 길게 쓰지 말고, 요구사항에 맞춰 함수별로 나누어 작성합니다. 외부 라이브러리 없이 순수 파이썬 기본 문법(리스트, 딕셔너리, 반복문, 조건문)만 사용합니다.

기본 데이터 구조 예시
Python
prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "당신은 10년 경력의 전문 블로거입니다...",
        "category": "텍스트 생성",
        "favorite": True
    },
    {
        "title": "제품 썸네일 생성",
        "content": "다음 제품의 매력적인 썸네일 이미지를 생성해주세요...",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "IT 컨설턴트 페르소나",
        "content": "당신은 전문 IT 컨설턴트입니다...",
        "category": "페르소나",
        "favorite": False
    }
]
구현해야 할 주요 함수들
show_menu(): 메뉴를 출력하고 사용자의 입력을 받는 함수

add_prompt(): 새로운 제목, 내용, 카테고리를 입력받아 prompts 리스트에 추가하는 함수

show_list(): 저장된 전체 프롬프트 목록과 번호, 즐겨찾기(⭐) 여부를 출력하는 함수

show_category(): 카테고리별로 필터링하여 출력하는 함수

search_prompt(): 키워드로 제목이나 내용을 검색하는 함수

show_detail(): 번호를 입력받아 상세 내용을 보여주는 함수

manage_favorite(): 즐겨찾기 추가 및 해제를 처리하는 함수

4단계: 브랜치 활용 및 Git 커밋 채우기 (중요)
미션 조건에 최소 10개 이상의 커밋과 브랜치 생성/병합 기록이 있어야 합니다.

기능을 하나 만들 때마다 커밋을 합니다. (예: git add ., git commit -m "feat: 프롬프트 추가 기능 구현")

브랜치 활용 미션: 프롬프트 목록 기능을 만들 때는 새 브랜치를 파서 작업해 보세요.

Bash
git checkout -b feature/list
# 목록 기능 코드 작성 후 커밋
git checkout main
git merge feature/list
최종적으로 모든 작업이 끝나면 git push origin main으로 GitHub에 업로드합니다.

5단계: 제출물 준비하기
과제가 끝나면 아래 4가지를 챙겨서 제출합니다.

GitHub 저장소 URL

개발 환경 설정 스크린샷 (VSCode, Python 버전, Git 설정 화면)

프로그램 실행 결과 스크린샷 (메뉴, 추가, 목록, 검색 등 동작 화면)

Git 로그 스크린샷 (터미널에 git log --oneline --graph를 친 화면)
