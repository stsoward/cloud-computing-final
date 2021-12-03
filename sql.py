import pyodbc
server = 'hls8finalproject-server.database.windows.net'
database = 'hls8database'
username = 'hls8finalproject-server-admin'
password = 'Te$t1234'   
driver= '{ODBC Driver 13 for SQL Server}'

def query(query):
    rows = []
    with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            row = cursor.fetchone()
            while row:
                rows.append(row)
                row = cursor.fetchone()
    return rows

def insert(query):
    with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            conn.commit()
            return
