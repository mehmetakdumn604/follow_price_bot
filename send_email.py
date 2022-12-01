from email.mime.text import MIMEText
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
def sendEmail(toMail,subject, content):
    fromMail = "alaqbunudacal@gmail.com"
    server = smtplib.SMTP("smtp.gmail.com",587)

    server.starttls()
    server.login(fromMail, "rrvwwevwxskppmah")

    message = MIMEMultipart("alternative")

    message["subject"] = subject

    htmlContent = MIMEText(content,"html")

    message.attach(htmlContent)

    server.sendmail(
        fromMail,toMail,message.as_string()
    )
    server.quit() 
