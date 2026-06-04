# Admissions Agent Tool

將 OpenCode Agent 變成你的備審資料製作助手。  
透過結構化問卷收集你的個人資料，自動產生台灣技職推甄備審 PPT。

## 運作方式

```
你 Clone 這個 Repo → 用 OpenCode 打開 →
Agent 載入 AGENTS.md → 開始問你問題 →
你回答 → Agent 寫入 profile.md →
Agent 修改 build_ppt.py → 執行 → 產出 PPT
```

## 需求

- Python 3.8+
- `python-pptx`（Agent 會自動安裝）
- OpenCode（建議最新版）

## 目錄結構

```
admissions-agent-tool/
├── AGENTS.md           # Agent 工作流程（核心！）
├── README.md           # 本檔案
├── profile.md          # 個人資料庫模板（Agent 填空）
├── scripts/
│   ├── build_ppt.py    # 主腳本（含 placeholder，Agent 會改）
│   ├── pptx_engine.py  # 共用函式庫（Agent 不動）
│   └── validate.py     # 驗證腳本
├── images/             # 放入你的照片、證明、截圖
├── output/             # 產出的 PPTX 在這裡
├── existing_ppt/       # 如有現成 PPT 可放入參考
└── examples/           # 範例檔案
```

## 快速開始

```bash
# 1. Clone
git clone <repo-url>
cd admissions-agent-tool

# 2. 用 OpenCode 開啟
opencode .

# 3. Agent 會自動開始 Phase 1 問卷流程
#    你只需要回答問題
```

## 完整流程

| Phase | 動作 | 產出 |
|-------|------|------|
| 0 | Agent 載入 AGENTS.md，檢查環境 | 確認 python-pptx 已安裝 |
| 1 | 六輪深度問答 | profile.md 被填寫 |
| 2 | 完整性檢查 | 確定資料足夠進入製作 |
| 3 | Agent 修改 build_ppt.py | 所有 placeholder 被取代 |
| 4 | 執行 python scripts/build_ppt.py | output/ 產生 PPTX |
| 5 | Truth Audit | 每個 claim 都 trace 回 profile.md |

## 反幻覺機制

- Agent **絕不發明**任何資訊
- 每段文字上方會加 `# TRUTH: profile.md → 章節X` 標記來源
- 如果資料不足，Agent 會停下來問你，不會瞎猜
- 最終會有 Truth Audit 確認所有 claim 都有依據

## License

MIT
