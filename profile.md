# 個人資料庫

> 請 Agent 依照 Phase 1 問卷結果填入以下欄位。
> 未填的欄位保留 `{{PLACEHOLDER}}` 格式。
> 此檔案是唯一事實源，所有 PPT 內容必須 trace 至此。

---

## 填寫狀態（Agent 每輪完成後更新）

- Round 1（基本身份）：❌ 未開始 / 🔄 進行中 / ✅ 已完成
- Round 2（目標校系）：❌ 未開始 / 🔄 進行中 / ✅ 已完成
- Round 3（主打專題）：❌ 未開始 / 🔄 進行中 / ✅ 已完成
- Round 4（競賽獎項）：❌ 未開始 / 🔄 進行中 / ✅ 已完成
- Round 5（證照與課外）：❌ 未開始 / 🔄 進行中 / ✅ 已完成
- Round 6（就讀動機）：❌ 未開始 / 🔄 進行中 / ✅ 已完成
- Round 7（實習科目）：❌ 未開始 / 🔄 進行中 / ✅ 已完成

---

## 1. 基本身份

```
1.1 中文姓名：{{NAME_ZH}}
1.2 英文姓名：{{NAME_EN}}
1.3 學校全名：{{SCHOOL}}
1.4 科系全名：{{DEPARTMENT}}
1.5 年級：{{GRADE}}
1.6 Email：{{EMAIL}}
1.7 GitHub 帳號：{{GITHUB}}
1.8 其他連結（網站/作品集/LinkedIn）：{{OTHER_LINKS}}
1.9 大頭照檔案名稱：{{HEADSHOT_FILENAME}}
1.10 手機號碼（選填）：{{PHONE}}
```

## 2. 目標校系

```
2.1 學校全名：{{TARGET_SCHOOL}}
2.2 系所全名：{{TARGET_DEPARTMENT}}
2.3 組別（如有分組）：{{TARGET_GROUP}}
2.4 上傳規定（幾個項目、頁數上限、檔案大小限制）：{{UPLOAD_RULES}}
2.5 截止日期：{{DEADLINE}}
2.6 語言偏好（中文/英文/雙語）：{{LANGUAGE}}
2.7 客製教授姓名（如有）：{{CUSTOM_PROFESSOR}}
2.8 客製教授研究方向：{{CUSTOM_PROFESSOR_FIELD}}
```

## 3. 主打專題 — 基本資訊

```
3.1 專題中文名稱：{{PROJECT_NAME_ZH}}
3.2 專題英文名稱（如有）：{{PROJECT_NAME_EN}}
3.3 起迄時間：{{PROJECT_START}} ~ {{PROJECT_END}}
3.4 總開發天數/月數：{{PROJECT_DURATION}}
3.5 團隊總人數：{{PROJECT_TEAM_SIZE}}
3.6 你的角色：{{PROJECT_ROLE}}
3.7 其他成員姓名與分工：
     {{TEAM_MEMBER_1}}：{{TEAM_MEMBER_1_ROLE}}
     {{TEAM_MEMBER_2}}：{{TEAM_MEMBER_2_ROLE}}
3.8 GitHub 連結：{{PROJECT_GITHUB}}
3.9 其他展示連結：{{PROJECT_DEMO_LINK}}
```

## 4. 主打專題 — 技術細節

```
4.1 硬體零件清單（型號, 用途, 數量）：
     {{HW_PART_1}}
     {{HW_PART_2}}
     {{HW_PART_3}}
     {{HW_PART_4}}
     {{HW_PART_5}}
4.2 軟體/程式語言/框架清單：
     {{SW_TOOL_1}}
     {{SW_TOOL_2}}
     {{SW_TOOL_3}}
4.3 通訊協定（如 BLE/Wi-Fi/自訂）：{{COMM_PROTOCOL}}
4.4 通訊協定版本演進（如 v1.2→v1.3→v1.4）：{{PROTOCOL_VERSIONS}}
4.5 Git 總 commits 數：{{GIT_COMMITS}}
4.6 Git 分支策略：{{GIT_BRANCH_STRATEGY}}
4.7 總程式碼行數（約略）：{{CODE_LINES}}
```

## 5. 主打專題 — 動機與問題

```
5.1 為什麼想做這個專題（原始動機）：{{MOTIVATION_ORIGINAL}}
5.2 要解決的具體問題：{{PROBLEM_STATEMENT}}
5.3 是否有做問卷調查：{{SURVEY_DONE}}
5.4 問卷樣本數：{{SURVEY_SAMPLE_SIZE}}
5.5 問卷具體結果數據：
     {{SURVEY_RESULT_1}}
     {{SURVEY_RESULT_2}}
     {{SURVEY_RESULT_3}}
     {{SURVEY_RESULT_4}}
```

## 6. 主打專題 — 你的具體貢獻

逐條列出你實際做的事情：

```
6.1 貢獻總述：{{CONTRIBUTION_SUMMARY}}
6.2 硬體貢獻：
     - {{HW_CONTRIB_1}}
     - {{HW_CONTRIB_2}}
     - {{HW_CONTRIB_3}}
6.3 軟體貢獻：
     - {{SW_CONTRIB_1}}
     - {{SW_CONTRIB_2}}
     - {{SW_CONTRIB_3}}
6.4 機構/設計貢獻：
     - {{MECH_CONTRIB_1}}
     - {{MECH_CONTRIB_2}}
6.5 你認為貢獻最多的部分：{{BEST_CONTRIBUTION}}
6.6 專題得獎紀錄（如有）：{{PROJECT_AWARD}}
```

## 7. 主打專題 — 困難故事 🔥

每一個故事請包含：時間、地點、發生了什麼、你做了什麼、結果如何。

```
7.1 最大困難標題：{{DIFFICULTY_1_TITLE}}
7.2 最大困難完整經過：
     {{DIFFICULTY_1_STORY}}
7.3 最印象深刻的一晚（標題）：{{MEMORABLE_NIGHT_TITLE}}
7.4 最印象深刻的一晚完整經過：
     {{MEMORABLE_NIGHT_STORY}}
7.5 東西壞掉/燒掉/重來的經驗（標題）：{{FAILURE_TITLE}}
7.6 東西壞掉/燒掉/重來的完整經過：
     {{FAILURE_STORY}}
7.7 3D 列印公差/加工問題故事：
     {{TOLERANCE_STORY}}
7.8 Git 檔案遺失/專案消失故事：
     {{GIT_DISASTER_STORY}}
7.9 團隊合作困難故事（如有）：
     {{TEAM_CONFLICT_STORY}}
```

## 8. 主打專題 — 反思與學習

```
8.1 學到最重要的三件事：
     1. {{LESSON_1}}
     2. {{LESSON_2}}
     3. {{LESSON_3}}
8.2 這個專題展現的能力：{{DEMONSTRATED_SKILLS}}
8.3 如果可以重來會改變什麼：{{CHANGE_IF_REDO}}
```

## 9. 主打專題 — 證明檔案

```
9.1 照片檔案清單（檔名 → 內容描述）：
     - {{PHOTO_1_FILENAME}}：{{PHOTO_1_DESC}}
     - {{PHOTO_2_FILENAME}}：{{PHOTO_2_DESC}}
     - {{PHOTO_3_FILENAME}}：{{PHOTO_3_DESC}}
     - {{PHOTO_4_FILENAME}}：{{PHOTO_4_DESC}}
     - {{PHOTO_5_FILENAME}}：{{PHOTO_5_DESC}}
     - {{PHOTO_6_FILENAME}}：{{PHOTO_6_DESC}}
9.2 簡報/報告/論文 PDF：{{PROJECT_PDF}}
9.3 得獎/專利證明檔案：{{PROJECT_CERT_FILES}}
```

## 10. 競賽獎項

如有多項，請複製以下區塊。

```
--- 競賽 1 ---
10.1 競賽全名：{{AWARD_1_NAME}}
10.2 主辦單位：{{AWARD_1_ORGANIZER}}
10.3 比賽日期：{{AWARD_1_DATE}}
10.4 獎項/名次/分數：{{AWARD_1_RANK}}
10.5 參賽規模（多少人/隊伍）：{{AWARD_1_SCALE}}
10.6 比賽方式（筆試/術科/作品審查）：{{AWARD_1_FORMAT}}
10.7 證明檔案名稱：{{AWARD_1_CERT_FILENAME}}
```

## 11. 證照

如有多項，請複製以下區塊。

```
--- 證照 1 ---
11.1 證照全名：{{CERT_1_NAME}}
11.2 發證單位：{{CERT_1_ISSUER}}
11.3 取得日期：{{CERT_1_DATE}}
11.4 證照號碼（如有）：{{CERT_1_NUMBER}}
11.5 證明檔案名稱：{{CERT_1_FILENAME}}

--- 證照 2 ---
11.6 證照全名：{{CERT_2_NAME}}
11.7 發證單位：{{CERT_2_ISSUER}}
11.8 取得日期：{{CERT_2_DATE}}
11.9 證明檔案名稱：{{CERT_2_FILENAME}}
```

## 12. 課外活動

如有多項，請複製以下區塊。

```
--- 活動 1 ---
12.1 活動名稱：{{ACTIVITY_1_NAME}}
12.2 主辦單位：{{ACTIVITY_1_ORGANIZER}}
12.3 日期/時數：{{ACTIVITY_1_DATE_HOURS}}
12.4 你學到什麼：{{ACTIVITY_1_LEARNING}}
12.5 證明檔案名稱：{{ACTIVITY_1_CERT_FILENAME}}
```

## 13. 就讀動機與個人定位

```
13.1 為什麼想念這個系：{{MOTIVATION_STATEMENT}}
13.2 三個關鍵能力或定位：
     1. {{KEY_LABEL_1}}
     2. {{KEY_LABEL_2}}
     3. {{KEY_LABEL_3}}
13.3 大學四年規劃：{{COLLEGE_PLAN}}
13.4 長期目標：{{LONG_TERM_GOAL}}
13.5 想對審查教授說的話（選填）：{{MESSAGE_TO_PROFESSOR}}
```

## 14. 其他作品（選填）

如有多項，請複製以下區塊。

```
--- 作品 1 ---
14.1 作品名稱：{{OTHER_PROJECT_NAME}}
14.2 技術棧：{{OTHER_PROJECT_TECH}}
14.3 GitHub/展示連結：{{OTHER_PROJECT_LINK}}
14.4 你的貢獻：{{OTHER_PROJECT_CONTRIBUTION}}
14.5 照片/截圖檔案：{{OTHER_PROJECT_IMAGES}}
```

## 15. 實習科目（B-1b 用）

```
15.1 修過的實習課程：
     {{INTERNSHIP_COURSE_1}}
     {{INTERNSHIP_COURSE_2}}
15.2 各課程作品：
     {{INTERNSHIP_WORK_1}}
     {{INTERNSHIP_WORK_2}}
15.3 實習學到最重要的技能/觀念：{{INTERNSHIP_LESSON}}
15.4 印象深刻的事：{{INTERNSHIP_STORY}}
15.5 實習作品照片檔名：
     {{INTERNSHIP_PHOTO_1}}
     {{INTERNSHIP_PHOTO_2}}
```

## 16. 手繪製圖（B-2a 用）

```
16.1 手繪作品名稱：{{HANDDRAFT_WORK_1}}, {{HANDDRAFT_WORK_2}}, {{HANDDRAFT_WORK_3}}
16.2 學習心得：{{HANDDRAFT_REFLECTION}}
16.3 作品照片檔名：
     {{HANDDRAFT_PHOTO_1}}
     {{HANDDRAFT_PHOTO_2}}
```

## 17. 電腦輔助製圖（B-2b 用）

```
17.1 學習軟體：{{CAD_WORK_1}}, {{CAD_WORK_2}}
17.2 檢定/證照：{{CAD_CERT_NAME}}
17.3 學習心得：{{CAD_REFLECTION}}
```

## 18. 3D 建模作品（B-2c 用）

```
18.1 建模作品：{{MODEL_WORK_1}}, {{MODEL_WORK_2}}
18.2 使用軟體：{{MODEL_SOFTWARE}}
```

## 19. 彈性學習（C-1 用）

```
19.1 彈性學習名稱：{{FLEXIBLE_LEARNING_NAME}}
19.2 時數/期間：{{FLEXIBLE_HOURS}}
19.3 心得：{{FLEXIBLE_REFLECTION}}
```

## 20. 多元表現綜整心得（D-1 用）

```
20.1 綜整自述（約 300-500 字總結三年學習）：
     {{SUMMARY_TEXT}}
```

