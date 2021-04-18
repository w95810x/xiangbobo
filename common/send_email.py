from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import sys,io,os
from pages.basepage import BasePage
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')


class Email(BasePage):

    def new_report(self):
        testreport = r'E:\xiang88\resuit'
        lists = os.listdir(testreport)
        # 重新按时间对目录下的文件进行排序
        lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
        file_new = os.path.join(testreport, lists[-1])
        print(file_new)
        return file_new

    def sendemail(self):
        smtpserver = 'smtp.163.com'  # 发件服务器
        port = 465  # 端口    服务器和端口号不知道的话，可以去qq邮箱搜索
        username = 'yswangbx@163.com'  # 发件箱用户名
        password = 'xxxxxxxxxxx'  # 授权码，注意这里不是密码，是qq邮箱支持第三方工具的授权码，需要去qq邮箱修改哈
        sender = 'xxxxxxx@163.com'  # 发件人邮箱
        receiver = 'xxxxxxxxxx@qq.com'  # 收件人邮箱
        # receiver = ['*****@qq.com','*****@163.com']  #多个收件人写成列表就可以了
        msg = MIMEMultipart('related')  # 定义邮件类型，related可以增加多种附件
        msg.attach(MIMEText('本轮自动化测试报告结果如下'))  # 邮件里边的文本
        msg['Subject'] = '报告'  # 主题
        msg['From'] = sender  # 让发件人不为空

        # 下边这几句是添加附件
        mail_path = open(self.new_report(), 'r',encoding='utf-8', errors='ignore').read()  # 这几句里边可以修改路径和文件名称，具体以实际为准
        att = MIMEText(mail_path, "base64", "utf-8")
        att["Content-Type"] = "application/octet-stream"
        att["Content-Disposition"] = "attachment;filename = 'result.html'"
        msg.attach(att)

        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)  # 连接邮件服务器
        smtp.login(username, password)  # 登录
        smtp.sendmail(sender, receiver, msg.as_string())  # 发送，接收，内容
        smtp.quit()  # 关闭
        print("邮件发送成功")  # 提示邮件发送结果

