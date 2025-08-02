import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender = 'nek546213@gmail.com'  # your email
receiver = 'deepudeeps2005@gmail.com'  # target email
password = 'ugvr ixao gimn sfjr '   # Gmail App Password

msg = MIMEMultipart('alternative')
msg['Subject'] = "⚠️ Account Verification Required"
msg['From'] = sender
msg['To'] = receiver

with open("email_template.html", 'r') as file:
    html = file.read()

msg.attach(MIMEText(html, 'html'))

try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
        print("[+] Email sent successfully!")
except Exception as e:
    print("[-] Failed to send email:", e)
