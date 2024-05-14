from flask import Flask, render_template, redirect, session, request, url_for
import requests
from urllib.parse import urlencode

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 請修改成您自己的密鑰

# NCU Portal OAuth 相關資訊
CLIENT_ID = '20240409132753m27OXYK5tuKF'
CLIENT_SECRET = 'vG5pUtTzulSgCwHkuCh8Bqut7DaheVo87SJ97jt2Akha1XRscFe'
AUTHORIZATION_URL = 'https://portal.ncu.edu.tw/oauth2/authorization'
TOKEN_URL = 'https://portal.ncu.edu.tw/oauth2/token'
USER_INFO_URL = 'https://portal.ncu.edu.tw/apis/oauth/v1/info'
CALLBACK_URL = 'http://127.0.0.1:5000/callback'

class PortalProvider:
    def __init__(self, client_id, client_secret, authorization_url, token_url, user_info_url):
        self.client_id = client_id
        self.client_secret = client_secret
        self.authorization_url = authorization_url
        self.token_url = token_url
        self.user_info_url = user_info_url

    def get_authorization_url(self):
        params = {
            'response_type': 'code',
            'client_id': self.client_id,
            'redirect_uri': CALLBACK_URL,
            'scope': 'chinese-name student-id email identifier academy-records'
        }
        return f"{self.authorization_url}?{urlencode(params)}"

    def get_access_token(self, code):
        data = {
            'grant_type': 'authorization_code',
            'code': code,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'redirect_uri': CALLBACK_URL
        }
        response = requests.post(self.token_url, data=data)
        return response.json().get('access_token')

    def get_user_info(self, access_token):
        headers = {'Authorization': f'Bearer {access_token}'}
        response = requests.get(self.user_info_url, headers=headers)
        return response.json()

provider = PortalProvider(CLIENT_ID, CLIENT_SECRET, AUTHORIZATION_URL, TOKEN_URL, USER_INFO_URL)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    authorization_url = provider.get_authorization_url()
    return redirect(authorization_url)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    if code:
        access_token = provider.get_access_token(code)
        user_info = provider.get_user_info(access_token)
        session['user_info'] = user_info
        return redirect(url_for('profile'))
    else:
        return "Error: Failed to obtain authorization code."

@app.route('/profile')
def profile():
    user_info = session.get('user_info')
    if user_info:
        return render_template('profile.html', user_info=user_info)
    else:
        return "Error: User information not found."

if __name__ == '__main__':
    app.run(debug=True)
