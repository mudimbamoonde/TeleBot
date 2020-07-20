import smtplib

sender = 'mudimbamoonde@gmail.com'
receiver = ['mudimba.moonde@zambeef.co.zm']

message = """From: From Person <from@mudimba.moonde@zambeef.co.zm>
To: To Person <to@mudimba.moonde@zambeef.co.com>
Subject: SMTP e-mail test

This is a test e-mail message."""

try:
    smt = smtplib.SMTP('smtp.gmail.com', 465)
    smt.login("mudimbamoonde@gmail.com", "")
    smt.sendmail(sender, receiver, message)
    print("Message Sent")
except smtplib.SMTPException as e:
    print("Error", e)
#     077332274 muchindu
