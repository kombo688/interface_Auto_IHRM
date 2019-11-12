"""
测试增删改查
"""
# 导包
import logging
import unittest
import requests

# 创建测试类
import app
from API.EmpAPI import EmpCRUD


class Test_Emp(unittest.TestCase):

    # 初始化函数
    def setUp(self) -> None:
        self.session = requests.Session()
        self.emp_obj = EmpCRUD()

    # 卸载资源
    def tearDown(self) -> None:
        self.session.close()

    # 函数：增
    # 为什么执行失败？
    # 原因：缺少token
    # 解决：实现关联——token
    def test_add(self):
        logging.info("新增员工信息")
        # request
        response = self.emp_obj.add(self.session, username="不废江河万古流", mobile="18784183349")
        print("员工新增响应结果：", response.json())
        id = response.json().get("data").get("id")
        app.USER_ID = id
        print("new add epm id:", id)
        # 断言
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))

    # 函数：改
    def test_update(self):
        logging.info("更新员工信息")
        # request
        response = self.emp_obj.update(self.session, app.USER_ID, "Jenkins")
        # assert
        print("update user_id:", response.json())
        # 断言
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))

    # 函数：查
    def test_select(self):
        logging.info("查询员工信息")
        response = self.emp_obj.select(self.session, app.USER_ID)
        print("select user id:", response.json())
        # 断言
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))

    # 函数：删
    def test_delete(self):
        logging.info("删除员工信息")
        response = self.emp_obj.delete(self.session, app.USER_ID)
        print("delete user id success!!!",response.json())
        # 断言
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))
