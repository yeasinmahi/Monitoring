import cx_Oracle
from Helper.Settings import Settings
cx_Oracle.init_oracle_client(lib_dir=r"C:\app\zhaque\product\11.2.0\instantclient_21_6")


def execute(query,connection):
    cs = Settings().GetConnectionString(connection)
    con = cx_Oracle.connect(cs["username"]+"/"+cs["password"]+"@"+cs["host_ip"] +":"+cs["port"] +"/"+cs["sid"])
    cur = con.cursor()
    cur.arraysize = 1
    cur.execute(query)
    row = cur.fetchall()
    con.close()
    return row
