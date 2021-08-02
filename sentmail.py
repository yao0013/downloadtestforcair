import smtplib
from email.mime.text import MIMEText

def mailsent(subjects,contents):

    msg_from = '154822916@qq.com'  # 发送方邮箱
    passwd = 'cddqugjdxqcnbjbi'  # 填入发送方邮箱的授权码
    msg_to = 'yaocm@g-cloud.com.cn'  # 收件人邮箱

    subject = subjects  # 主题
    content = contents
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)# 邮件服务器及端口号
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
        print("发送成功")

    except s.SMTPException as e:
        print('发送失败')
    finally:
        s.quit()

    # if __name__ == '__main__':
    #     mailsent("good job")