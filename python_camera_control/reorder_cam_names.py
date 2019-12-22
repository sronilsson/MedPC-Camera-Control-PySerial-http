

def reorder_cam_names(nickNamesOrder, activeCameraListIDs):
    print(nickNamesOrder,activeCameraListIDs)
    reorderedCamIDlist = []
    camIndexList = []
    loop = 1
    for pp in range(len(nickNamesOrder)):
        camIndexList.append(nickNamesOrder.index(loop))
        loop+=1
    for i in camIndexList:
        currVal = activeCameraListIDs[i]
        reorderedCamIDlist.append(currVal)
    activeCameraListIDs = reorderedCamIDlist
    return activeCameraListIDs