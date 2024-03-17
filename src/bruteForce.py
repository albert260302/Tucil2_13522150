from lib.subFunction import *

def bruteForceT(max:int,t:float,j:int,p:float)->float:
    return math.comb(max-1,j)*((1-t)**(max-1-j))*(t**(j))*p

def bruteForce(n:int,pointx,pointy):
    step = 1/(jumlahtitik(n)-1)
    x = np.arange(0,1,step)
    arrx = []
    arry = []
    for i in range(len(x)):
        for j in range(0,len(pointx)):
            if (j==0):
                arrx.append(bruteForceT(len(pointx),x[i],j,pointx[j]))
                arry.append( bruteForceT(len(pointy),x[i],j,pointy[j]))
            else:
                arrx[i] += bruteForceT(len(pointx),x[i],j,pointx[j])
                arry[i] += bruteForceT(len(pointy),x[i],j,pointy[j])
        if (i==len(x)-1):
            arrx.append(pointx[len(pointx)-1])
            arry.append(pointy[len(pointy)-1])
    recordx = {}
    recordy = {}
    for i in range(n,0,-1):
        if (i==n):      
            recordx[i] = arrx
            recordy[i] = arry
        else:
            recordx[i] = recordx[i+1][::2]
            recordy[i] = recordy[i+1][::2]
    return recordx,recordy