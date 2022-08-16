import datetime
from Helper.Settings import Settings
from Helper.Oracle_Con import execute
from Helper.Email import Email
from Helper.MatPlot import MatPlot
from Helper.Data_Populate import Data_Populate

date_ = datetime.datetime.strftime((datetime.datetime.today() - datetime.timedelta(days=1)), '%Y-%m-%d')


names = []
for i in Settings().GetQueries():
    name = i["name"]
    names.append(name)
    query = i["query"]
    connectionName = i["connection"]
    print(name+"\n"+ connectionName+"\n"+ query+"\n\n")
    result = execute(query,connectionName);
    Data_Populate().Export_Excel(result,name)
    MatPlot().Line(result,name)
#Email().send_mail(names)



