# 全局变量配置类

import sys, os

# 获取系统跟路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# 把跟路径下所有文件添加到环境变量中
sys.path.append(BASE_DIR)

# 数据库配置
DATEBASE_DIR = os.path.join(BASE_DIR, 'config', 'datebaseConfig.ini')
# 系统其它配置
SYSCONFIG_DIR = os.path.join(BASE_DIR, 'config', 'sysConfig.ini')
# 日志
LOG_DIR = os.path.join(BASE_DIR, 'logs')
# 测试报告
REPORT_DIR = os.path.join(BASE_DIR, 'report')
# 测试报告中的截图
SCREENSHOT_DIR = os.path.join(REPORT_DIR, 'screenshot')
# 测试数据
TESTDATE_DIR = os.path.join(BASE_DIR, 'testdate')
# 页面元素数据
ELEMENT_DIR = os.path.join(BASE_DIR, 'elementdate')
# requests相关
REQUESTS_DIR = os.path.join(BASE_DIR,'requestsCase')