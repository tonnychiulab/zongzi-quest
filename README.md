# 粽情冒險 Zongzi Quest

> 端午節限定版 — 基於 [Sharkie](https://github.com/davidhckh/sharkie-game) 改作

一款橫向卷軸冒險遊戲。控制可愛的鯊魚穿越海洋，收集三種台灣粽子、搭配沾醬觸發加成，最終擊敗大魔王！

**Play Online:** [GitHub Pages](https://tonnychiulab.github.io/zongzi-quest/)

---

## 玩法說明

### 操控

| 按鍵 | 動作 |
|------|------|
| `←` `→` / `A` `D` | 移動 |
| `Space` / `↑` / `W` | 跳躍 |
| `X` | 射出泡泡 |
| `Y` | 鰭拍攻擊 |

### 目標

1. 收集地圖上的 **20 顆粽子** 累積分數
2. 蒐集 **沾醬道具**（砂糖或醬油），配上鹼粽觸發特殊加成
3. 集滿所有沾醬，解鎖毒泡泡 — 擊敗大魔王！

---

## 粽子圖鑑

| 種類 | 顏色 | 分數 | 特殊效果 |
|------|------|------|---------|
| 北部粽 | 草綠 | +1 | 蒸煮清爽，無特效 |
| 南部粽 | 深棕 | +2 | 炭火紮實，收集即回血 +5 HP |
| 鹼粽 | 黃金光暈 | +3 | 攜帶沾醬時觸發加成 |

### 沾醬機制

撿到沾醬後進入 **10 秒蓄力狀態**，在蓄力期間再撿鹼粽即可觸發：

| 沾醬 | 搭鹼粽效果 |
|------|-----------|
| 砂糖 | 甜蜜加持：回血 +20 HP |
| 醬油 | 鮮鹹爆發：速度 ×1.8，持續 5 秒 |

---

## 快速開始

### 本地執行

```bash
git clone https://github.com/tonnychiulab/zongzi-quest.git
cd zongzi-quest
python -m http.server 8000
```

開啟瀏覽器前往 `http://localhost:8000`

> **需求：** 現代瀏覽器（Chrome / Firefox / Edge）、Python 3（本地伺服器用）

### GitHub Pages 部署

1. 將專案 Push 至你的 GitHub repo
2. 進入 Settings → Pages → Source 選擇 `main` 分支根目錄
3. 儲存後即可透過 `https://your-username.github.io/repo-name/` 遊玩

---

## 技術細節

- **純 Vanilla JavaScript (ES6+)** — 無框架依賴
- **HTML5 Canvas** — 2D 硬體加速渲染
- **GSAP 3** — UI 動畫過場
- **Python + Pillow** — 粽子像素風格素材生成（`generate_assets.py`）

### 專案結構

```
zongzi-quest/
├── index.html              # 主頁面
├── script.js               # 遊戲初始化
├── style.css               # 樣式
├── generate_assets.py      # 素材生成腳本（開發用）
├── game/
│   ├── entities/
│   │   ├── zongzi.class.js     # 粽子（北部/南部/鹼粽）
│   │   ├── condiment.class.js  # 沾醬（砂糖/醬油）
│   │   ├── character.class.js  # 鯊魚角色
│   │   ├── boss.class.js       # 大魔王
│   │   └── ...
│   ├── ui.class.js         # 介面（粽子計分、沾醬蓄力提示）
│   ├── level.class.js      # 關卡配置
│   └── world.class.js      # 世界渲染
└── assets/
    ├── items/
    │   ├── north-zongzi/   # 北部粽動畫幀
    │   ├── south-zongzi/   # 南部粽動畫幀
    │   ├── alkaline-zongzi/ # 鹼粽動畫幀（8幀呼吸光暈）
    │   ├── sugar-animated/ # 砂糖動畫幀
    │   └── soysauce-animated/ # 醬油動畫幀
    ├── icons/
    │   ├── zongzi-icon.png
    │   └── condiment-icon.png
    └── ...
```

---

## 與原版差異

| 原版 Sharkie | 粽情冒險 |
|-------------|---------|
| 金幣（20 個，各 +1 分） | 三種粽子（+1 / +2 / +3 分） |
| 毒藥瓶（解鎖毒泡泡） | 沾醬道具（砂糖/醬油，另有配對加成） |
| 英文介面 | 繁體中文介面 |
| "Sharkie" 標題 | "粽情冒險" 端午節主題 |

---

## 致謝

本遊戲基於 **[davidhckh](https://github.com/davidhckh)** 的開源作品 [Sharkie](https://github.com/davidhckh/sharkie-game) 改作，遵循 MIT 授權。

原作提供了完整的遊戲引擎架構、角色動畫素材、音效系統與關卡設計，是非常優秀的 Vanilla JS 遊戲專案，非常感謝原作者的開源貢獻。

---

## 授權

本改作依循原作者授權，以 **MIT License** 開源，詳見 [LICENSE](LICENSE)。

- 原始版權 © 2021 [David](https://github.com/davidhckh)
- 改作版權 © 2026 [Tonny](https://github.com/tonnychiulab)

原始碼歡迎 Fork 與再改作，若你做了有趣的版本，歡迎開 Issue 分享！
