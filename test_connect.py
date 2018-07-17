import pyodbc

server = '10.40.30.37/WIN-KVE063RJ25U'
database = 'prueba'
username = 'Administrator'
password = 'Icidesi10.'
driver='{ODBC Driver 17 for SQL Server}'


conn = pyodbc.connect(
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=10.40.30.37\WIN-KVE063RJ25U,1433;'
    r'DATABASE=prueba;'
    r'UID=na;'
    r'PWD=Icidesi10'
    )

#conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+',PORT=1443;DATABASE='+database+';UID='+username+';PWD='+password)
conn.close()


print("Termino la cconexion")

