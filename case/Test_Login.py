"""
封装unittest相关实现
"""
# 导包
import json
import unittest
import requests
import app
from API.loginAPI import Login
from parameterized import parameterized


def build_data():
    with open(app.PRO_PATH + "/data/login_data.json", "r", encoding="utf-8") as f:
        data = []
        for v in json.load(f).values():
            mobile = v.get("mobile")
            password = v.get("password")
            success = v.get("success")
            code = v.get("code")
            message = v.get("message")
            ele = (mobile, password, success, code, message)
            data.append(ele)
    return data


# 创建测试类
class TestLogin(unittest.TestCase):
    # 初始化函数
    def setUp(self) -> None:
        # 初始化session
        self.session = requests.Session()
        # 初始化API
        self.login_obj = Login()

    # 卸载函数
    def tearDown(self) -> None:
        self.session.close()

    # 测试函数——login
    @parameterized.expand(build_data())
    def test_login_all(self, mobile, password, success, code, message):
        # 请求服务器
        response = self.login_obj.get_login(self.session, mobile, password)
        # print("登录响应结果：", response.json())
        # 断言
        self.assertEqual(success, response.json().get("success"))
        self.assertEqual(code, response.json().get("code"))
        self.assertIn(message, response.json().get("message"))

    def test_login_success(self):
        # 发送请求
        response = self.login_obj.get_login(self.session, "13800000002", "123456")
        # 断言
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))
        print("login success", response.json())
        # 提取token
        token = response.json().get("data")
        print("登录后响应的token：", token)
        # 为了允许其它使用token值，将token设置在App.py中的变量
        app.TOKEN = token
