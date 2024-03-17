import numpy as np
import matplotlib.pyplot as plt
import math

fig, (ax1, ax2) = plt.subplots(1, 2)

def bruteForceT(max:int,t:float,j:int,p:float)->float:
    return math.comb(max-1,j)*((1-t)**(max-1-j))*(t**(j))*p
def jumlahtitik(n:int):
    if (n==1):
        return 3
    else:
        return 2*jumlahtitik(n-1)-1

    return 
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

def tengah(x1,y1,x2,y2):
    return (x1+x2)/2,(y1+y2)/2
def mid(x1,x2):
    return (x1+x2)/2



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

def niter(n, iter):
    if (iter==1):
        return n
    else:
        return niter(2*n-1,iter-1)
if __name__=="__main__":
    pointx = np.array([])
    pointy = np.array([])
    npoint = int(input("Masukkan jumlah titik: "))
    for i in range(npoint):
        px,py = map(float,input(f"Msukkan titik P{i}: ").split())
        pointx = np.append(pointx,px)
        pointy = np.append(pointy,py)
    niter = int(input("Masukkan jumlah iterasi: "))
    brutex,brutey = bruteForce(niter,pointx,pointy)
    conqx,conqy = dvnconq(niter,pointx,pointy)
    ax1.plot(brutex[niter],brutey[niter])
    ax1.set_title("DnQ-method Curve")
    print("Brute force")
    print(brutex[niter])
    print(brutey[niter])
    ax2.plot(conqx[niter],conqy[niter])
    print("DNQ method")
    print(conqx[niter])
    print(conqy[niter])
    ax2.set_title("DnQ-method Curve")
    plt.show()


    