# 2025-cloud-native-hw1

## System Introduction
這是2025雲原生第一次作業，我建立了三層邏輯（presentation, application, persistence）來達到目的。


## System Requirements
請確保您的環境符合以下條件：

- **Python 版本**：Python 3.12+
- **作業系統**：macOS / Windows（已測試）

### 確認 Python 版本
python --version
如果 Python 版本 **低於 3.12**，請升級。

---

## Installation
### 下載專案（從 GitHub 或壓縮包解壓縮）
git clone https://github.com/jushengtin2/2025-cloud-native-hw1
cd 2025-cloud-native-hw1

### 執行建置（格式化程式碼 & 檢查）
./build.sh  # Linux/macOS
sh build.sh  # Windows（使用 Git Bash）

---

## Running the Application（執行專案）
###  執行 CLI 應用程式
./run.sh  # Linux/macOS
sh run.sh  # Windows（使用 Git Bash）

### 手動執行（若不使用 `run.sh`）
python3 presentation.py or python presentation.py

---

## Features（功能列表）
| 指令 | 說明 |
|------|------|
| REGISTER <username> | 註冊新使用者 |
| CREATE_LISTING <username> <title> <description> <price> <category> | 建立商品 |
| DELETE_LISTING <username> <listing_id> | 刪除商品 |
| GET_LISTING <username> <listing_id> | 查詢商品資訊 |
| GET_CATEGORY <username> <category> | 查詢某分類的商品（時間排序） |
| GET_TOP_CATEGORY <username> | 取得最多商品的分類 |
| EXIT | 退出程式 |

---
