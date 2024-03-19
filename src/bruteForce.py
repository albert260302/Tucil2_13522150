from lib.subFunction import *

# Menghitung B(t) untuk titik p
def bernsteinPoly(max:int,t:float,j:int,p:float)->float:
    return math.comb(max-1,j)*((1-t)**(max-1-j))*(t**(j))*p

# Fungsi utama metode Brute Force
def bruteForce(n:int,pointx,pointy):
    step = 1/(jumlahtitik(n)-1)
    x = np.linspace(0,1,1001)
    arrx = []
    arry = []
    for i in range(len(x)):
        for j in range(0,len(pointx)):
            if (j==0):
                arrx.append(bernsteinPoly(len(pointx),x[i],j,pointx[j]))
                arry.append( bernsteinPoly(len(pointy),x[i],j,pointy[j]))
            else:
                arrx[i] += bernsteinPoly(len(pointx),x[i],j,pointx[j])
                arry[i] += bernsteinPoly(len(pointy),x[i],j,pointy[j])
    recordx = {}
    recordy = {}
    x = np.arange(0,1,step)
    x = np.append(x,1)
    resultx = []
    resulty = []
    for i in x:
        resultx.append(arrx[round(i*1000)])
        resulty.append(arry[round(i*1000)])
    for i in range(n,-1,-1):
        if (i==n):      
            recordx[i] = resultx
            recordy[i] = resulty
        else:
            recordx[i] = recordx[i+1][::2]
            recordy[i] = recordy[i+1][::2]

    return recordx,recordy