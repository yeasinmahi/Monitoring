import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from Helper.Data_Populate import Data_Populate


class Email:
    species = "Email"

   
    def send_mail(self,names):
        try: 
            date_ = datetime.datetime.strftime((datetime.datetime.today() - datetime.timedelta(days=1)), '%Y-%m-%d')

            sender = "Report<DSSDigitalSolutions@no.smtp.mail>"
            receiver = ['my.arafat@blmanagedservices.com']
            #ccaddr = ['maria.zaman@banglalink.net', 'zhaque@banglalink.net']
            ccaddr = ['maria.zaman@banglalink.net']

            msg = MIMEMultipart()
            msg['From'] = sender
            msg['To'] = ", ".join(receiver)
            msg['Cc'] = ", ".join(ccaddr)

            receiver.extend(ccaddr)

            msg['Subject'] = f'Health check report {date_}'
            html = Data_Populate().get_html_templete(names)
            msg.attach(MIMEText(html, 'html'))
            
            for name in names:
                self.attach_file_to_email(msg, 'Data/Images/', name, '.png', {'Content-ID': '<'+name+'>'})

            # for attachement 
            #for name in names:
            #    self.attach_file_to_email(msg, 'Data/Excels/', name, '.xlsx')
            r_name= 'Report_'+date_+'.pdf'
            Data_Populate().images_to_Pdf(names,'Report_'+date_+'.pdf')
            self.attach_file_to_email(msg, 'Data/Pdf/','Report_'+date_,'.pdf')
            
            s = smtplib.SMTP('172.16.7.183:25', timeout=15)
            m = msg.as_string()
            s.sendmail(sender, receiver, m)
            s.quit()
            print("\nEmail sent successfully")
        except Exception as ex:
            print(str(ex))

    def attach_file_to_email(self,email_message,filepath, filename, fileextension, extra_headers=None):
        with open(filepath+filename+fileextension, "rb") as f:
            file_attachment = MIMEApplication(f.read())
        # Add header/name to the attachments    
        file_attachment.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename+fileextension}",
        )
        if extra_headers is not None:
            for name, value in extra_headers.items():
                file_attachment.add_header(name, value)
        # Attach the file to the message
        email_message.attach(file_attachment)

    
