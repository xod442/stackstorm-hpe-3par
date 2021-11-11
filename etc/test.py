from os import sys
from sys import path
import os, sys
import time
import hpe3parclient
import requests

# this is a hack to get the hpe driver module
# and it's utils module on the search path.
cmd_folder = os.path.realpath(os.path.abspath("..") )
if cmd_folder not in sys.path:
     sys.path.insert(0, cmd_folder)

# requests.packages.urllib3.disable_warnings()

from hpe3parclient import client, exceptions
# from utils import *



name = "API-TEST-VOLUME-X"
#testSNAPName = ttestVolName+"SNAP"
cpgName = "SSD_r1"
size = 1000

print(cpgName)

cl = client.HPE3ParClient("https://10.132.0.40:8080/api/v1")

cl.login("apiaccess", "siesta123")

#cl.createVolume(testVolName, testCPGName, 2048, "foo")

#volumes = cl.getVolumes()
#wsapi_version = cl.getWsApiVersion()
#tasks = cl.getAllTasks()
allTasks = cl.getAllTasks()

allTasks = allTasks['members']
print(allTasks)
"""
dbuser = "appUser"
dbpass = 'passwordForAppUser'

dbclient = MongoClient('mongodb://%s:%s@localhost:27017/' % (dbuser,dbpass))


mydb = dbclient["app_db"]
known = mydb["3parvols"]

new_volume={}

for vol in volumes:
    myquery = { "u_id" : vol['uuid'] }
    records = known.find(myquery).count()
    print('--------------------------------------------------')
    print(myquery)
    print(records)
    if records == 0:
        vol['u_process']='no'
        write_record = known.insert_one(vol)
        new_volume={}

    else:
        records='Fail to write mongo record, possible duplicate'
        # write_record = process.insert_one(alarm)



for i in info:
    print(i['uuid'])

print(info)


# Get the arrays
allTasks = cl.createVolume(name, cpgName, size)
print('--------------------1---------------------------------')
print(allTasks)
# Get the arrays
allTasks = cl.getVolumes()
print('--------------------2---------------------------------')
print(allTasks)
# Get the arrays
allTasks = cl.deleteVolume(name)
print('---------------------3--------------------------------')
print(allTasks)
# Get the arrays
allTasks = cl.getVolume(name)
print('-----------------------4------------------------------')
print(allTasks)

#print(allTasks['members'])
#print(len(allTasks['members']))

for a in allTasks['members']:
    task = [
            a['id'],
            a['type'],
            a['name'],
            a['status'],
            a['startTime'],
            a['finishTime'],
            a['user']
            ]
    task_data.append(task)
print(task_data)
"""
