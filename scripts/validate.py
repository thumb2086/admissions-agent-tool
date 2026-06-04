"""驗證腳本 — 檢查 profile 完整性 + 圖片存在 + 產出檔案"""

import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILE_PATH = os.path.join(ROOT, "profile.md")
BUILD_SCRIPT = os.path.join(ROOT, "scripts", "build_ppt.py")
IMAGES_DIR = os.path.join(ROOT, "images")
OUTPUT_DIR = os.path.join(ROOT, "output")


def check_placeholders(filepath):
    """掃描檔案中殘留的 {{PLACEHOLDER}} 模式"""
    if not os.path.exists(filepath):
        return [f"[MISSING] 檔案不存在: {filepath}"]
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    placeholders = re.findall(r"\{\{[A-Z_0-9]+\}\}", content)
    return placeholders


def check_profile_completeness():
    """檢查 profile.md 的 MUST HAVE 欄位"""
    if not os.path.exists(PROFILE_PATH):
        print("[FAIL] profile.md 不存在")
        return False

    with open(PROFILE_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # MUST HAVE 欄位清單
    must_have = [
        ("NAME_ZH", "中文姓名"),
        ("NAME_EN", "英文姓名"),
        ("SCHOOL", "學校"),
        ("DEPARTMENT", "科系"),
        ("TARGET_SCHOOL", "目標學校"),
        ("TARGET_DEPARTMENT", "目標系所"),
        ("PROJECT_NAME_ZH", "專題名稱"),
        ("PROJECT_START", "專題起始時間"),
        ("PROJECT_ROLE", "專題角色"),
    ]

    all_ok = True
    for code, label in must_have:
        pattern = f"{{{{code}}}}"
        if pattern in content:
            print(f"[WARN] MUST HAVE 未填: {label} ({code})")
            all_ok = False
        else:
            print(f"[OK] {label} 已填寫")

    return all_ok


def check_images():
    """掃描 build_ppt.py 中所有圖片路徑，確認檔案存在"""
    if not os.path.exists(BUILD_SCRIPT):
        print("[FAIL] build_ppt.py 不存在")
        return False

    with open(BUILD_SCRIPT, "r", encoding="utf-8") as f:
        content = f.read()

    # 找出所有 img("...") 呼叫
    img_refs = re.findall(r'img\("([^"]+)"\)', content)
    # 加上 PROJECT_PHOTOS 清單中的檔名
    photo_assign = re.findall(r'"([^"]+\.(jpg|jpeg|png|JPG|JPEG|PNG))"', content)
    for match in photo_assign:
        img_refs.append(match[0])

    missing = []
    for ref in set(img_refs):
        path = os.path.join(IMAGES_DIR, ref)
        if not os.path.exists(path):
            missing.append(ref)

    if missing:
        print(f"\n⚠️  缺失圖片 ({len(missing)} 張):")
        for m in missing:
            print(f"  - images/{m}")
    else:
        print("\n[OK] 所有圖片皆存在")

    return len(missing) == 0


def check_output():
    """確認 output/ 有產出檔案"""
    if not os.path.exists(OUTPUT_DIR):
        print("[FAIL] output/ 目錄不存在")
        return False

    files = [f for f in os.listdir(OUTPUT_DIR) if f.endswith(".pptx")]
    if not files:
        print("[FAIL] output/ 沒有任何 PPTX 檔案")
        return False

    print(f"\n📁 output/ 目錄產出 ({len(files)} 個檔案):")
    for f in sorted(files):
        size = os.path.getsize(os.path.join(OUTPUT_DIR, f))
        print(f"  - {f} ({size:,} bytes)")
    return True


def check_remaining_placeholders():
    """檢查 build_ppt.py 中殘留的 {{PLACEHOLDER}}"""
    placeholders = check_placeholders(BUILD_SCRIPT)
    if placeholders:
        print(f"\n⚠️  殘留未取代的 Placeholder ({len(placeholders)} 個):")
        for p in sorted(set(placeholders)):
            print(f"  - {p}")
        return False
    else:
        print("\n[OK] 所有 Placeholder 皆已取代")
        return True


def run_all():
    print("=" * 50)
    print("  Admissions Agent Tool — 驗證腳本")
    print("=" * 50)

    print("\n--- [1/5] Profile 完整性檢查 ---")
    profile_ok = check_profile_completeness()

    print("\n--- [2/5] Placeholder 殘留檢查 ---")
    placeholder_ok = check_remaining_placeholders()

    print("\n--- [3/5] 圖片存在檢查 ---")
    images_ok = check_images()

    print("\n--- [4/5] 產出檔案檢查 ---")
    output_ok = check_output()

    print("\n--- [5/5] Truth Audit 摘要 ---")
    truth_count = 0
    if os.path.exists(BUILD_SCRIPT):
        with open(BUILD_SCRIPT, "r", encoding="utf-8") as f:
            truth_count = f.read().count("# TRUTH:")
    print(f"  - {truth_count} 個 TRUTH claims")

    print("\n" + "=" * 50)
    results = [profile_ok, placeholder_ok, images_ok, output_ok]
    if all(results):
        print("  ✅ 全部通過！備審 PPT 已就緒。")
    else:
        failed = sum(1 for r in results if not r)
        print(f"  ⚠️  {failed} 項檢查未通過，請修正後重新執行。")
    print("=" * 50)


if __name__ == "__main__":
    run_all()
