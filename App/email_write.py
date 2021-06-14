import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

class emailwrite:
    def emailwrite(title,into,file):
        sendEmail = "a33107521@gmail.com"
        recvEmail = [user]
        password = "brajhqejwbqqnion"

        smtpName = "smtp.gmail.com"
        smtpPort = 587

        for recvEmaila in recvEmail:
            # 여러 MIME을 넣기위한 MIMEMultipart 객체 생성
            msg = MIMEMultipart()

            msg["Subject"] = "[Sirius API]" + title
            msg["From"] = sendEmail
            msg["To"] = recvEmaila

            # 본문 추가
            text = (
                into
                + "ssh://mireu.iptime.org:5100/home/Service-Support/APP/MDFILE/" , file
                )
            contentPart = MIMEText(text)
            msg.attach(contentPart)

            s = smtplib.SMTP(smtpName, smtpPort)
            s.starttls()
            s.login(sendEmail, password)
            s.sendmail(sendEmail, str(recvEmaila), msg.as_string())
            s.close()