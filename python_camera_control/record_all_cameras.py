import serial
import requests
import os
from tabulate import tabulate
import pandas as pd
import datetime
import time
import urllib3
import keyboard
from connect_cameras import connectCameras
from connect_cameras import disconnectCameras


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
connectedCameras = []
noCameras = 0
connectedCameras, noCameras, interface = connectCameras()

loop = 0
datetimeFormat = '%H:%M:%S.%f'
currDateTime = datetime.datetime.now()
currDateTime = currDateTime.strftime('%H:%M:%S.%f')
if len(connectedCameras) == 1:
    activeCameraList = [1]
else:
    activeCameraList = range(1, noCameras+1)
recordingStatus = ['OFF'] * noCameras
lastOnset = [currDateTime]*noCameras
lastOffset = [currDateTime]*noCameras
totalRecordingTime = [currDateTime] * noCameras
recSessions = [0] * noCameras
currentCamera = 0
watchtowerurl = 'https://localhost:4343'

def turnONcam(currentCamera,connectedCameras):
    recordingStatus = 'ON'
    currentCam = connectedCameras[currentCamera]
    requests.post(watchtowerurl + '/api/cameras/action', data={'IdGroup[]': [currentCam], 'Action': 'RECORDGROUP'}, verify=False)
    return recordingStatus

def turnOFFcam(recSessions, currentCamera, connectedCameras):
    recordingStatus = 'OFF'
    recSessions += 1
    currentCam = connectedCameras[currentCamera]
    requests.post(watchtowerurl + '/api/cameras/action', data={'IdGroup[]': [currentCam], 'Action': 'STOPRECORDGROUP'}, verify=False)
    return recSessions, recordingStatus

########$$$$$$$$$$$$$$$$$$$$$$########################## SEND AND RECIEVE SIGNALS ########$$$$$$$$$$$$$$$$$$$$$$##########################
for i in range(noCameras):
    turnONcam(currentCamera, connectedCameras)
    currentCamera+=1

while True:
    if keyboard.is_pressed('q'):  # if key 'q' is pressed
        print('Disconnecting cameras')
        disconnectCameras(connectedCameras, interface)
        break
    else:
        pass
