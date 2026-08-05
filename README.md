# A1-1 미션 프로젝트 진행 4단계 로드맵

//=================

## 1단계: 개발 환경 확인 및 Git 초기화하기
              가장 먼저 코드를 작성할 준비와 버전 관리 도구를 세팅합니다.

### 1) VSCode 열기 및 Python 확인

	- VSCode를 열고 터미널(Ctrl + ~)을 엽니다.

	- 터미널에 아래 명령어를 입력해 Python과 Git 버전을 확인합니다.

### python --version
### git --version

//=================

### 2) Git 사용자 설정 (처음 Git을 쓰는 경우 필수)
	### git config --global user.name "내이름"
	### git config --global user.email "내이메일@email.com"
	### git config --global init.defaultBranch main

//=================

### 3) GitHub 저장소 생성 및 연결

	- GitHub 웹사이트에서 새 Repository를 생성합니다 (예: prompt-manager).

	- 로컬 프로젝트 폴더를 만들고 Git을 초기화합니다.

	### git init
	### git remote add origin [내-깃허브-저장소-주소]

		git init
		git remote add origin [내-깃허브-저장소-주소]

//=================

## 2단계: 기본 데이터와 프로그램 틀(메뉴) 잡기
	      파이썬 파일(예: main.py)을 만들고, 프로그램의 뼈대가 되는 메뉴 반복문과 기본 데이터를 작성합니다.

	### - 기본 데이터 구조 설계:
		 제시된 예시처럼 리스트 안에 딕셔너리 형태로 3개 이상의 프롬프트를 미리 넣어둡니다.

	### - 무한 루프 메뉴 구현:
		 사용자가 0번을 누르기 전까지 계속 메뉴가 뜨도록 while 문을 작성합니다.

## main.py 예시 뼈대

prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "당신은 10년 경력의 전문 블로거입니다...",
        "category": "텍스트 생성",
        "favorite": True
    },
    # 최소 3개 이상 추가
]

def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")

# 프로그램 실행 루프
while True:
    show_menu()
    choice = input("선택: ")
    
    if choice == "1":
        # TODO: 프롬프트 추가 함수 호출
        pass
    elif choice == "0":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다. 다시 선택해주세요.")

//=================

## 3단계: 기능별 함수 하나씩 구현하기 (Git 브랜치 활용!)
요구사항 기능들을 하나씩 함수로 구현합니다. 
특히 "프롬프트 목록" 기능은 Git 브랜치를 새로 파서 작업한 뒤 main에 merge 하는 미션 요구사항이 있으므로 꼭 지켜야 합니다.


### 1) 기능 구현 순서 추천:

	- 프롬프트 목록 보기 (show_list): 리스트를 순회하며 번호와 함께 출력

	- 프롬프트 추가 (add_prompt): input()으로 제목, 내용, 카테고리를 받아 prompts.append()로 추가

	- 상세 보기 및 검색 (search_prompt, view_detail): 조건에 맞는 데이터 찾기

	- 즐겨찾기 관리 (toggle_favorite): True/False 값 반전시키기


### 2) Git 브랜치 미션 수행 팁:

	- 목록 기능을 만들 때 터미널에서 브랜치를 생성하고 이동합니다.
	### git checkout -b feature/list

	- 코드를 완성하고 저장한 뒤 커밋(저장)합니다.
	### git add .
	### git commit -m "feat: 프롬프트 목록 출력 기능 구현"

	- 다시 main 브랜치로 돌아와서 병합합니다.
	### git checkout main
	### git merge feature/list

//=================

## 4단계: README.md 작성 및 GitHub에 최종 제출

### 1) 프로젝트 루트 폴더에 README.md 파일을 만들고 프로그램 설명, 실행 방법, 기능 목록을 보기 좋게 작성합니다.

### 2) 지금까지 작업한 내용을 최종적으로 GitHub에 업로드(Push)합니다.

	### git add .
	### git commit -m "docs: README 작성 및 최종 코드 정리"
	### git push origin main


### 3) 요구하는 스크린샷(개발 환경, 실행 결과, git log --oneline --graph 결과)을 캡처하여 저장합니다.

##💡 지금 당장 무엇부터 해야 할까요?

	### VSCode를 켜고 빈 폴더를 연 뒤, main.py 파일을 만드세요.

	### 터미널을 열어 git init을 치고 위에서 안내한 2단계 코드를 복사해서 붙여넣은 뒤 실행해 보세요. 
        ### 메뉴가 뜨는 것을 확인하는 순간 첫 번째 발자국이 성공적으로 떼어진 것입니다!


