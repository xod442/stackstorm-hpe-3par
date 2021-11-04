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

requests.packages.urllib3.disable_warnings()

from hpe3parclient import client, exceptions
# from utils import *

username = "apiaccess"
password = "siesta3"

name = "API-TEST-VOLUME-X"
#testSNAPName = testVolName+"SNAP"
cpgName = "SSD_r1"
size = 1000

print(cpgName)

cl = client.HPE3ParClient("https://10.132.0.40:8080/api/v1")

cl.login("apiaccess", "siesta3")

#cl.createVolume(testVolName, testCPGName, 2048, "foo")

info = cl.getVolumes()
#wsapi_version = cl.getWsApiVersion()
#tasks = cl.getAllTasks()

info = info['members']

for i in info:
    print(i['uuid'])

print(info)

"""
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
