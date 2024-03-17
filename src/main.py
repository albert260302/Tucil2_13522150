from divAndConq import *
from bruteForce import *
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2)


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


    