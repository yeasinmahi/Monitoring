from Oracle_Con import execute
from Email import Email

query = """select trunc(logtime), sum(totalrequest),method from tblapilogsummery
where applicationname='CFLWebService'
and method like '%SMSForwading.svc%'
group by trunc(logtime), method
order by 1 desc"""

result = execute(query);
email = Email();
email.send_mail("test")
