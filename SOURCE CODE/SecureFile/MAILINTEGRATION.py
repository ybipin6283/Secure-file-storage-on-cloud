import smtplib
class EmailSending:
    
    def send_email(self, subject, msg, to):
        try:
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login("","")
            message = 'Subject: {}\n\n{}'.format(subject, msg)
            server.sendmail(to, to, message)
            server.quit()
            print("Success: Email sent!")
        except Exception as e:
            print(e)
            print("Email failed to send.")
