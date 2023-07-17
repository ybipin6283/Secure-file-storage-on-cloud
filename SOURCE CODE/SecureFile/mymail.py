import smtplib

gmail_user = ''
gmail_password = ''

sent_from = gmail_user
to = ['dhaatisolutions6@gmail.com']
subject = 'OMG Super Important Message'
body = 'Hey, what'

email_text = "hiii"

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!')
except Exception as e:
    print(e)