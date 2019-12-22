import requests
import re

activeCameraListRename = []
watchtowerurl = 'https://localhost:4343'

cameraList = ['e3v81c3', 'e3v81c2', 'e3v81bf', 'e3v8149', 'e3v81c4', 'e3v81b6', 'e3v81be', 'e3v81c0', 'e3v814f', 'e3v81c6', 'e3v81b9', 'e3v81b7']
nickNames = ['Box1', 'Box2', 'Box3', 'Box4', 'Box5', 'Box6', 'Box7', 'Box8', 'Box9', 'Box10', 'Box11', 'Box12']
nickNamesOrder = []

def getCamByName(jsonobj, name):
    for dict in jsonobj:
        if name in dict['Hostname']:
            return dict

def getCamIdByName(jsonobj, name):
    return getCamByName(jsonobj, name)['Id']

def rename_cams(j, activeCameras):
    print('renaming camera...')
    loop = 0
    for i in activeCameras:
        currentHostname = activeCameras[loop]['Hostname']
        currentHostname = currentHostname.split('.')
        currentHostname = currentHostname[0]
        activeCameraListRename.append(currentHostname)
        loop+=1
    for l in activeCameraListRename:
        currentHostname = l
        camid = getCamIdByName(j, currentHostname)
        if currentHostname == cameraList[0]:
            requests.post(watchtowerurl + '/api/cameras/manage', data={'Id': camid, 'Action': 'RENAME', 'Customname': nickNames[0]}, verify=False)
            currNick = int(re.sub("\D", "", nickNames[0]))
        if currentHostname == cameraList[1]:
            requests.post(watchtowerurl + '/api/cameras/manage', data={'Id': camid, 'Action': 'RENAME', 'Customname': nickNames[1]}, verify=False)
            currNick = int(re.sub("\D", "", nickNames[1]))
        if currentHostname == cameraList[2]:
            requests.post(watchtowerurl + '/api/cameras/manage', data={'Id': camid, 'Action': 'RENAME', 'Customname': nickNames[2]}, verify=False)
            currNick = int(re.sub("\D", "", nickNames[2]))
        if currentHostname == cameraList[3]:
            requests.post(watchtowerurl + '/api/cameras/manage', data={'Id': camid, 'Action': 'RENAME', 'Customname': nickNames[3]}, verify=False)
            currNick = int(re.sub("\D", "", nickNames[3]))
        if currentHostname == cameraList[4]:
            requests.post(watchtowerurl + '/api/cameras/manage', data={'Id': camid, 'Action': 'RENAME', 'Customname': nickNames[4]}, verify=False)
            currNick = int(re.sub("\D", "", nickNames[4]))
        if currentHostname == cameraList[5]:
            requests.post(watchtowerurl + '/api/cameras/manage', data={'Id': camid, 'Action': 'RENAME', 'Customname': nickNames[5]}, verify=False)
            currNick = int(re.sub("\D", "", nickNames[5]))
        if currentHostname == cameraList[6]:
            requests.post(watchtowerurl + '/api/cameras/manage', data={'Id': camid, 'Action': 'RENAME', 'Customname': nickNames[6]}, verify=False)
            currNick = int(re.sub("\D", "", nickNames[6]))
        if currentHostname == cameraList[7]:
            requests.post(watchtowerurl + '/api/cameras/manage', data={'Id': camid, 'Action': 'RENAME', 'Customname': nickNames[7]}, verify=False)
            currNick = int(re.sub("\D", "", nickNames[7]))
        if currentHostname == cameraList[8]:
            requests.post(watchtowerurl + '/api/cameras/manage', data={'Id': camid, 'Action': 'RENAME', 'Customname': nickNames[8]}, verify=False)
            currNick = int(re.sub("\D", "", nickNames[8]))
        if currentHostname == cameraList[9]:
            requests.post(watchtowerurl + '/api/cameras/manage', data={'Id': camid, 'Action': 'RENAME', 'Customname': nickNames[9]}, verify=False)
            currNick = int(re.sub("\D", "", nickNames[9]))
        if currentHostname == cameraList[10]:
            requests.post(watchtowerurl + '/api/cameras/manage', data={'Id': camid, 'Action': 'RENAME', 'Customname': nickNames[10]}, verify=False)
            currNick = int(re.sub("\D", "", nickNames[10]))
        if currentHostname == cameraList[11]:
            requests.post(watchtowerurl + '/api/cameras/manage', data={'Id': camid, 'Action': 'RENAME', 'Customname': nickNames[11]}, verify=False)
            currNick = int(re.sub("\D", "", nickNames[11]))
        nickNamesOrder.append(currNick)
    return(nickNamesOrder)