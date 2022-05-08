import smtplib
from email.mime.text import MIMEText


def send_email(msg, msgtype):
    mail_host = 'smtp.qq.com'
    mail_user = '804642554@qq.com'
    mail_pass = 'xlgurytijxvybcfa'
    sender = '804642554@qq.com'
    receivers = ['Haob.19@intl.zju.edu.cn']

    if msgtype == 'private':
        message = MIMEText('This is the auto reply for your WeChat PRIVATE chat:\n' +
                           msg['ActualNickName'] + ' said: \n' + msg['Content'], 'plain', 'utf-8')
    else:
        message = MIMEText('This is the auto reply for your WeChat GROUP chat:\n' +
                           msg['ActualNickName'] + ' said by @: \n' + msg['Content'], 'plain', 'utf-8')

    message['Subject'] = "Maid Robot Auto Forward"
    message['From'] = sender
    message['To'] = receivers[0]

    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.quit()

    return

