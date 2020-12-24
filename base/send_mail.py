from data.data_config import global_var
from email.utils import parseaddr,formataddr
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header


class SendMail:
    def __init__(self):
        '''
                :file_name: 附件文件名称
                :subject: 标题名称
                :content: 邮件内容
                :email_file: 附件路径，如果不在当前目录下，要写绝对路径，默认没有附件
                :email_file1: 附件路径，如果不在当前目录下，要写绝对路径，默认没有附件
                :smtpHost: # 邮箱服务器地址
                :sendAddr: 发件人账号
                :password: 发件人密码，授权码
                :recipientAddrs: 收件人账号
                '''
        file_name = global_var.file_name
        subject = global_var.subject
        email_file = global_var.email_file
        email_file_1 = global_var.email_file_1
        smtpHost = global_var.smtpHost
        sendAddr = global_var.sendAddr
        password = global_var.password
        recipientAddrs = global_var.recipientAddrs

        self.file_name = file_name
        self.subject = subject
        self.email_file = email_file
        self.email_file_1 = email_file_1
        self.smtpHost = smtpHost
        self.sendAddr = sendAddr
        self.password = password
        self.recipientAddrs = recipientAddrs

        # 获取html报告内容
        def get_html(self):
            htmlf = open(self.email_file, encoding="utf-8")
            htmlcont = htmlf.read()
            return htmlcont

        # 邮件格式化方法
        def _format_addr(self, s):
            name, addr = parseaddr(s)
            return formataddr((Header(name, 'utf-8').encode(), addr))

        def send_email(self):
            # 发件人地址
            from_addr = self.sendAddr
            # 密码刚才复制的邮箱的授权码
            password = self.password
            # 收件人地址
            to_addr = self.recipientAddrs  # ,'wm0072008@126.com'
            # 邮箱服务器地址
            smtp_server = self.smtpHost
            # 添加附件
            att = MIMEApplication(open(self.email_file, 'rb').read())
            att.add_header('Content-Disposition', 'attachment', filename=self.file_name)
            # 打开html报告文件，获取HTML内容
            f = open(self.email_file, 'rb')
            mail_body = f.read()
            f.close()

            mail_body = '''
Hello！

    六间房App接口自动化测试结果，测试报告请查看附件
'''
            # 设置邮件信息
            msg = MIMEText(mail_body, _subtype='html', _charset='utf-8')
            msgRoot = MIMEMultipart('related')
            msgRoot['From'] = self._format_addr('接口测试结果<%s>' % from_addr)
            msgRoot['To'] = self._format_addr('测试人员<%s>' % to_addr)
            msgRoot['Subject'] = Header(self.subject, 'utf-8').encode()
            msgRoot.attach(msg)
            msgRoot.attach(att)

            # 发送邮件
            try:
                server = smtplib.SMTP_SSL(smtp_server, 465)
                # 打印出和SMTP服务器交互的所有信息
                server.set_debuglevel(1)
                # 登录SMTP服务器
                server.login(from_addr,password)
                # sendmail():发送邮件，由于可以一次发给多个人，所以传入一个list邮件正文是一个str，as_string()把MIMEText对象变成str。
                server.sendmail(from_addr,to_addr,msgRoot.as_string())
                server.quit()
                print('邮件发送成功！')
            except smtplib.SMTPException:
                print('邮件发送失败')

if __name__ == '__main__':
    s = SendMail()
    a = s.send_email()
    print(a)