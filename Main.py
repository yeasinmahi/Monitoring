from Helper.Oracle_Con import execute
from Helper.Email import Email
from Helper.MatPlot import MatPlot
from Helper.Data_Populate import Data_Populate


data = Data_Populate.GetQuerys()
names = []
for i in data['queries']:
    names.append(i["name"])
    #name = i["name"]
    #query = i["query"]
    #print(name+"\n"+ query+"\n\n")
    #result = execute(query);
    #Data_Populate().Export_Excel(result,name)
    #MatPlot().Line(result,name)
        
Email().send_mail(names)



