import json
import requests
import urllib3
import time
loop = 0
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
watchtowerurl = 'https://localhost:4343'
from rename_cameras import rename_cams
from reorder_cam_names import reorder_cam_names

# quick and dirty function for looking up cameras from name
def getCamByName(jsonobj, name):
    for dict in jsonobj:
        if name in dict['Hostname']:
            return dict

def getCamIdByName(jsonobj, name):
    return getCamByName(jsonobj, name)['Id']

def connectCameras():
    activeCameraListIDs = []
    print('connecting camera...')
    loop = 0
    r = requests.get(watchtowerurl + '/api/interfaces/available', verify=False)
    j = json.loads(r.text)
    interface = j[0]['IPAddr']
    resolution = '600p60'
    codec = 'H264'
    anno = 'CameraName'
    segment = "10m"
    requests.get(watchtowerurl + '/api/cameras/scan', verify=False)
    activeCameras = requests.get(watchtowerurl+'/api/cameras', verify=False)
    j = json.loads(activeCameras.text)
    activeCameras = activeCameras.json()
    nickNamesOrder = rename_cams(j, activeCameras)
    time.sleep(5)
    for i in activeCameras:
        activeCameraListIDs.append(activeCameras[loop]['Id'])
        if loop == 0:
            camid = getCamIdByName(j, 'e3v81c3')
            requests.post(watchtowerurl + '/api/cameras/action', data={'Id': camid, 'Action': 'UPDATEMC'}, verify=False)
            time.sleep(10)
        requests.post(watchtowerurl + '/api/cameras/action', data={'Id': activeCameraListIDs[loop], 'Action': 'BIND'}, verify=False)
        requests.post(watchtowerurl + '/api/cameras/action', data={'Id': activeCameraListIDs[loop], 'Action': 'CONNECT', 'Iface': interface, 'Config': resolution, 'Codec': codec, 'Annotation': anno, 'Segtime': segment}, verify=False)
        loop += 1
    activeCameraListIDs = reorder_cam_names(nickNamesOrder, activeCameraListIDs)
    return activeCameraListIDs, len(activeCameraListIDs), interface

def disconnectCameras(connectedCameras, interface):
    for i in connectedCameras:
        currentCam = i
        requests.post(watchtowerurl+'/api/cameras/action', data = {'Id': currentCam, 'Action': 'DISCONNECT', 'Iface': interface}, verify=False)
    print('Cameras disconnected')