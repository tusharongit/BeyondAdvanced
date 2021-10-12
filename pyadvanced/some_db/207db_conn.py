import sqlite3 # open-source sql built into python

# make a connection to a db

# DB2
# import DB2
# conn = DB2.connect(dsn='ibm-DB', uid='analyst', pwd='db2pwd')
 
# Sybase
# import Sybase
# conn = Sybase.connect('SYBASE', 'username', 'passwd', 'databasename')

# Oracle
# import cx_Oracle
# conn = cx_Oracle.connect('username', 'passwd', 'hostname:port/SID')
# conn2 = cx_Oracle.connect('username/passwd@hostname:portno/SID')
# dsn_tns = cx_Oracle.makedsn('hostname', portno, 'SID')
# conn3 = cx_Oracle.connect('username', 'passwd', dsn_tns)
 
# MySQL
# import MySQLdb
# conn = MySQLdb.connect(host = "hostname", user = "username",# passwd = "password", db = "dbname")
 
# PySQLite
# from pysqlite2 import dbapi2 as sqlite
# conn = sqlite.connect("mydb", connectionproperties)
 
# ODBC
# import odbc
# conn = odbc.odbc("myDSN/username/password")

conn = sqlite3.connect('my_db') # conect to this db or create a db if doesnt exist and then connect to it

# create a cursor to access members of the db
curs = conn.cursor() # curs is a db access object

# some SQL statements to create tables, populate data, etc.

# we will have a zoo table containing animals with name, count, cost, exhibit
stmt_create = '''
CREATE TABLE zoo
( animal VARCHAR(20) PRIMARY KEY,
  count INT,
  cost FLOAT,
  exhibit VARCHAR(20)
)
'''

# execute the statement
curs.execute(stmt_create)

# tidy up
conn.commit()
conn.close()
