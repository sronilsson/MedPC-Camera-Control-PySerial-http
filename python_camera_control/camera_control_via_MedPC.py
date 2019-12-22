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
camerasToTurnOn = []
camerasToTurnOff = []
watchtowerurl = 'https://localhost:4343'

def turnONcam(camerasToTurnOn,connectedCameras):
    currentCameras = [connectedCameras[x] for x in camerasToTurnOn]
    requests.post(watchtowerurl + '/api/cameras/action', data={'IdGroup[]': currentCameras, 'Action': 'RECORDGROUP'}, verify=False)

def turnOFFcam(camerasToTurnOff, connectedCameras):
    currentCameras = [connectedCameras[x] for x in camerasToTurnOff]
    requests.post(watchtowerurl + '/api/cameras/action', data={'IdGroup[]': currentCameras, 'Action': 'STOPRECORDGROUP'}, verify=False)

########$$$$$$$$$$$$$$$$$$$$$$########################## Associate port and board ########$$$$$$$$$$$$$$$$$$$$$$##########################
ArduinoData = serial.Serial()
ArduinoData.port = "COM4"
ArduinoData.baudrate = 9600
ArduinoData.timeout = 1
ArduinoData.setRTS(False)
ArduinoData.open()
ArduinoData.reset_input_buffer()
ArduinoData.reset_output_buffer()

########$$$$$$$$$$$$$$$$$$$$$$########################## SEND AND RECIEVE SIGNALS ########$$$$$$$$$$$$$$$$$$$$$$##########################
while True:
    try:
        if keyboard.is_pressed('q'):  # if key 'q' is pressed
            print('Disconnecting cameras')
            disconnectCameras(connectedCameras, interface)
            break
        else:
            pass
    except:
        pass
    BoxStatus = ArduinoData.readline()
    try:
        BoxStatus = BoxStatus.decode().strip('\r\n')
        BoxStatus = BoxStatus.split(",")
        BoxStatus = BoxStatus[:-1]
        BoxStatus = list(map(int, BoxStatus))
        while ('' in BoxStatus):
            BoxStatus.remove('')
    except (UnicodeDecodeError, ValueError):
        pass
        while ('' in BoxStatus):
            BoxStatus.remove('')
    time.sleep(0.01)
    if len(BoxStatus) == noCameras:
        if loop == 0:
            prevBoxStatus = BoxStatus
        if loop != 0:
            camerasToTurnOff = []
            camerasToTurnOn = []
            OnFlag = 0
            OffFlag = 0
            for i in BoxStatus:
                currDateTime = datetime.datetime.now()
                currDateTime = currDateTime.strftime('%H:%M:%S.%f')
                if (BoxStatus[currentCamera] == 1) and prevBoxStatus[currentCamera] == 1:   #The camera remains OFF
                    pass
                if (BoxStatus[currentCamera] == 0) and prevBoxStatus[currentCamera] == 0:   #The camera remains ON
                    pass
                if (BoxStatus[currentCamera] == 1) and prevBoxStatus[currentCamera] == 0:   #The camera TURNS OFF
                    lastOffset[currentCamera] = currDateTime
                    recSessions[currentCamera]+=1
                    recordingStatus[currentCamera] = 'OFF'
                    camerasToTurnOff.append(currentCamera)
                    OffFlag = 1
                if (BoxStatus[currentCamera] == 0) and prevBoxStatus[currentCamera] == 1:   #The camera TURNS ON
                    lastOnset[currentCamera] = currDateTime
                    recordingStatus[currentCamera] = 'ON'
                    camerasToTurnOn.append(currentCamera)
                    OnFlag = 1
                currentCamera += 1
            if OffFlag == 1:
                turnOFFcam(camerasToTurnOff, connectedCameras)
            if OnFlag == 1:
                turnONcam(camerasToTurnOn, connectedCameras)
            os.system('cls')
            dataDf = pd.DataFrame()
            dataDf['Box'], dataDf['Status'], dataDf['Last cam onset'], dataDf['Last cam offset'], dataDf['Tot. rec sessions'] = [activeCameraList, recordingStatus, lastOnset, lastOffset, recSessions]
            for index, row in dataDf.iterrows():
                v1 = str(row['Last cam onset'])
                v2 = str(row['Last cam offset'])
                v3 = str(row['Tot. rec sessions'])
                if v1 == v2:
                    dataDf.loc[index, 'Last cam onset'] = "No onsets"
                    dataDf.loc[index, 'Last cam offset'] = "No offsets"
                if v3 == '0':
                    dataDf.loc[index, 'Last cam offset'] = "No offsets"
            print(tabulate(dataDf, headers='keys', tablefmt='fancy_grid', showindex=False))
            ArduinoData.reset_input_buffer()
            ArduinoData.reset_output_buffer()
            time.sleep(0.05)
            currentCamera = 0
        prevBoxStatus = BoxStatus
        loop+=1
