import matplotlib.pyplot as plt
import numpy as np
import os

style={0:"c-", 1:"m-",2:"y-"}
def animate_subplots(orix, oriy,bfx,bfy, dnqx,dnqy,cpointx,cpointy):


    def update(n):
        fig.suptitle(f"iterasi {n}")

        ax1.clear()
        ax2.clear()
        ax1.set_title(f'Brute Force Method')
        ax1.set_xlabel('X')
        ax1.set_ylabel('Y')
        minx = min(np.min(bfx[n]),np.min(orix))
        miny = min(np.min(bfy[n]),np.min(oriy))
        maxx = max(np.max(bfx[n]),np.max(orix))
        maxy = max(np.max(bfy[n]),np.max(oriy))
        ax1.set_xlim(minx-1, maxx+1)
        ax1.set_ylim(miny-1, maxy+1)
        ax1.plot(orix,oriy, 'go--') 
        for i in range(len(bfx[n])-1):
            ax1.plot(bfx[n][i:i+2], bfy[n][i:i+2],'bo-')
            plt.pause(0.5)

        ax1.set_aspect((maxx-minx) / (maxy-miny)) 


        

        if (n!=0):
            ax2.plot(orix,oriy, 'go--')
            minx = min(np.min(dnqx[n]),np.min(orix))
            miny = min(np.min(dnqy[n]),np.min(oriy))
            maxx = max(np.max(dnqx[n]),np.max(orix))
            maxy = max(np.max(dnqy[n]),np.max(oriy))
            ax2.set_xlim(minx-1, maxx+1)
            ax2.set_ylim(miny-1, maxy+1)
            ax2.set_title(f'Divide and Conquer Method')
            ax2.set_xlabel('X')
            ax2.set_ylabel('Y')
            lenStep = len(cpointx[n])
            k = 2
            while k < lenStep:
                for j in range(len(cpointx[n][k])):
                    plt.scatter(cpointx[n][k][j],cpointy[n][k][j],color='black',marker='o',label='Dots',s=10)
                k += 3
            for i in range(lenStep-1,-1,-1):
                for j in range(0,len(cpointx[n][i])-1):
                        ax2.plot(cpointx[n][i][j:j+2], cpointy[n][i][j:j+2],style[i%3])
                        plt.pause(1/(len(cpointx[n][i])-1))
            for i in range(len(dnqx[n])-1):
                ax2.plot(dnqx[n][i:i+2],dnqy[n][i:i+2],'r-')
                plt.pause(5/len(dnqx[n]))
            plt.pause(1)
        ax2.clear()
        ax2.plot(orix,oriy, 'go--')
        if (n==0):
            plt.pause(1)
        ax2.plot(dnqx[n], dnqy[n],'ro-')
        minx = min(np.min(dnqx[n]),np.min(orix))
        miny = min(np.min(dnqy[n]),np.min(oriy))
        maxx = max(np.max(dnqx[n]),np.max(orix))
        maxy = max(np.max(dnqy[n]),np.max(oriy))
        ax2.set_xlim(minx-1, maxx+1)
        ax2.set_ylim(miny-1, maxy+1)
        ax2.set_title(f'Divide and Conquer Method')
        ax2.set_xlabel('X')
        ax2.set_ylabel('Y')
        
        ax2.set_aspect((maxx-minx) / (maxy-miny)) 



        


    fig, (ax1,ax2) = plt.subplots(1,2)
   

    for i in range(len(bfx)):
        update(i)
        plt.pause(1)
    
    print(f"Pilih iterasi yang diinginkan: ")
    print(f"1.  Iterasi mulai dari 0 sampai {len(bfx)-1}: ")
    print("2.  (-1) untuk menonton kembali proses pembentukan [tidak pakai kurung]")
    print("3.  (-2) untuk selesai [tidak pakai kurung]")
    iter = int(input("Iterasi ke: "))

    while (iter!=-2):
        if (iter>len(bfx) and iter < -2):
            print(f"Iterasi di luar jangkauan !")
            print(f"Input kembali")
            print()
        elif (iter==-1): 
            for i in range(len(bfx)):
                update(i)
                plt.pause(1)
        else:
            update(iter)
            plt.pause(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Pilih iterasi yang diinginkan: ")
        print(f"1.  Iterasi mulai dari 0 sampai {len(bfx)-1}: ")
        print("2.  (-1) untuk menonton kembali proses pembentukan [tidak pakai kurung]")
        print("3.  (-2) untuk selesai [tidak pakai kurung]")
        iter = int(input("Iterasi ke: "))

    print("Terima kasih, sehat-sehat selalu !")
    plt.pause(2)
    plt.close()

    

