# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# Time:2019/5/30 10:57

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def get_eamil(case):
    smtpserver = "smtp.163.com"
    port = 0 # 端口
    sender = "xiao_whb@163.com"
    psw = "xiaoxi123" # 密码
    # receiver = ["zhonglinhua@brc.com.cn","liaolei1@brc.com.cn","gaojia1@brc.com.cn"]
    #receiver = ["xiao_whb@163.com","zhonglinhua@brc.com.cn","liaolei1@brc.com.cn","gaojia1@brc.com.cn","13880497676@163.com"]
    receiver= ["13880497676@163.com"]

    if case==1:
        # ----------2.编辑邮件的内容-------
        file_path = "../report/report_justbon.html"
        with open(file_path, "rb") as fp:
          mail_body = fp.read()
        msg = MIMEMultipart()
        msg["from"] = sender # 发件人
        msg["to"] = ";".join(receiver) # 收件人
        # msg['to'] = receiver
        msg["subject"] = "嘉宝生活家app_UI自动化测试报告"
        body = MIMEText(mail_body, "html", "utf-8")
        msg.attach(body)
        # 附件
        att = MIMEText(mail_body, "base64", "utf-8")
        att["Content-Type"] = "application/octet-stream"
        att["Content-Disposition"] = 'attachment; filename="report_justbon.html"'
        msg.attach(att)
        # ----------3.发送邮件------
        try:
             smtp = smtplib.SMTP()
             smtp.connect(smtpserver) # 连服务器
             smtp.login(sender, psw)
        except:
             smtp = smtplib.SMTP_SSL(smtpserver, port)
             smtp.login(sender, psw) # 登录
        smtp.sendmail(sender, receiver, msg.as_string()) # 发送
        smtp.quit()
        print("发送邮件")

    elif case==2:
        # ----------2.编辑邮件的内容-------
        file_path = "../report/report_finance.html"
        with open(file_path, "rb") as fp:
          mail_body = fp.read()
        msg = MIMEMultipart()
        msg["from"] = sender # 发件人
        msg["to"] = ";".join(receiver) # 收件人
        # msg['to'] = receiver
        msg["subject"] = "收费系统测试报告"
        body = MIMEText(mail_body, "html", "utf-8")
        msg.attach(body)
        # 附件
        att = MIMEText(mail_body, "base64", "utf-8")
        att["Content-Type"] = "application/octet-stream"
        att["Content-Disposition"] = 'attachment; filename="report_finance.html"'
        msg.attach(att)
        # ----------3.发送邮件------
        try:
             smtp = smtplib.SMTP()
             smtp.connect(smtpserver) # 连服务器
             smtp.login(sender, psw)
        except:
             smtp = smtplib.SMTP_SSL(smtpserver, port)
             smtp.login(sender, psw) # 登录
        smtp.sendmail(sender, receiver, msg.as_string()) # 发送
        smtp.quit()
        print("发送邮件")

# get_eamil(2)