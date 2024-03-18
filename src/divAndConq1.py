from lib.subFunction import *
def algo(point,result,cpoint,iter):
    length = len(point)
    if (length==2):
        midPoint = mid(point[0],point[1])
        result = np.concatenate((np.array([point[0]]), np.array([midPoint]), np.array([point[1]])))
        cpoint[iter] = [result.tolist()]

    else:
        midarr = np.array([])
        temp = np.array([])
        for i in range(length-1):
            midPoint = mid(point[i],point[i+1])
            midarr = np.concatenate((midarr,np.array([midPoint])))
            temp = np.append(temp,point[i])
            temp = np.append(temp,midPoint)
        temp = np.append(temp,point[length-1])
        temp = temp.reshape(1,-1)
        print(f"temp: {temp}")
        print(f"point: {point}")
        
        resultN = np.array([])
        algo(midarr,resultN,cpoint,iter)
        print(f"resultN: {resultN}")
        print(f"cpoint: {cpoint[iter]}")
        cpoint[iter].append(resultN.tolist())
        
        result = np.concatenate(( np.array([point[0]]), resultN,np.array([point[length-1]])))
    
def dnc(n:int,point,result,cpoint,max):
    length = len(point)
    if (n==0):
        result =  np.array([])
    else:
        newPoint = np.array([])
        algo(point,newPoint,cpoint,max-n+1)
        newLength = len(newPoint)
        print("iter done")
        resultL = np.array([])
        print(f"new point: {newPoint}")
        print(f"cpoint: {cpoint}")
        dnc(n-1,newPoint[0:newLength//2+1],resultL,cpoint,max)
        resultR = np.array([])
        dnc(n-1,newPoint[newLength//2:newLength],resultR, cpoint,max)
        result = np.concatenate(resultL,np.array([newPoint[newLength//2]]),resultR)

def dvnconq(n:int, pointx, pointy):
    recordx = {}
    recordy = {}
    cpointx = {}
    cpointy = {}
    arrx = np.array([])
    arry = np.array([])
    dnc(n,pointx,arrx,cpointx,n)
    dnc(n,pointy,arry,cpointy,n)
    arrx = np.concatenate((np.array([pointx[0]]),arrx,np.array([pointx[len(pointx)-1]])))
    arry = np.concatenate((np.array([pointy[0]]),arry,np.array([pointy[len(pointy)-1]])))
    for i in range(n,-1,-1):
        if (i==n):      
            recordx[i] = arrx
            recordy[i] = arry
        else:
            recordx[i] = recordx[i+1][::2]
            recordy[i] = recordy[i+1][::2]
    return recordx,recordy,cpointx,cpointy
