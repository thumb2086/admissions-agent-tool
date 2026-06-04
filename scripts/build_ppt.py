"""備審 PPT 產生器 — Agent 請修改此檔案

使用方法：
  1. Agent 讀取 ../profile.md 取得使用者資料
  2. 將下方所有 {{PLACEHOLDER}} 取代為實際內容
  3. 每段新增文字上方加上 # TRUTH: profile.md → 章節代號
  4. 執行 python build_ppt.py
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pptx_engine import *
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.chart import XL_CHART_TYPE

# ============================================================
# DIRECTORIES — Agent 請勿修改
# ============================================================
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGES_DIR = os.path.join(ROOT, "images")
OUTPUT_DIR = os.path.join(ROOT, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def img(filename):
    return os.path.join(IMAGES_DIR, filename)

# ============================================================
# 個人資料（Agent 請從 profile.md 填入，不得額外發明）
# ============================================================
# TRUTH: profile.md → 1.1
STUDENT_NAME_ZH = "{{NAME_ZH}}"
# TRUTH: profile.md → 1.2
STUDENT_NAME_EN = "{{NAME_EN}}"
# TRUTH: profile.md → 1.3
STUDENT_SCHOOL = "{{SCHOOL}}"
# TRUTH: profile.md → 1.4
STUDENT_DEPT = "{{DEPARTMENT}}"
# TRUTH: profile.md → 1.6
STUDENT_EMAIL = "{{EMAIL}}"
# TRUTH: profile.md → 1.7
STUDENT_GITHUB = "{{GITHUB}}"
# TRUTH: profile.md → 1.9
HEADSHOT_FILE = img("{{HEADSHOT_FILENAME}}")

# ============================================================
# 目標校系（Agent 請從 profile.md 填入）
# ============================================================
# TRUTH: profile.md → 2.1
TARGET_SCHOOL = "{{TARGET_SCHOOL}}"
# TRUTH: profile.md → 2.2
TARGET_DEPT = "{{TARGET_DEPARTMENT}}"
# TRUTH: profile.md → 2.3
TARGET_GROUP = "{{TARGET_GROUP}}"

# ============================================================
# 主打專題資料（Agent 請從 profile.md 填入）
# ============================================================
# TRUTH: profile.md → 3.1
PROJECT_NAME = "{{PROJECT_NAME_ZH}}"
# TRUTH: profile.md → 3.3
PROJECT_DATES = "{{PROJECT_START}} ~ {{PROJECT_END}}"
# TRUTH: profile.md → 3.4
PROJECT_DURATION = "{{PROJECT_DURATION}}"
# TRUTH: profile.md → 3.5
PROJECT_TEAM_SIZE = "{{PROJECT_TEAM_SIZE}}"
# TRUTH: profile.md → 3.6
PROJECT_ROLE = "{{PROJECT_ROLE}}"
# TRUTH: profile.md → 3.8
PROJECT_GITHUB = "{{PROJECT_GITHUB}}"

# ---- 技術細節 ----
# TRUTH: profile.md → 4.1
HW_LIST = [
    "{{HW_PART_1}}",
    "{{HW_PART_2}}",
]
# TRUTH: profile.md → 4.2
SW_LIST = [
    "{{SW_TOOL_1}}",
    "{{SW_TOOL_2}}",
]
# TRUTH: profile.md → 4.3
COMM_PROTOCOL = "{{COMM_PROTOCOL}}"
# TRUTH: profile.md → 4.5
GIT_COMMITS = "{{GIT_COMMITS}}"

# ---- 動機 & 貢獻 ----
# TRUTH: profile.md → 5.1
MOTIVATION = "{{MOTIVATION_ORIGINAL}}"
# TRUTH: profile.md → 5.2
PROBLEM = "{{PROBLEM_STATEMENT}}"
# TRUTH: profile.md → 5.4 / 5.5
SURVEY_RESULTS = [
    "{{SURVEY_RESULT_1}}",
    "{{SURVEY_RESULT_2}}",
]
# TRUTH: profile.md → 6.2
HW_CONTRIB = [
    "{{HW_CONTRIB_1}}",
    "{{HW_CONTRIB_2}}",
    "{{HW_CONTRIB_3}}",
]
# TRUTH: profile.md → 6.3
SW_CONTRIB = [
    "{{SW_CONTRIB_1}}",
    "{{SW_CONTRIB_2}}",
    "{{SW_CONTRIB_3}}",
]

# ---- 困難故事 ----
# TRUTH: profile.md → 7.1 / 7.2
DIFFICULTY_STORY = "{{DIFFICULTY_1_STORY}}"

# ---- 反思 ----
# TRUTH: profile.md → 8.1
LESSONS = [
    "{{LESSON_1}}",
    "{{LESSON_2}}",
    "{{LESSON_3}}",
]

# ---- 證明圖片 ----
# TRUTH: profile.md → 9.1
PROJECT_PHOTOS = [
    "{{PHOTO_1_FILENAME}}",
    "{{PHOTO_2_FILENAME}}",
    "{{PHOTO_3_FILENAME}}",
    "{{PHOTO_4_FILENAME}}",
    "{{PHOTO_5_FILENAME}}",
]

# ============================================================
# 競賽獎項（Agent 請從 profile.md 填入）
# ============================================================
# TRUTH: profile.md → 10.1 / 10.4
AWARD_1 = "{{AWARD_1_NAME}} — {{AWARD_1_RANK}}"
# TRUTH: profile.md → 10.2
AWARD_1_ORG = "{{AWARD_1_ORGANIZER}}"
# TRUTH: profile.md → 10.7
AWARD_1_CERT = img("{{AWARD_1_CERT_FILENAME}}")

# ============================================================
# 證照（Agent 請從 profile.md 填入）
# ============================================================
# TRUTH: profile.md → 11.1
CERT_1 = "{{CERT_1_NAME}}"
# TRUTH: profile.md → 11.2
CERT_1_ORG = "{{CERT_1_ISSUER}}"
# TRUTH: profile.md → 11.5
CERT_1_FILE = img("{{CERT_1_FILENAME}}")

# ============================================================
# 課外活動（Agent 請從 profile.md 填入）
# ============================================================
# TRUTH: profile.md → 12.1
ACTIVITY_1 = "{{ACTIVITY_1_NAME}}"
# TRUTH: profile.md → 12.3
ACTIVITY_1_DATE = "{{ACTIVITY_1_DATE_HOURS}}"

# ============================================================
# 就讀動機（Agent 請從 profile.md 填入）
# ============================================================
# TRUTH: profile.md → 13.1
MOTIVATION_STATEMENT = "{{MOTIVATION_STATEMENT}}"
# TRUTH: profile.md → 13.2
KEY_LABELS = [
    "{{KEY_LABEL_1}}",
    "{{KEY_LABEL_2}}",
    "{{KEY_LABEL_3}}",
]
# TRUTH: profile.md → 13.3
COLLEGE_PLAN = "{{COLLEGE_PLAN}}"
# TRUTH: profile.md → 13.4
LONG_TERM_GOAL = "{{LONG_TERM_GOAL}}"


# ============================================================
# PPT 產生函式
# ============================================================

def build_project_ppt():
    """B-1a: 專題實作投影片"""
    prs = new_presentation()
    s = prs.slides.add_slide(prs.slide_layouts[6])
    add_cover(s, f"B-1 專題實作\n{PROJECT_NAME}")

    s = prs.slides.add_slide(prs.slide_layouts[6])
    # TRUTH: profile.md → 目錄項目（根據實際內容設計）
    add_toc(s, [
        ("01", "研究動機與目的", ""),
        ("02", "硬體架構與通訊", ""),
        ("03", "機械機構設計", ""),
        ("04", "App 功能頁面", ""),
        ("05", "團隊分工與貢獻", ""),
        ("06", "開發規模", ""),
        ("07", "反思與學習", ""),
    ], highlight_text=PROJECT_NAME, photo_path=img(PROJECT_PHOTOS[0]) if PROJECT_PHOTOS else None)

    # 研究動機與目的
    s = prs.slides.add_slide(prs.slide_layouts[6])
    add_title(s, "研究動機與目的")
    # TRUTH: profile.md → 5.1, 5.2
    add_multiline_text(s, 0.8, 1.6, 5.7, 5.5, [
        MOTIVATION,
        "",
        PROBLEM,
    ], font_size=16)

    # 硬體架構
    s = prs.slides.add_slide(prs.slide_layouts[6])
    add_title(s, "硬體架構與通訊")
    lines = [f"控制核心：{HW_LIST[0]}" if len(HW_LIST) > 0 else ""]
    for hw in HW_LIST[1:]:
        lines.append(hw)
    if COMM_PROTOCOL:
        lines.append("")
        lines.append(f"通訊協定：{COMM_PROTOCOL}")
    # TRUTH: profile.md → 4.1, 4.3
    add_multiline_text(s, 0.8, 1.6, 6.0, 4.0, lines, font_size=18)

    # 圖片以 grid 方式放置
    for i, photo in enumerate(PROJECT_PHOTOS[:4]):
        x = 6.6 + (i % 2) * 3.3
        y = 1.6 + (i // 2) * 2.8
        add_image(s, img(photo), x, y, 3.0)

    # 團隊分工
    s = prs.slides.add_slide(prs.slide_layouts[6])
    add_title(s, "團隊分工與貢獻")
    # TRUTH: profile.md → 6.2, 6.3
    contrib_lines = [f"團隊人數：{PROJECT_TEAM_SIZE}", f"你的角色：{PROJECT_ROLE}", ""]
    for c in HW_CONTRIB:
        contrib_lines.append(f"• {c}")
    for c in SW_CONTRIB:
        contrib_lines.append(f"• {c}")
    add_multiline_text(s, 0.8, 1.6, 5.5, 5, contrib_lines, font_size=16)

    # Git 規模
    s = prs.slides.add_slide(prs.slide_layouts[6])
    add_title(s, "開發規模")
    # TRUTH: profile.md → 4.5, 3.4
    add_multiline_text(s, 0.8, 1.6, 11.5, 4, [
        f"開發期間：{PROJECT_DATES}",
        f"時長：{PROJECT_DURATION}",
        f"總 commits：{GIT_COMMITS}",
    ], font_size=18)

    # 反思
    s = prs.slides.add_slide(prs.slide_layouts[6])
    add_title(s, "反思與學習")
    lesson_lines = []
    for l in LESSONS:
        lesson_lines.append(f"• {l}")
    # TRUTH: profile.md → 8.1
    add_multiline_text(s, 0.8, 1.6, 11.5, 5, lesson_lines, font_size=16)

    # 困難故事
    s = prs.slides.add_slide(prs.slide_layouts[6])
    add_title(s, "開發過程的挑戰")
    # TRUTH: profile.md → 7.2
    add_multiline_text(s, 0.8, 1.6, 11.5, 5.5, [DIFFICULTY_STORY], font_size=16)

    s = prs.slides.add_slide(prs.slide_layouts[6])
    add_ending(s)
    add_footer(prs, f"{STUDENT_NAME_ZH} | {STUDENT_SCHOOL}{STUDENT_DEPT}")

    path = os.path.join(OUTPUT_DIR, "B-1a_專題實作.pptx")
    prs.save(path)
    print(f"[OK] B-1a: {os.path.getsize(path):,} bytes")


def build_cert_award_ppt():
    """C-5/C-7: 競賽與證照投影片"""
    prs = new_presentation()
    s = prs.slides.add_slide(prs.slide_layouts[6])
    add_cover(s, "競賽表現與檢定證照")

    s = prs.slides.add_slide(prs.slide_layouts[6])
    add_toc(s, [
        ("01", "競賽表現", AWARD_1 if AWARD_1 != "{{AWARD_1_NAME}} — {{AWARD_1_RANK}}" else ""),
        ("02", "檢定證照", CERT_1 if CERT_1 != "{{CERT_1_NAME}}" else ""),
    ])

    # 競賽
    s = prs.slides.add_slide(prs.slide_layouts[6])
    add_title(s, "競賽表現")
    # TRUTH: profile.md → 10.1~10.4
    add_multiline_text(s, 0.8, 1.6, 6, 4, [
        f"競賽名稱：{AWARD_1}",
        f"主辦單位：{AWARD_1_ORG}",
    ], font_size=18)
    add_image(s, AWARD_1_CERT, 7.5, 1.6, 4)

    # 證照
    s = prs.slides.add_slide(prs.slide_layouts[6])
    add_title(s, "檢定證照")
    # TRUTH: profile.md → 11.1, 11.2
    add_multiline_text(s, 0.8, 1.6, 6, 4, [
        f"證照：{CERT_1}",
        f"發證單位：{CERT_1_ORG}",
    ], font_size=18)
    add_image(s, CERT_1_FILE, 7.5, 1.6, 4)

    s = prs.slides.add_slide(prs.slide_layouts[6])
    add_ending(s)
    add_footer(prs, f"{STUDENT_NAME_ZH} | {STUDENT_SCHOOL}{STUDENT_DEPT}")

    path = os.path.join(OUTPUT_DIR, "C-5_C-7_競賽證照.pptx")
    prs.save(path)
    print(f"[OK] C: {os.path.getsize(path):,} bytes")


def build_motivation_ppt():
    """D-2: 學習歷程自述 / 就讀動機"""
    prs = new_presentation()
    s = prs.slides.add_slide(prs.slide_layouts[6])
    add_cover(s, "D-2 學習歷程自述", f"{STUDENT_NAME_ZH} · {STUDENT_SCHOOL}")

    s = prs.slides.add_slide(prs.slide_layouts[6])
    add_toc(s, [
        ("01", "學習歷程", "從入學到專題的技術累積"),
        ("02", "就讀動機", f"為什麼選擇{TARGET_SCHOOL}{TARGET_DEPT}"),
        ("03", "未來規劃", "短中長期學習目標"),
    ])

    # 就讀動機
    s = prs.slides.add_slide(prs.slide_layouts[6])
    add_title(s, "就讀動機")
    # TRUTH: profile.md → 13.1, 13.2
    label_lines = [f"• {lbl}" for lbl in KEY_LABELS]
    add_multiline_text(s, 0.8, 1.6, 5.5, 5, [
        MOTIVATION_STATEMENT,
        "",
        "三個關鍵能力：",
        *label_lines,
    ], font_size=18)

    # 未來規劃
    s = prs.slides.add_slide(prs.slide_layouts[6])
    add_title(s, "未來規劃")
    # TRUTH: profile.md → 13.3, 13.4
    add_multiline_text(s, 0.8, 1.6, 5.5, 5, [
        "短期目標：",
        COLLEGE_PLAN,
        "",
        "長期目標：",
        LONG_TERM_GOAL,
    ], font_size=18)

    s = prs.slides.add_slide(prs.slide_layouts[6])
    add_ending(s)
    add_footer(prs, f"{STUDENT_NAME_ZH} | {STUDENT_SCHOOL}{STUDENT_DEPT}")

    path = os.path.join(OUTPUT_DIR, "D-2_學習歷程自述.pptx")
    prs.save(path)
    print(f"[OK] D-2: {os.path.getsize(path):,} bytes")


# ============================================================
# 主程式
# ============================================================
if __name__ == "__main__":
    print("=== 開始產生備審 PPT ===")
    build_project_ppt()
    build_cert_award_ppt()
    build_motivation_ppt()
    print(f"=== 完成！檔案位於: {OUTPUT_DIR} ===")
