import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config import setting
import configparser
from public.models.getreport import get_report
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from public.models.log import Log
log = Log()
# 发送邮件
def send_Email():
    # 读取配置文件邮件信息
    con = configparser.ConfigParser()
    con.read(setting.SYSCONFIG_DIR,encoding='UTF-8')
    HOST = con.get('email','HOST')
    PORT = con.get('email', 'PORT')
    SENDER = con.get('email','SENDER')
    RECEIVER = con.get('email','RECEIVER')
    USERNAME = con.get('email','USERNAME')
    PASSWORD = con.get('email','PASSWORD')
    EMAILBODY = con.get('email','EMAILBODY')
    SUBJECT = con.get('email','SUBJECT')

    # 获取最新测试报告作为附件
    report = get_report()
    sendReport = open(report,'rb').read()

    # 邮件内容设置
    att = MIMEText(sendReport,'base64','UTF-8')
    att["Content-Type"] = 'application/octet-stream'
    att.add_header("Content-Disposition", "attachment", filename=("gbk", "", setting.REPORT_DIR))

    msg = MIMEMultipart('related')
    msg.attach(att)
    msgtext = MIMEText(EMAILBODY, 'html', 'utf-8')
    msg.attach(msgtext)

    msg['From']=SENDER
    msg['To']=RECEIVER
    msg['Subject']=SUBJECT

    # 发送邮件
    try:
        server = smtplib.SMTP_SSL(HOST,PORT)
        server.login(user=USERNAME,password=PASSWORD)
        server.sendmail(SENDER,RECEIVER,msg.as_string())
        server.quit()
        log.info('邮件发送成功：发送人-->%s,收件人-->%s'%(SENDER,RECEIVER))
    except Exception as ex:
        log.error('邮件发送失败-->%s' % ex)


send_Email()