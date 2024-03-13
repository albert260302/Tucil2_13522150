import numpy as np
import matplotlib.pyplot as plt
import math

def bruteForceT(max:int,t:float,j:int,p:float)->float:
    return math.comb(max-1,j)*((1-t)**(max-1-j))*(t**(j))*p

def bruteForce(n:int):
    iter = int(input("Masukkan jumlah iterasi: "))
    step = 1/iter
    x = np.arange(0,1,step)
    arrx = []
    arry = []
    for j in range(n):
        px,py = map(float,input(f"Msukkan titik P{j}: ").split())
        for i in range(len(x)):
            qx = bruteForceT(n,x[i],j,px)
            qy = bruteForceT(n,x[i],j,py)
            if (j==0):
                arrx.append(qx)
                arry.append(qy)
            else:
                arrx[i] += qx
                arry[i] += qy
        if (j==n-1):
            arrx.append(px)
            arry.append(py)
    print(arrx)
    print(arry)
    plt.plot(arrx,arry)
    plt.show()

bruteForce(4)
        