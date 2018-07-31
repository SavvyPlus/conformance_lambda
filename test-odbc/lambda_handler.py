# -*- coding: utf-8 -*-
import pyodbc as pyodbc
import os
import subprocess

#db_connection_string = "Driver={ODBC Driver 13 for SQL Server};Server=test-2-savvy-work.ciimkozo2x5b.ap-southeast-2.rds.amazonaws.com;Port=1433;Database=EnergyAccounting;UID=djangounchained;PWD=N))$I!BJDA6y;"
db_connection_string = "Driver={libmsodbcsql-13.0.so.1.0};Server=test-2-savvy-work.ciimkozo2x5b.ap-southeast-2.rds.amazonaws.com;Port=1433;Database=EnergyAccounting;UID=djangounchained;PWD=N))$I!BJDA6y;"


def connect():
    conn = pyodbc.connect(db_connection_string)

    with conn.cursor() as curs:
        curs.execute("""
            SELECT id,account_reference
            FROM [EnergyAccounting].[dbo].[invoice_account]
        """)

        accounts = curs.fetchall()
        for account in accounts:
            print(account)


def lambda_handler(event, context):
    libdir = os.environ['LD_LIBRARY_PATH'] + ":" + os.path.join(os.getcwd(), 'lib')
    command = 'LD_LIBRARY_PATH={} python lambda_handler.py'.format(libdir)
    subprocess.call(command, shell=True)

if __name__ == '__main__':
    connect()
