from Oracle_Con import execute
from Email import Email
from MatPlot import MatPlot
from Data_Populate import Data_Populate


data = Data_Populate.GetQuerys()

for i in data['queries']:
    name = i["name"]
    query = i["query"]
    print(name+"\n"+ query+"\n\n")
    result = execute(query);
    Data_Populate().Export_Excel(result,name)
    MatPlot().Line(result,name)
        
Email().send_mail("test")



