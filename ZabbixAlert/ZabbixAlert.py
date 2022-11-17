import os
from Helper.Settings import Settings
from Helper.Oracle_Con import execute

zabbix_server = "172.16.7.221"

def send_data(zabbix_server,host,key,value):
    output = os.popen("zabbix_sender -z "+zabbix_server+" -s "+host+" -k "+key+" -o "+ str(value)).read()
    print(output)

for i in Settings().GetQueries():
    key = i["key"]
    host = i["host"]
    query = i["query"]
    connectionName = i["connection"]

    value = execute(query,connectionName)
    send_data(zabbix_server,host,key,value)
    print(key+"\n"+host+"\n"+ connectionName+"\n"+ query+ "\n"+ str(value)+"\n\n")





