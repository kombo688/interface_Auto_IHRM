"""
    框架搭建：
            核心：api+data+case
            api：封装请求业务
            data：封装测试数据
            case：集成unittest实现，调用api以及参数化解析data
            报告：report+tools+run_suite
            report：保存测试报告
            tools：保存测试报告模板
            run_suite：组装测试套件
            配置：App.py
                    需求：封装路径数据
            日志：log
                保存日志文件
"""
import logging
import logging.handlers
import os

BASE_URL = "http://182.92.81.159"
# 封装项目路径
FILE_PATH = os.path.abspath(__file__)
PRO_PATH = os.path.dirname(FILE_PATH)
TOKEN = None
USER_ID = None


# 日志模块
def my_log_config():
    # 1.获取日志对象
    logger = logging.getLogger()
    # 2.日志级别
    logger.setLevel(logging.INFO)
    # 3.配置输出目标
    to = logging.StreamHandler()
    # 4.配置输出格式
    to_1 = logging.handlers.TimedRotatingFileHandler(PRO_PATH + "/log/my_log",
                                                     when="h",
                                                     interval=12,
                                                     backupCount=14,
                                                     encoding="utf-8")
    # 5.组织配置并添加进日志对象
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")
# 在需要的位置调用日志输出
    to.setFormatter(formatter)
    to_1.setFormatter(formatter)
    logger.addHandler(to)
    logger.addHandler(to_1)
    # 为测试类的测试函数添加日志函数
    # 1.使用__init__初始化日志
    # 2.在测试函数中调用logging.xxx(信息)
# my_log_config()
# logging.info("debug")
