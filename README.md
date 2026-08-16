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

1. VSCode에서 Python 파일을 생성하고 실행할 수 있다
설명 내용: VSCode는 소스 코드를 작성하는 편집기(IDE)입니다. 새 파일을 만들 때 확장자를 .py로 지정하면 파이썬 파일이 됩니다. 작성한 코드는 VSCode 내장 터미널에서 python 파일이름.py 명령어를 입력해 실행할 수 있습니다.

핵심 포인트: .py 확장자와 터미널 실행 명령어(python) 기억하기

2. 터미널에서 Python/Git 버전을 확인하고 필요한 설정을 점검할 수 있다
설명 내용: 컴퓨터에 개발 도구가 잘 설치되어 있는지 확인하는 과정입니다. 터미널(명령 프롬프트 등)에 아래 명령어를 입력해 버전을 체크합니다.

Python 버전 확인: python --version (또는 python3 --version)

Git 버전 확인: git --version

설정 점검: Git을 처음 사용할 때는 내 커밋 기록에 남을 이름과 이메일을 필수로 설정해야 합니다.

git config --global user.name "내이름"

git config --global user.email "내이메일@email.com"

3. 파이썬 기초 문법에 대해 설명할 수 있다
설명 내용: 이번 프로그램 만들기에 사용된 핵심 파이썬 개념들입니다.

변수: 데이터를 담아두는 상자 (예: title = "블로그 글")

리스트([])와 딕셔너리({}): 여러 데이터를 순서대로 담거나(리스트), 키-값 쌍으로 구조화하여 담는(딕셔너리) 데이터 구조

조건문(if-elif-else): 상황에 따라 다른 코드가 실행되도록 흐름을 제어하는 문법 (예: 사용자가 메뉴 1을 누르면 추가 기능 실행)

반복문(while, for): 프로그램이 종료되지 않고 계속 메뉴를 보여주거나(while), 목록을 하나씩 꺼내 출력할 때(for) 사용

함수(def): 코드를 기능별로 묶어두고 필요할 때마다 불러다 쓰는 재사용 가능한 코드 블록

4. Git이 무엇이고 왜 필요한지 설명할 수 있다
설명 내용:

Git이란?: 코드의 변경 이력(수정 역사)을 시간 순서대로 기록하고 관리해 주는 버전 관리 시스템(VCS)입니다.

왜 필요한가?: 코드를 수정하다가 에러가 났을 때 예전 상태로 쉽게 되돌릴 수 있고, 여러 사람이 협업할 때 누가 어떤 부분을 고쳤는지 추적할 수 있기 때문에 개발자에게 필수적입니다.

5. Git 주요 명령어(init, add, commit, push, pull, checkout, clone, merge)의 역할
init: 내 컴퓨터의 일반 폴더를 Git이 관리하는 로컬 저장소로 지정(초기화)합니다.

add: 수정한 파일을 Git이 추적하도록 임시 저장소(Staging Area)에 올립니다.

commit: 임시 저장된 파일들의 상태를 확정하여 의미 있는 변경 이력으로 기록합니다.

push: 내 컴퓨터에서 커밋한 기록을 원격 저장소(GitHub)로 업로드합니다.

pull: 원격 저장소(GitHub)에 있는 최신 코드를 내 컴퓨터로 다운로드합니다.

checkout: 다른 브랜치로 이동하거나, 특정 시점의 코드로 전환합니다.

clone: 원격 저장소에 있는 프로젝트 통째로 내 컴퓨터로 복사해 옵니다.

merge: 다른 브랜치에서 작업한 내용을 현재 브랜치와 하나로 합칩니다.

6. 브랜치를 생성하고 병합할 수 있다
설명 내용:

브랜치(Branch)란?: 기존 코드(main)를 복사해서 독립적으로 새로운 기능(예: 프롬프트 목록 보기 기능)을 개발할 수 있는 나만의 작업 공간입니다.

생성과 병합: git checkout -b 새브랜치이름으로 브랜치를 만들어 안전하게 기능을 개발한 뒤, 작업이 끝나면 main 브랜치로 돌아와(git checkout main) git merge 새브랜치이름으로 합칩니다.

7. GitHub에 코드를 업로드하고 관리할 수 있다
설명 내용: GitHub는 Git으로 관리하는 코드 저장소를 온라인에 보관하고 공유할 수 있는 클라우드 플랫폼입니다. 내 컴퓨터에서 작업한 내용을 git remote add origin URL로 연결한 뒤 git push를 통해 업로드하고, 웹 화면에서 다른 사람들과 코드를 공유하거나 관리할 수 있습니다.
