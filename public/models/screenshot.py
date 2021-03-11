import os,sys
# 把该函数添加至环境变量
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config import setting

# 截图函数
def insert_img(driver,fileName):
    file_path = setting.SCREENSHOT_DIR+"\\"+fileName
    return driver.get_screenshot_as_file(file_path)