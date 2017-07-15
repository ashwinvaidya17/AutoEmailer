#--------------Created by Ashwin Vaidya 2017---------------
#email lists are stored in mteachers_emails.txt, fteachers_emails.txt, student_emails.txt with different body for each
#use sys.argv for username and password
#----requires allow lesssecure apps to be turned on--------
import smtplib, os,sys
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders



#----------Email function--------------
def send_mail( send_from, send_to, subject, text, files, server, port, username, password):
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = send_to
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

#-------------------------------------------------------------
#store student emails
with open("student_emails.txt") as file:
    student_emails_array = [i.strip() for i in file]
print("Student list: ")
print(student_emails_array)  #debugger
with open("mteachers_emails.txt") as file:
    mteachers_emails_array = [i.strip() for i in file]
print("Male teachers list: ")
print(mteachers_emails_array)  #debugger
with open("fteachers_emails.txt") as file:
    fteachers_emails_array = [i.strip() for i in file]
print("Female teachers list: ")
print(fteachers_emails_array)  #debugger

attachmentfile = ["Newsletter June17.pdf"] #Newsletter attachment should be in the same folder
username='mcugnewsletter'
if len(sys.argv)!=2:
	print("No password entered")
	exit(0);
password=sys.argv[1]
bodyStudent =  "Hello, \nWe are pleased to bring you the June’17 edition of MCUG Newsletter.\nHope you like it! Your valuable suggestions will help us in improving future editions .\nPFA\n\nRegards,\nMCUG Newsletter Team."
bodyMTeachers = "Dear Sir,\nWe are pleased to bring you the June’17 edition of MCUG Newsletter.\nHope you like it! Your valuable suggestions will help us in improving future editions .\nPFA\n\nRegards,\nMCUG Newsletter Team."
bodyFTeachers = "Dear Ma'am,\nWe are pleased to bring you the June’17 edition of MCUG Newsletter.\nHope you like it! Your valuable suggestions will help us in improving future editions .\nPFA\n\nRegards,\nMCUG Newsletter Team."
print("sending...")

for Otheremail in student_emails_array:
	send_mail('mcugnewsletter@gmail.com',Otheremail,"MCUG NEWSLETTER", bodyStudent, attachmentfile, 'smtp.gmail.com', 587, username,password)
	print("Sent to "+Otheremail)
print("Sent to students")
for Otheremail in fteachers_emails_array:
	send_mail('mcugnewsletter@gmail.com',Otheremail,"MCUG NEWSLETTER", bodyFTeachers, attachmentfile, 'smtp.gmail.com', 587, username,password)
	print("Sent to "+Otheremail)
print("Sent to female teachers")
for Otheremail in mteachers_emails_array:
	send_mail('mcugnewsletter@gmail.com',Otheremail,"MCUG NEWSLETTER", bodyMTeachers, attachmentfile, 'smtp.gmail.com', 587, username,password)
	print("Sent to "+Otheremail)
print("Sent to male teachers")