import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

class SendMail(object):
    def __init__(self,user,password,receiver,subject,text,file=None,img=None,email_host='smtp.163.com',port=25):
        self.user=user
        self.password=password
        self.receiver=receiver
        self.subject=subject
        self.text=text
        self.file=file
        self.img=img
        self.emilhost=email_host
        self.port=port
    def send(self):
        msg=MIMEMultipart()
        msg['From']=self.user
        msg['To']=self.receiver
        msg['Subject']=self.subject
        msg.attach(MIMEText(self.text, 'plain', 'utf-8'))
        if self.file:
            mi=MIMEText(open(self.file,'rb').read(),'base64','utf-8')
            mi["Content-Disposition"] = 'attachment; filename="1.txt"'
            msg.attach(mi)
        if self.img:
            image=MIMEImage(open(self.img,'rb').read())
            image["Content-Disposition"] = 'attachment; filename="1.jpg"'
            msg.attach(image)
        self.smtp=smtplib.SMTP(self.emilhost,self.port)
        self.smtp.login(self.user,self.password)
        try:
            self.smtp.sendmail(self.user,self.receiver,msg.as_string())
        except Exception as e:
            print(e)
            print("false")



if __name__ == '__main__':
        receiver = '*****@qq.com'
        username = '****@163.com'
        password = '******'
        subject='整体测试'
        text='python程序测试，请勿回复'
        file='shdkd.txt'
        image='2.jpg'
        mail=SendMail(user=username,password=password,receiver=receiver,subject=subject,text=text,file=file,img=image)
        mail.send()