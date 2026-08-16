
import json
from pathlib import Path
from collections import defaultdict

DATA_FILE = Path("prompts.json")
EXPORT_DIR = Path("prompt_exports")

# 기본 프롬프트 데이터
DEFAULT_PROMPTS = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "당신은 10년 경력의 전문 블로거입니다. 주어진 주제에 대해 SEO에 최적화된 블로그 글을 작성해주세요. 서론, 본론, 결론 구조를 갖추고, 독자의 관심을 끄는 제목을 3개 제안해주세요.",
        "category": "텍스트 생성",
        "favorite": True,
        "views": 0
    },
    {
        "title": "제품 썸네일 생성",
        "content": "다음 제품의 매력적인 썸네일 이미지를 생성하기 위한 미드저니/DALL-E 프롬프트를 작성해주세요. 주요 색상과 시각적 요소를 포함해주세요.",
        "category": "이미지 생성",
        "favorite": False,
        "views": 0
    },
    {
        "title": "IT 컨설턴트 페르소나",
        "content": "당신은 15년 경력의 저명한 IT 컨설턴트입니다. 클라우드 전환 및 MSA 도입을 고민하는 기업 대표의 눈높이에 맞춰 이해하기 쉽고 전문적인 조언을 제공해주세요.",
        "category": "페르소나",
        "favorite": False,
        "views": 0
    }
]

CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]


def normalize_prompt(p):
    p.setdefault("favorite", False)
    p.setdefault("views", 0)
    return p


def load_prompts():
    if not DATA_FILE.exists():
        return [dict(p) for p in DEFAULT_PROMPTS]

    try:
        with DATA_FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            return [normalize_prompt(p) for p in data]
    except (json.JSONDecodeError, OSError):
        print("저장 파일을 읽지 못해 기본 프롬프트를 불러옵니다.")
    return [dict(p) for p in DEFAULT_PROMPTS]


prompts = load_prompts()


def save_prompts():
    try:
        with DATA_FILE.open("w", encoding="utf-8") as f:
            json.dump(prompts, f, ensure_ascii=False, indent=2)
    except OSError as e:
        print(f"저장 중 오류가 발생했습니다: {e}")


def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("8. 프롬프트 수정")
    print("9. 프롬프트 삭제")
    print("10. 조회수 Top 목록")
    print("11. JSON 저장")
    print("12. 카테고리별 Markdown 내보내기")
    print("0. 종료")


def choose_category(allow_new=True):
    print("\n카테고리 선택:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"{i}) {cat}")

    choice = input("선택 (번호 또는 직접 입력): ").strip()

    if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
        return CATEGORIES[int(choice) - 1]

    if choice in CATEGORIES:
        return choice

    if choice == "":
        return "기타"

    if allow_new:
        return choice

    print("잘못된 카테고리입니다.")
    return None


def add_prompt():
    print("\n=== 프롬프트 추가 ===")
    title = input("제목: ").strip()
    if not title:
        print("제목은 비워둘 수 없습니다.")
        return

    content = input("내용: ").strip()
    if not content:
        print("내용은 비워둘 수 없습니다.")
        return

    category = choose_category()
    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False,
        "views": 0
    }
    prompts.append(new_prompt)
    save_prompts()
    print("\n프롬프트가 추가되었습니다!")


def show_list(items=None):
    print("\n=== 프롬프트 목록 ===")
    items = prompts if items is None else items

    if not items:
        print("등록된 프롬프트가 없습니다.")
        return

    for i, p in enumerate(items, 1):
        star = " ⭐" if p["favorite"] else ""
        print(f"{i}. [{p['category']}] {p['title']}{star} (조회 {p['views']}회)")

    print(f"\n총 {len(items)}개의 프롬프트")


def select_prompt_index():
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return None

    show_list()
    choice = input("\n프롬프트 번호 입력: ").strip()

    if not choice.isdigit():
        print("올바른 숫자를 입력해주세요.")
        return None

    idx = int(choice) - 1
    if not 0 <= idx < len(prompts):
        print("존재하지 않는 번호입니다.")
        return None

    return idx


def show_by_category():
    print("\n=== 카테고리별 조회 ===")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"{i}) {cat}")

    choice = input("선택: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(CATEGORIES)):
        print("잘못된 선택입니다.")
        return

    selected_category = CATEGORIES[int(choice) - 1]
    matched = [p for p in prompts if p["category"] == selected_category]

    print(f"\n[{selected_category}] 카테고리 프롬프트:")
    if not matched:
        print("해당 카테고리에 프롬프트가 없습니다.")
        return

    for i, p in enumerate(matched, 1):
        star = " ⭐" if p["favorite"] else ""
        print(f"{i}. {p['title']}{star} (조회 {p['views']}회)")

    print(f"\n총 {len(matched)}개의 프롬프트")


def search_prompt():
    print("\n=== 프롬프트 검색 ===")
    keyword = input("검색어: ").strip().lower()

    if not keyword:
        print("검색어를 입력해주세요.")
        return

    results = [
        p for p in prompts
        if keyword in p["title"].lower()
        or keyword in p["content"].lower()
        or keyword in p["category"].lower()
    ]

    print("\n검색 결과:")
    if not results:
        print("검색 결과가 없습니다.")
        return

    for i, p in enumerate(results, 1):
        star = " ⭐" if p["favorite"] else ""
        print(f"{i}. [{p['category']}] {p['title']}{star} (조회 {p['views']}회)")

    print(f"\n{len(results)}개의 프롬프트를 찾았습니다.")


def show_detail():
    print("\n=== 프롬프트 상세 보기 ===")
    idx = select_prompt_index()

    if idx is None:
        return

    p = prompts[idx]

    # 상세 보기 자체를 사용 기록으로 간주
    p["views"] += 1
    save_prompts()

    star = "⭐" if p["favorite"] else "없음"

    print("\n" + "─" * 40)
    print(f"제목: {p['title']}")
    print(f"카테고리: {p['category']}")
    print(f"즐겨찾기: {star}")
    print(f"조회수: {p['views']}회")
    print("─" * 40)
    print("내용:")
    print(p["content"])
    print("─" * 40)


def manage_favorites():
    print("\n=== 즐겨찾기 관리 ===")
    idx = select_prompt_index()

    if idx is None:
        return

    p = prompts[idx]
    p["favorite"] = not p["favorite"]
    save_prompts()

    status = "추가" if p["favorite"] else "해제"
    print(f"'{p['title']}' 프롬프트를 즐겨찾기에 {status}했습니다!")


def show_favorites():
    print("\n=== 즐겨찾기 목록 ===")
    favorites = [p for p in prompts if p["favorite"]]

    if not favorites:
        print("즐겨찾기된 프롬프트가 없습니다.")
        return

    for i, p in enumerate(favorites, 1):
        print(f"{i}. [{p['category']}] {p['title']} ⭐ (조회 {p['views']}회)")

    print(f"\n총 {len(favorites)}개의 즐겨찾기")


def edit_prompt():
    print("\n=== 프롬프트 수정 ===")
    idx = select_prompt_index()

    if idx is None:
        return

    p = prompts[idx]

    print("\n현재 정보")
    print(f"제목: {p['title']}")
    print(f"내용: {p['content']}")
    print(f"카테고리: {p['category']}")

    new_title = input("\n새 제목 (Enter = 유지): ").strip()
    new_content = input("새 내용 (Enter = 유지): ").strip()

    print("\n카테고리를 변경하려면 입력하세요.")
    print("Enter를 누르면 기존 카테고리를 유지합니다.")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"{i}) {cat}")

    category_choice = input("새 카테고리: ").strip()

    if new_title:
        p["title"] = new_title

    if new_content:
        p["content"] = new_content

    if category_choice:
        if category_choice.isdigit() and 1 <= int(category_choice) <= len(CATEGORIES):
            p["category"] = CATEGORIES[int(category_choice) - 1]
        elif category_choice in CATEGORIES:
            p["category"] = category_choice
        else:
            p["category"] = category_choice

    save_prompts()
    print("\n프롬프트가 수정되었습니다.")


def delete_prompt():
    print("\n=== 프롬프트 삭제 ===")
    idx = select_prompt_index()

    if idx is None:
        return

    p = prompts[idx]
    confirm = input(f"'{p['title']}'을(를) 정말 삭제하시겠습니까? (y/n): ").strip().lower()

    if confirm == "y":
        deleted = prompts.pop(idx)
        save_prompts()
        print(f"'{deleted['title']}' 프롬프트가 삭제되었습니다.")
    else:
        print("삭제를 취소했습니다.")


def show_top_views():
    print("\n=== 조회수 TOP 목록 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    top = sorted(prompts, key=lambda p: p["views"], reverse=True)

    for rank, p in enumerate(top, 1):
        star = " ⭐" if p["favorite"] else ""
        print(
            f"{rank}. [{p['category']}] {p['title']}"
            f"{star} - 조회 {p['views']}회"
        )


def export_markdown():
    print("\n=== 카테고리별 Markdown 내보내기 ===")

    if not prompts:
        print("내보낼 프롬프트가 없습니다.")
        return

    EXPORT_DIR.mkdir(exist_ok=True)

    grouped = defaultdict(list)
    for p in prompts:
        grouped[p["category"]].append(p)

    created_files = []

    for category, items in grouped.items():
        safe_category = "".join(
            c for c in category if c not in '\\/:*?"<>|'
        ).strip() or "기타"

        file_path = EXPORT_DIR / f"{safe_category}.md"

        with file_path.open("w", encoding="utf-8") as f:
            f.write(f"# {category} 프롬프트 모음\n\n")

            for number, p in enumerate(items, 1):
                favorite = "⭐" if p["favorite"] else ""
                f.write(f"## {number}. {p['title']} {favorite}\n\n")
                f.write(f"- **카테고리:** {p['category']}\n")
                f.write(f"- **조회수:** {p['views']}회\n\n")
                f.write("### 프롬프트\n\n")
                f.write(f"> {p['content'].replace(chr(10), chr(10) + '> ')}\n\n")
                f.write("---\n\n")

        created_files.append(file_path)

    print(f"\n{len(created_files)}개의 Markdown 파일을 내보냈습니다.")
    print(f"저장 위치: {EXPORT_DIR.resolve()}")


def main():
    while True:
        show_menu()
        menu = input("선택: ").strip()

        if menu == "1":
            add_prompt()
        elif menu == "2":
            show_list()
        elif menu == "3":
            show_by_category()
        elif menu == "4":
            search_prompt()
        elif menu == "5":
            show_detail()
        elif menu == "6":
            manage_favorites()
        elif menu == "7":
            show_favorites()
        elif menu == "8":
            edit_prompt()
        elif menu == "9":
            delete_prompt()
        elif menu == "10":
            show_top_views()
        elif menu == "11":
            save_prompts()
            print(f"\n프롬프트를 '{DATA_FILE}'에 저장했습니다.")
        elif menu == "12":
            export_markdown()
        elif menu == "0":
            save_prompts()
            print("\n프로그램을 종료합니다. 감사합니다!")
            break
        else:
            print("\n잘못된 번호입니다. 다시 선택해주세요.")


if __name__ == "__main__":
    main()
