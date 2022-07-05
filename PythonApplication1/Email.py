import datetime
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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
    

            s = smtplib.SMTP('172.16.7.183:25', timeout=15)
            text = msg.as_string()
            s.sendmail(sender, receiver, text)
            s.quit()
        except Exception as ex:
            print(str(ex))


