import numpy as np
import math
def tengah(x1,y1,x2,y2):
    return (x1+x2)/2,(y1+y2)/2
def mid(x1,x2):
    return (x1+x2)/2
def jumlahtitik(n:int):
    if (n==1):
        return 3
    else:
        return 2*jumlahtitik(n-1)-1

def round(n):
    if (n> int(n)+0.5):
        return math.ceil(n)
    else:
        return math.floor(n)
def niter(n, iter):
    if (iter==0):
        return 2
    else:
        return niter(2*n-1,iter-1)
