# Monitoring_Treand

I will add it later
    {
      "name": "GetPackStatus",
      "query": "select * from ( select trunc(logtime) datetime, sum(totalrequest) total from tblapilogsummery where applicationname='APIHUB2' and method like '%getpackstatus%' group by trunc(logtime) order by 1 desc) where datetime !=trunc(sysdate) and rownum<= 7",
      "connection": "ApiHublog",
      "chart": "line"
    },