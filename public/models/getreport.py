import os,configparser
from config import setting
# 根据时间排序，获取最新的测试报告

def get_report():
    report_dir = setting.REPORT_DIR
    # 获取测试报告文件夹下的所有文件
    reportList =os.listdir(report_dir)
    # 文件夹下的文件按照时间进行排序
    reportList.sort(key=lambda filename:os.path.getmtime(report_dir+"\\"+filename))
    # 取最新文件
    new_file =os.path.join(report_dir,reportList[-1])
    return new_file

