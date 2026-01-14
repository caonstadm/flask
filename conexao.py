from __future__ import print_function

#SAP DEV 100

#/H/200.187.6.22/S/3299

hostname = 'localhost'
username = 'username'
password = 'password'
database = 'dbname'

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

print( "Using mysqlclient (MySQLdb):" )
import MySQLdb
myConnection = MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )
doQuery( myConnection )
myConnection.close()

print( "Using mysql.connector:" )
import mysql.connector
myConnection = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )
doQuery( myConnection )
myConnection.close()

print( "Using pymysql:" )
import pymysql
myConnection = pymysql.connect( host=hostname, user=username, passwd=password, db=database )
doQuery( myConnection )
myConnection.close()

