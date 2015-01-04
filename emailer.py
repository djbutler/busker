#!/usr/bin/env python

import smtplib
from email.mime.text import MIMEText
from numpy.random import randint

# NOTE: you need to create "email_credentials.txt"
# (see email_credentials_SAMPLE.txt for format)
with open('email_credentials.txt','r') as f:
    email,password = [line.strip() for line in f.readlines()]

# initialize an SMTP session
session = smtplib.SMTP('smtp.gmail.com', 587)
session.ehlo()
session.starttls()
session.login(email, password)

# construct the email
sender = "Busker"
subject = "Your top songs"
recipient = email
headers = ["from: " + sender,
           "subject: " + subject,
           "to: " + recipient,
           "mime-version: 1.0",
           "content-type: text/html"]
headers = "\r\n".join(headers)

# write the body
body = "Your top songs\n\n<links that let you donate money>"

# send the email
session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
