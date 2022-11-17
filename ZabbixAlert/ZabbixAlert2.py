import os
from datetime import datetime, timedelta
from shutil import copy
import requests
import cx_Oracle

#cx_Oracle.init_oracle_client(lib_dir=r"C:\app\zhaque\product\11.2.0\instantclient_21_6")
con = cx_Oracle.connect('ApiHub/AP1HuB_neW_182aPp@172.16.10.76:2637/PRODBOS')
cur = con.cursor()
cur.arraysize = 10
zabbix_server = "172.16.7.221"
sender_Server = "BLAPPDEV02"


def send_data(key,value):
    
    #print(total_value)
    output = os.popen("zabbix_sender -z "+zabbix_server+" -s "+sender_Server+" -k "+key+" -o "+ str(value)).read()
    print(output)
          
def get_data(sql):
    
    try:
        cur.execute(sql)
        records = cur.fetchall()
        if(cur.rowcount >0):
            return records[0][0]
        
    except Exception as e:
          print(str(e))
        
    return 0

sql = """select count(1) from tblappaudittrail where  createdate >= sysdate - (interval '5' minute) and serviceuserid in (33)"""
  
total_value =  get_data(sql)

sql ="""select count(1) from tblappaudittrail where  createdate >= sysdate - (interval '5' minute) and serviceuserid in (33) and statuscode = 200"""

success_value =  get_data(sql)

success_rate = 0
if(total_value !=0):
    success_rate = str(round(success_value*100/total_value, 2))

sql = """select sum(rtt)/300 from tblappaudittrail where  createdate >= sysdate - (interval '5' minute) and serviceuserid in (33)"""
  
avg_rtt =  get_data(sql)
avg_rtt = str(round(avg_rtt, 2))

send_data("apigateway2test_toffee_total_count",total_value)
send_data("apigateway2test_toffee_success_count",success_value)
send_data("apigateway2test_toffee_success_rate",success_rate)
send_data("apigateway2test_toffee_avg_rtt",avg_rtt)
#print(total_value)

#print(success_rate)

con.close()

