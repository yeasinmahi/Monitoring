import psutil

con = psutil.net_connections()
counter =0
for i in con:
    port = i.laddr.port
    if(port>=49152 & port<=65535):
        counter=counter+1

print (counter)