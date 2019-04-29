#coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime

class SendEmail:

    #全局变量，为了在一个类或一个函数中使用由函数返回的变量
    global send_user
    global email_host
    global password

    password = "Jeremy@1314@."
    email_host = "smtp.qq.com"
    send_user = "494181687@qq.com"

    def send_mail(self,user_list,sub,content):
        user = "Jeremy" + "<" + send_user + ">"
        print("发件人:%s" %user)

        # 创建一个带附件的实例
        message = MIMEMultipart()
        #邮件标题
        message['Subject'] = sub
        #发件人
        message['From'] = user
        #收件人
        message['To'] = ";".join(user_list)

        # 邮件正文内容
        message.attach(MIMEText(content, 'plain', 'utf-8'))

        # 构造附件1（附件为HTML格式的网页）
        filename = '../report/report.html'
        time = datetime.date.today()
        with open(filename,'rb') as f:
            #附件att传入filename文件
            att = MIMEText(f.read(), 'html', 'utf-8')
            att["Content-Type"] = 'application/octet-stream'
            #filename=邮件中附件显示的名字（任意写）
            att["Content-Disposition"] = 'attachment; filename="%s_Result.html"'% time
            #添加附件att
            message.attach(att)

        # 构造附件2
        # 略，有几个附件构造几个att

        # try:
        #     smtpObj = smtplib.SMTP('localhost')
        #     smtpObj.sendmail(send_user,user_list,message.as_string())
        #     print("[info]:邮件发送成功！！！")
        # except smtplib.SMTPException:
        #     print("[info]:无法发送邮件~~")
        #
        #     smtpObj.quit()

        #调用smtp方法发送SSL邮件
        try:
            server = smtplib.SMTP_SSL()
            server.connect(email_host,465)# 启用SSL发信, 端口一般是465
            #server.set_debuglevel(1)# 打印出和SMTP服务器交互的所有信息
            server.login(send_user,password)
            server.sendmail(send_user,user_list,message.as_string())
            print("[info]:邮件发送成功！！！")
        except smtplib.SMTPException:
            print("[info]:无法发送邮件~~")
            server.quit()

    def send_main(self):
        #收件人列表
        user_list = ['litq@fun.tv']
        print("收件人:%s" %user_list)
        sub = "接口自动化测试报告"
        content = "接口自动化测试结果:见附件"
        self.send_mail(user_list,sub,content)
