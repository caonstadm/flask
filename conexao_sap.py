from __future__ import print_function

#SAP DEV 100

#/H/200.187.6.22/S/3299
# hostname: hcmdev
# database: ECD
# ambiente DEV.(ECD)

# Conexao Padrao
# hostname = 'localhost'
# username = 'username'
# password = 'password'
# database = 'dbname'

# Conexao SAP DEV 
hostname = '200.187.6.22'
port = '3299'
username = 'cabreu'
password = 'Taxi2022'
database = 'hcmdev'

import oracledb
import os

un = os.environ.get('PYTHON_USERNAME')
pw = os.environ.get('PYTHON_PASSWORD')
cs = os.environ.get('PYTHON_CONNECTSTRING')

with oracledb.connect(user=username, password=password, port=port, host=hostname) as connection:
    with connection.cursor() as cursor:
        sql = """select sysdate from dual"""
        for r in cursor.execute(sql):
            print(r)

# Simple routine to run a query on a database and print the results:
def doQuery( conn ) :
    cur = conn.cursor()

    cur.execute( "SELECT fname, lname FROM employee" )

    for firstname, lastname in cur.fetchall() :
        print( firstname, lastname )


print( "Using Oracle:" )
import oracledb
myConnection = oracledb.connect( host=hostname, user=username, passwd=password, db=database )
doQuery( myConnection )
myConnection.close()
