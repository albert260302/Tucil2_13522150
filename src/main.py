from divAndConq import *
from bruteForce import *
from plotq import *
import matplotlib.pyplot as plt



if __name__=="__main__":
    # flag = True
    # while flag:
    pointx = np.array([])
    pointy = np.array([])
    cpointx = {}
    cpointy = {}
    npoint = int(input("Masukkan jumlah titik: "))
    for i in range(npoint):
        px,py = map(float,input(f"Msukkan titik P{i}: ").split())
        pointx = np.append(pointx,px)
        pointy = np.append(pointy,py)
    niter = int(input("Masukkan jumlah iterasi: "))
 
    conqx,conqy,cpointx,cpointy = dvnconq(niter,pointx,pointy)
    brutex,brutey = bruteForce(niter,pointx,pointy)

    animate_subplots(pointx,pointy,brutex,brutey,conqx,conqy,cpointx,cpointy)


    