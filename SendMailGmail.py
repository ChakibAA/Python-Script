import csv
from email.mime import text
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


from_mail = 'chakib@gmail.com'
email_password = '******'

subject = 'Subject'
content = """<html>
<body>
   HTML CONST
</body>
</html>
"""

with open('email.csv', 'r') as csvFile:
    read = csv.reader(csvFile)
    msg = MIMEMultipart()
    msg['From'] = from_mail
    msg['Subject'] = subject
    msg.attach(MIMEText(content, "html"))
    server = smtplib.SMTP_SSL("smtp.gmail.com", 587)
    server.login(from_mail, email_password)

    for line in read:
        to_send = line[0]
        msg = MIMEMultipart()
        msg['To'] = to_send
        text = msg.as_string()
        server.sendmail(from_mail, to_send, text)

        print(line, 'done')
    server.quit()
