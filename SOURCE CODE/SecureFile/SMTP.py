import smtplib
class EmailSending:
    
    def send_email(self, subject, msg, to):
        try:
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            #server.login("myprojectcheck222@gmail.com","Project@123456789")
            server.login("", "")
            message = 'Subject: {}\n\n{}'.format(subject, msg)
            server.sendmail(to, to, message)
            server.quit()
            print("Success: Email sent!")
        except:
            print("Email failed to send.")
