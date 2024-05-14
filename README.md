# NCU PORTAL OAuth 2.0串接範例
這個範例程式展示了如何在Python Flask應用程式中串接NCU PORTAL的OAuth 2.0授權機制，並獲取使用者資訊。

## 使用技術
Python
Flask框架

## 串接文件
文件: https://github.com/ncucc/portal4g-doc

## 操作說明

### 1. Clone專案到本地

首先，將專案克隆到本地。開啟終端並執行以下命令：
```bash
git clone https://github.com/Celia-code/SSO_DEMO.git
```
進入專案目錄：
```bash
cd project
```
### 2. 設置環境變數
專案使用 .env 檔案來設置環境變數。首先，複製示例環境變數文件 example.env 並命名為 .env：
```bash
copy example.env .env
```
打開 .env 文件，修改其中的環境變數。
- CLIENT_ID:NCU Portal提供的Client ID
- CLIENT_SECRET:NCU Portal提供的Client Secret
- CALLBACK_URL: 重定向的網頁連結
- AUTHORIZATION_URL: OAuth單一簽入入口 (https://portal.ncu.edu.tw/oauth2/authorization)
- TOKEN_URL: OAuth 取得 Access Token 入口 (https://portal.ncu.edu.tw/oauth2/token)
- USER_INFO_URL: 使用者資訊入口 (https://portal.ncu.edu.tw/apis/oauth/v1/info)

### 3. 安裝依賴
```bash
pip install -r requirements.txt
```

### 4. 執行專案
```bash
python main.py
```

