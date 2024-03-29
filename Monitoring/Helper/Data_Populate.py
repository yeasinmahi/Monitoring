import json
import pandas as pd
import pdfkit
#config = pdfkit.configuration(wkhtmltopdf = r"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")  
from fpdf import FPDF
import os
from Helper.Utility import Utility

class Data_Populate(object):
    species = "Data Load"

    def GetConfig():
        try:
            f= open("config.json")
            data = json.load(f)
            f.close()
            return data
        except Exception as e:
            return print(e)

    def Export_Excel(self,data,name,columns=['Date','count']):
        
        df = pd.DataFrame(list(data))
       
        df.columns =columns
        print(df)
        Utility().CreateFilePath('Data/Excels')
        writer = pd.ExcelWriter('Data/Excels/'+name+'.xlsx')
        df.to_excel(writer, sheet_name=name, index=False,  na_rep='NaN')
        writer.save()

    def Excel_To_Html(self,name):
        pd.set_option('display.max_colwidth', 40)
        df = pd.read_excel('Data/Excels/'+name+'.xlsx')
        return df.to_html(index=False)

    def images_to_Pdf(self, names,report_name):
        Utility().CreateFilePath('Data/Images')
        Utility().CreateFilePath('Data/Pdf')
        pdf = FPDF()
        for name in names:
            pdf.add_page()
            pdf.image('Data/Images/'+ name+ '.png', 0,0,210)
        pdf.output('Data/Pdf/'+report_name, "F")

    def get_html_templete(self, names):
        trs = ""
        for name in names:
            trs+="<tr><td style='padding:0;'><img src='cid:"+name+"' alt='"+name+"' /></td><td>"+Data_Populate().Excel_To_Html(name)+"</td></tr>"
        html = '''
 <html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <meta name="x-apple-disable-message-reformatting">
    <title>Monitoring </title>
    <style>
        table, td, div, h1, p {font-family: Arial, sans-serif;}
        
    </style>
</head>
<body>
	<table role="presentation" style="width:auto;border-collapse:collapse;border:1px solid #cccccc;border-spacing:0;text-align:left;">
		''' + f'{trs}'+ '''
	</table>
</body>
</html>
'''
        return html;