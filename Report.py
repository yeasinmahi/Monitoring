import datetime
import os
import smtplib
from email import encoders
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from zipfile import ZipFile

import matplotlib.pyplot as plt
import pandas as pd
import requests
from matplotlib.backends.backend_pdf import PdfPages

now = datetime.datetime.now()
dateinfo = (now - datetime.timedelta(days=1)).strftime('%d%b%y')
reportdt = (now - datetime.timedelta(days=1)).strftime('%d-%b-%Y')

zipname = 'apihub_report_' + dateinfo + '.zip'
pdfname = 'APIHUB_REPORT_' + dateinfo + '.pdf'
infracsv = 'apihub_server_info_' + dateinfo + '.csv'
infraReportName = 'APIHUB_SERVER_INFO_' + dateinfo + '.pdf'

pdf = PdfPages("apihub_report/" + pdfname)
files = set()
files.add(pdfname)
files.add(infracsv)
files.add(infraReportName)


##### KPI Report

def sendKpi(filename):
    success_rate = ''
    try:
        csv = pd.read_csv(os.getcwd() + "/apihub_report/" + filename)
        success_rate = str(sum(list(csv.loc[csv['STATUS'].isin(['OK_200', 'OK_202'])]["PERCENTAGE"])))
        json = {
            "name": "serv_kpi",
            "key": "serv@Kpi",
            "appName": "APIHUB",
            "status": "OK",
            "date": (now - datetime.timedelta(days=1)).strftime('%Y-%m-%d'),
            "availability": "100",
            "successRate": success_rate
        }
        res = requests.post('http://172.16.8.132:9749/servicekpi/apiJson.php', json=json)
        print(res.text)
    except Exception as e:
        print(str(e))
    return success_rate


############################################################
##### Function to generate graph and saving it as pdf ######
def genGraph(filename, xlabel, ylabel, figtitle, xheader, yheader):
    try:
        csv = pd.read_csv(os.getcwd() + "/apihub_report/" + filename)
        plt.style.use('ggplot')
        plt.figure(figsize=(7, 5.5))
        plt.ticklabel_format(style='plain')
        plt.title(figtitle)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        axis_font = {'size': '8'}
        plt.xticks(rotation=45, **axis_font)
        plt.yticks(rotation=45, **axis_font)
        # plt.ticklabel_format(style = 'plain')
        plt.bar(csv[xheader], csv[yheader], width=.5, color='#1E88E5')
        plt.tight_layout()
        pdf.savefig(dpi=500)

        files.add(filename)
    except Exception as ex:
        print(str(ex))


##### Function to generate graph and saving it as pdf v2 ######
def genGraphv2(filename, xlabel, ylabel, figtitle, xheader, yheader1, yheader2):
    try:
        csv = pd.read_csv(os.getcwd() + "/apihub_report/" + filename)
        plt.style.use('ggplot')
        plt.figure(figsize=(7, 5.5))

        ax = plt.subplot()
        ax.bar(csv[xheader], csv[yheader1], width=.5, label="Total")
        ax.bar(csv[xheader], csv[yheader2], width=.5, label="Success")
        ax.legend()

        axis_font = {'size': '8'}
        plt.xticks(rotation=45, **axis_font)
        plt.yticks(rotation=45, **axis_font)

        plt.title(figtitle)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        plt.tight_layout()
        pdf.savefig(dpi=500)

        files.add(filename)
    except Exception as ex:
        print(str(ex))


##### Function to send mail with pdf attachment ######
success_rate = sendKpi('req_stat_' + dateinfo + '.csv')

genGraph('hits_avg_max_tps_' + dateinfo + '.csv', 'Date', 'Request Count', 'Daily Number of  Hits', 'DATE', 'REQ_COUNT')
genGraph('hits_avg_max_tps_' + dateinfo + '.csv', 'Date', 'Average TPS', 'Daily Avg. TPS', 'DATE', 'AVG_TPS')
genGraph('hits_avg_max_tps_' + dateinfo + '.csv', 'Date', 'Max TPS', 'Daily Max TPS', 'DATE', 'MAX_TPS')
genGraph('hrly_avg_max_tps_' + dateinfo + '.csv', 'Hour', 'Request Count', reportdt + ': Hourly Number of Hits', 'HR',
         'REQ_COUNT')
genGraph('hrly_avg_max_tps_' + dateinfo + '.csv', 'Hour', 'Average TPS', reportdt + ': Hourly Average TPS', 'HR',
         'AVG_TPS')
genGraph('hrly_avg_max_tps_' + dateinfo + '.csv', 'Hour', 'Max TPS', reportdt + ': Hourly Max TPS', 'HR', 'MAX_TPS')
genGraph('unique_users_7days_' + dateinfo + '.csv', 'Date', 'Unique Users', ' Daily Unique Users', 'DATE',
         'Unique_Users')
genGraph('unique_users_7days_' + dateinfo + '.csv', 'Date', 'Unique Prepaid Users', ' Daily Unique Prepaid Users',
         'DATE', 'Prepaid_Unique_Users')
genGraph('unique_users_7days_' + dateinfo + '.csv', 'Date', 'Unique Postpaid Users', ' Daily Unique Postpaid Users',
         'DATE', 'Postpaid_Unique_Users')
genGraph('hrly_uniq_users_' + dateinfo + '.csv', 'Hour', 'Unique Users', reportdt + ': Hourly Unique Users', 'HOUR',
         'UNIQUE_USERS')
genGraph('ms_hit_count_' + dateinfo + '.csv', 'Micro Service', 'Hit Count', reportdt + ': MicroService-wise Hits',
         'MicroService', 'Count')
genGraph('ms_rtt_' + dateinfo + '.csv', 'Micro Service', 'Average RTT', reportdt + ': MicroService-wise Average RTT',
         'MicroService', 'Average_RTT(sec)')
genGraph('req_stat_' + dateinfo + '.csv', 'Status', 'Percentage', reportdt + ' Request Status Percentage', 'STATUS',
         'PERCENTAGE')
genGraphv2('purchase_info_' + dateinfo + '.csv', 'Date', 'DBSS Purchase', 'Daily DBSS Purchase', 'DATE',
           'DBSS_PURC_TOT', 'DBSS_PURC_SUC')
genGraphv2('purchase_info_' + dateinfo + '.csv', 'Date', 'CMS Purchase', 'Daily CMS Purchase', 'DATE', 'CMS_PURC_TOT',
           'CMS_PURC_SUC')
genGraphv2('purchase_info_' + dateinfo + '.csv', 'Date', 'DBSS Gift', 'Daily DBSS Gift', 'DATE', 'DBSS_GIFT_TOT',
           'DBSS_GIFT_SUC')
genGraph('lb_ip_count_' + dateinfo + '.csv', 'Load-Balanced-IP', 'Count', reportdt + ': Load Balanced IP',
         'Load-Balanced-IP', 'Count')
genGraph('src_ip_count_' + dateinfo + '.csv', 'Source-IP', 'Count', reportdt + ': Source IP', 'Source-IP', 'Count')

pdf.close()

##### Zip Files

with ZipFile("/app/apihub/apihub_report/" + zipname, 'w') as zip:
    for file in files:
        zip.write("apihub_report/" + file)


##### Function to send mail with pdf attachment ######

def send_mail():
    sender = "Do Not Reply<DSSDigitalSolutions@no.smtp.mail>"
    # receiver = ['imam.ahmed@banglalink.net' , 'ut.saha@blmanagedservices.com']
    # receiver = ['ut.saha@blmanagedservices.com']
    receiver = ['ferdousul.haque@banglalink.net', 'mehe.hasan@banglalink.net', 'imam.ahmed@banglalink.net',
                'ut.saha@blmanagedservices.com', 'Md.imran@brainstation-23.com',
                'maria.zaman@banglalink.net', 'abdullah.masud@banglalink.net',
                'Fakhan@banglalink.net', 'mizanur.rahman@banglalink.net', 'zazam@banglalink.net',
                'safwat.parvez@banglalink.net', 'rashedul.bari@banglalink.net']
    ccaddr = [' ']

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = ", ".join(receiver)
    msg['Cc'] = ", ".join(ccaddr)

    receiver.extend(ccaddr)

    msg['Subject'] = "Apihub Daily Report: " + reportdt
    body = 'Dear Concern, \n \nPlease find the APIHUB Daily  Report details of date: ' + reportdt + ' in attachment.\n Success rate: ' + success_rate + '% \n \n \nBest Regards,\nAPIHUB Monitoring System'
    msg.attach(MIMEText(body, 'plain'))
    filename = pdfname
    attachment = open("apihub_report/" + pdfname, "rb")
    appmime = MIMEBase('application', 'octet-stream')
    appmime.set_payload(attachment.read())

    encoders.encode_base64(appmime)
    appmime.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(appmime)

    attachment = MIMEApplication(open("apihub_report/" + infraReportName, "rb").read(), _subtype="txt")
    attachment.add_header('Content-Disposition', 'attachment', filename=infraReportName)
    msg.attach(attachment)

    attachment = MIMEApplication(open("/app/apihub/apihub_report/" + zipname, "rb").read(), _subtype="zip")
    attachment.add_header('Content-Disposition', 'attachment', filename=zipname)
    msg.attach(attachment)

    s = smtplib.SMTP('172.16.7.183:25', timeout=15)
    text = msg.as_string()
    s.sendmail(sender, receiver, text)
    s.quit()


####### Calling the send_mail() function to send mails ####

send_mail()

########## Deleting all the files ################

for file in files:
    os.remove("apihub_report/" + file)

