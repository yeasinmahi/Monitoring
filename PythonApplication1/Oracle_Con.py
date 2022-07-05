import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir=r"C:\app\zhaque\product\11.2.0\instantclient_21_6")


def execute(query):
    con = cx_Oracle.connect('ApiHublog/AP1HuBL0g_61542627@172.16.10.76:2637/PRODBOS')
    #print (con.version)
    successr = '100'
    avail = '100'

    cur = con.cursor()
    cur.arraysize = 1
    cur.execute(query)
    row = cur.fetchall()
    con.close()
    return row
