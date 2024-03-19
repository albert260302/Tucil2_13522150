from divAndConq import *
from bruteForce import *
from plotq import *
import time



if __name__=="__main__":
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
    print()
    print("Waktu yang dibutuhkan")
    start = time.time()
    brutex,brutey = bruteForce(niter,pointx,pointy)
    end = time.time()
    print(f"Brute Force: {(end-start)*1000} ms")
    start  = time.time()
    conqx,conqy,cpointx,cpointy = dvnconq(niter,pointx,pointy)
    end = time.time()
    print(f"Divide and Conquer: {(end-start)*1000} ms")
    animate_subplots(pointx,pointy,brutex,brutey,conqx,conqy,cpointx,cpointy)


    