import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

name = input("Enter Receiver's Name: ")
emailID = input("Enter mail ID: ")
html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Bot'
email['to'] = emailID
email['subject'] = 'Here are some recommendations for you...'

email.set_content(html.substitute({'name': name}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(' ', ' ')        #Your (Sender's) Email ID and Password.
    smtp.send_message(email)
    print('Done!')
