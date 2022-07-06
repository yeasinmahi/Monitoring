import datetime
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
import os

class Email:
    species = "Email"


    def send_mail(self,text):
        try: 
            date_ = datetime.datetime.strftime((datetime.datetime.today() - datetime.timedelta(days=1)), '%Y-%m-%d')

            sender = "Report<DSSDigitalSolutions@no.smtp.mail>"
            receiver = ['my.arafat@blmanagedservices.com']
            ccaddr = ['maria.zaman@banglalink.net']

            msg = MIMEMultipart()
            msg['From'] = sender
            msg['To'] = ", ".join(receiver)
            msg['Cc'] = ", ".join(ccaddr)

            receiver.extend(ccaddr)

            msg['Subject'] = f'Health check report {date_}'
            body = f'Dear Concern, \n\n' \
                   f'Please find the BOSGW health check report in below \n\n ' \
                   f'Date: {date_} \n\n' 

            msg.attach(MIMEText(body, 'plain'))

            part = MIMEBase('application', 'octet-stream')
            part.set_payload(open('Data/Images/CFL.png', 'rb').read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',
            'attachment; filename="%s"' % os.path.basename('Data/Images/CFL.png'))
            msg.attach(part)

            s = smtplib.SMTP('172.16.7.183:25', timeout=15)
            text = msg.as_string()
            s.sendmail(sender, receiver, text)
            s.quit()
        except Exception as ex:
            print(str(ex))


