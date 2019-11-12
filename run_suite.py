"""
按需求组装套件
自动化测试执行顺序：
                增——>改——>查——>删
"""
# 导包
import logging
import unittest

import app
from case.Test_Login import TestLogin
from case.Test_iHRM import Test_Emp
import time
from tools.HTMLTestRunnerCN import HTMLTestReportCN

# 实例化套件对象
suite = unittest.TestSuite()
suite.addTest(TestLogin("test_login_success"))
suite.addTest(Test_Emp("test_add"))
suite.addTest(Test_Emp("test_update"))
suite.addTest(Test_Emp("test_select"))
suite.addTest(Test_Emp("test_delete"))
# 调用日志文件
with open(app.PRO_PATH+"/report/report.html", "wb") as f:
    runner = HTMLTestReportCN(f, title="人力资源管理系统", description="testing IHRM basic function")
    runner.run(suite)

