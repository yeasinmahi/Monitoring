import datetime
from Helper.Settings import Settings
from Helper.Oracle_Con import execute
from Helper.Email import Email
from Helper.MatPlot import MatPlot
from Helper.Data_Populate import Data_Populate

date_ = datetime.datetime.strftime((datetime.datetime.today() - datetime.timedelta(days=1)), '%Y-%m-%d')


names = []
for i in Settings().GetQueries():
    #print(i)
    name = i["name"]
    names.append(name)
    query = i["query"]
    connectionName = i["connection"]
    chart = i["chart"]
   
    result = execute(query,connectionName)
    if "columns" in i:
   
        #print(i['columns']+"\n"+ connectionName+"\n"+ query+"\n\n")
        li = list(i['columns'].split(","))
        Data_Populate().Export_Excel(result,name,li)
    else:
        Data_Populate().Export_Excel(result,name)
    MatPlot().Chart(result,name,chart,i['titel'])
Email().send_mail(names)



