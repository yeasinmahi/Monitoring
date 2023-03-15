
import datetime

import pymysql

import requests

import pandas as pd

 

 

date = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d-%b-%Y')

 

data_string = date +" SOC POC "

 

currentMonth = datetime.datetime.now().month

currentYear = datetime.datetime.now().year

df = pd.read_excel('E:\Maria\Project\monitoring\Hoichoi'+'.xlsx',dtype={'Product Code':str,'Service Number':str})

print(df)

 

for index, row in df.iterrows():

     Product = row['Product Code']

     MSISDN = row['Service Number']

     print(Product)

     print(MSISDN)

     data = {

        "phoneNumber": "+"+MSISDN,

        "planCode": Product,

        "externalUserId": "+"+MSISDN,

        "countryCode": "BD"

     }

     Headers = { "x-api-key" : "veJXEGfRFy34UpWip8cE99vVbHDANrNgajdyj8Br","Content-Type":"application/json" }

 

     response = requests.put("https://prod-api-partner.viewlift.com/v1/subscribe?site=hoichoitv&partner=BANGLALINK", headers=Headers,json=data)

     print("Status Code", response.status_code)

     print("JSON Response ", response.json())
