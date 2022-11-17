import cx_Oracle
from Helper.Settings import Settings
cx_Oracle.init_oracle_client(lib_dir=r"C:\app\zhaque\product\11.2.0\instantclient_21_6")


def execute(query,connection):
    try:
        cs = Settings().GetConnectionString(connection)
        con = cx_Oracle.connect(cs["username"]+"/"+cs["password"]+"@"+cs["host_ip"] +":"+cs["port"] +"/"+cs["sid"])
        cur = con.cursor()
        cur.arraysize = 1
        cur.execute(query)
        row = cur.fetchone()
        con.close()
        return row[0]
        
    except Exception as e:
          print(str(e))

    return 0;
    
