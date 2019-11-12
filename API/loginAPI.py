"""
    封装类：
        封装请求函数
"""
import app


class Login:
    def __init__(self):
        self.login_url = app.BASE_URL + "/api/sys/login"

    # 登录函数
    # 参数：session+mobile+password
    def get_login(self, session, mobile, password):
        my_login = {
            "mobile": mobile,
            "password": password
        }
        return session.post(self.login_url, json=my_login)
