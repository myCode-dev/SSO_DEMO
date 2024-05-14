from flask import Flask, render_template, redirect, session, request, url_for
import requests
import base64
from datetime import datetime
import secrets
from dotenv import load_dotenv
import os
import http.cookies

# 加载dotenv文件
load_dotenv()

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# NCU Portal OAuth 相關資訊
client_id = os.getenv('CLIENT_ID')  # 客戶端ID
client_secret = os.getenv('CLIENT_SECRET')  # 客戶端密鑰
authorization_url = os.getenv('AUTHORIZATION_URL')  # 授權URL
token_url = os.getenv('TOKEN_URL') # Token獲取URL
user_info_url = os.getenv('USER_INFO_URL')  # 使用者資訊獲取URL
callback_url = os.getenv('CALLBACK_URL')  # 回調URL

# 定義首頁路由
@app.route('/')
def index():
    return render_template("index.html")


# 用於生成 OAuth2 認證連結的路由
@app.route('/login')
def login():
    scopes = 'chinese-name student-id email identifier academy-records'  # 請求使用者資訊的Scope
    auth_url = f"{authorization_url}?response_type=code&client_id={client_id}&redirect_uri={callback_url}&scope={scopes}"
    return redirect(auth_url)


# 定義登出路由
@app.route('/logout')
def logout():
    session.pop('ncu_token', None)    
    return redirect('/')  # 將用戶重定向到登錄頁面


# 接收 OAuth2 認證回調的路由
@app.route('/callback')
def callback():
    # 獲取Authorization Code
    code = request.args.get('code')
    
    # 使用Authorization Code換取Access Token
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Basic ' + base64.b64encode((client_id + ':' + client_secret).encode()).decode()
    }
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': callback_url
    }
    response = requests.post(token_url, headers=headers, data=data)
    token_data = response.json()
    print(token_data)
    access_token = token_data.get('access_token')
    session['ncu_token'] = access_token

    if access_token:
        # 使用Access Token獲取使用者資訊
        headers = {
            'Authorization': 'Bearer ' + access_token
        }
        response = requests.get(user_info_url, headers=headers)
        user_info = response.json()
        print(user_info)

        # 獲取當前日期和時間
        now = datetime.now()
        
        if(user_info['accountType'] == "STUDENT"):
            return render_template("kanban.html", user_data=user_info, year=now.year, month=now.month, day=now.day)
        else:
            return render_template("welcome.html", user_data=user_info, year=now.year, month=now.month, day=now.day)
    else:
        return redirect('/logout')

if __name__ == '__main__':
    app.run(debug=True)
