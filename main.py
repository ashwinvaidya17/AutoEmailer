#--------------Created by Ashwin Vaidya 2017---------------
"""email lists are stored in mteachers_emails.txt, fteachers_emails.txt, student_emails.txt with different body for each"""
#use sys.argv for username and password
import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders

file = open("student_emails.txt")
sendToemail = file.read() #reading only one email for now
attachmentfile = ["student_emails.txt"] #sending the same file as test

def send_mail( send_from, send_to, subject, text, files, server, port, username, password):
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime = True)
    msg['Subject'] = subject

    msg.attach( MIMEText(text) )

    for f in files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload( open(f,"rb").read() )
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="{0}"'.format(os.path.basename(f)))
        msg.attach(part)

    smtp = smtplib.SMTP(server, port)
    smtp.starttls()
    smtp.login(username,password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()
send_mail('ashwinoriginal@gmail.com',sendToemail,"NEWSLETTER", "Sample body", attachmentfile, 'smtp.gmail.com', 587, "ashwinoriginal","password")