from lib.subFunction import *
def algo(point):
    length = len(point)
    if (length==2):
        midPoint = mid(point[0],point[1])
        return np.concatenate((np.array([point[0]]), np.array([midPoint]), np.array([point[1]])))
    else:
        midarr = np.array([])
        for i in range(length-1):
            midPoint = mid(point[i],point[i+1])
            midarr = np.concatenate((midarr,np.array([midPoint])))
        return np.concatenate(( np.array([point[0]]), algo(midarr) ,np.array([point[length-1]])))
    
def dnc(n:int,point):
    length = len(point)
    if (n==0):
        return np.array([])
    else:
        newPoint = algo(point)
        newLength = len(newPoint)
        return np.concatenate((dnc(n-1,newPoint[0:newLength//2+1]),np.array([newPoint[newLength//2]]),dnc(n-1,newPoint[newLength//2:newLength])))
def dvnconq(n:int, pointx, pointy):
    recordx = {}
    recordy = {}
    arrx = np.concatenate((np.array([pointx[0]]),dnc(n,pointx),np.array([pointx[len(pointx)-1]])))
    arry = np.concatenate((np.array([pointy[0]]),dnc(n,pointy),np.array([pointy[len(pointy)-1]])))
    for i in range(n,0,-1):
        if (i==n):      
            recordx[i] = arrx
            recordy[i] = arry
        else:
            recordx[i] = recordx[i+1][::2]
            recordy[i] = recordy[i+1][::2]
    return recordx,recordy
