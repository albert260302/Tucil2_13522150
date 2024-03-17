import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import time

def animate_subplots(orix, oriy,bfx,bfy, dnqx,dnqy):
    # Function to generate random data points
    def generate_data():
        x = np.arange(0, 10, 0.1)
        y = np.sin(x)
        return x, y

    # Function to update the plot
    def update(n):

        ax1.clear()
        ax1.plot(bfx[n], bfy[n],'b-')
        ax1.plot(orix,oriy, 'go--')
        ax1.set_title(f'Brute Force Method')
        ax1.set_xlabel('X')
        ax1.set_ylabel('Y')
        ax1.set_xlim(np.min(bfx[n])-1, np.max(bfx[n])+1)
        ax1.set_ylim(np.min(bfy[n])-1, np.max(bfy[n])+1)
        ax1.set_aspect((np.max(bfx[n])-np.min(bfx[n])) / (np.max(bfy[n])-np.min(bfy[n])))  # Adjust aspect ratio

        ax2.clear()
        ax2.plot(dnqx[n], dnqy[n],'r-')
        ax2.plot(orix,oriy, 'go--')
        ax2.set_title(f'Divide and Conquer Method')
        ax2.set_xlabel('X')
        ax2.set_ylabel('Y')
        ax2.set_xlim(np.min(dnqx[n])-1, np.max(dnqx[n])+1)
        ax2.set_ylim(np.min(dnqy[n])-1, np.max(dnqy[n])+1)
        ax2.set_aspect((np.max(dnqx[n])-np.min(dnqx[n])) / (np.max(dnqy[n])-np.min(dnqy[n])))  # Adjust aspect ratio

        fig.suptitle(f"iterasi {n}")

    # Create a figure and multiple axes objects
    fig, (ax1,ax2) = plt.subplots(1,2)
   

    for i in range(len(bfx)):
        update(i+1)
        plt.pause(1)

    plt.show()

    

