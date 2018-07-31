# -*- coding: utf-8 -*-
"""
Created on Wed Jul 02 14:17:19 2014

@author: andrew.dodds
"""

import sys
assert "sqlalchemy" not in sys.modules
#assert "decimal" not in sys.modules
#sys.modules["decimal"] = cdecimal

import time
import datetime
import pyodbc as pyodbc
import ast              # literal_eval
import configparser
import os
import json
import logging
import logging.config
import fnmatch
import shutil
from datadog import initialize as DataDogInitialize
from datadog import api as DataDogAPI
import os



config = configparser.ConfigParser()
config.read('DataDog.cfg')
api_key = str(config.get('Datadog Connection','api_key'))
app_key = str(config.get('Datadog Connection','app_key'))

DataDogInitialize(api_key=api_key,app_key=app_key)  

# Initialise logging
tags = ['version:1', 'application:savvy data loader']



# Configuration
config = configparser.RawConfigParser()
config.read('MeterDataLoader.cfg')
db_connection_string = config.get('Database Connection','odbcconnectionstring')
db_connect_retry_seconds = config.getint('Database Connection','retry_time_seconds')

folders_refresh_seconds = config.getint('Refresh Times','source_locations_refresh_seconds')
files_refresh_seconds = config.getint('Refresh Times','source_files_refresh_seconds')
folders_purge_seconds = 60*config.getint('Refresh Times','archive_purge_delay_minutes')

def get_source_folder_list():
    # Database connection
    print(db_connection_string)   

    conn = pyodbc.connect(db_connection_string)
      
    with conn.cursor() as curs:    
        curs.execute("""
            SELECT id,account_reference
            FROM [EnergyAccounting].[dbo].[invoice_account]
        """)
        folder_tup = curs.fetchall()
    
    # Close database connections        
    conn.close()
    return folder_tup


def list_folder():
	for key in conn.list_objects(Bucket="savvyloader",Prefix="savvy-queue/")['Contents']:
		url,filename = str(key['Key']).split("/")
		print(filename)


def lambda_handler(event, context):
	print(get_source_folder_list())

if __name__ == '__main__':
	print(get_source_folder_list())

