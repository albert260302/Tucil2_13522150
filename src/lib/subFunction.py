import numpy as np
import math
#menghitung titik tengah antara 2 titik
def tengah(x1,y1,x2,y2):
    return (x1+x2)/2,(y1+y2)/2
#menghitung titik tengah antara 2 titik 1 dimensi
def mid(x1,x2):
    return (x1+x2)/2
# Menghitung jumlah titik jika diberikan n iterasi (rekursif)
def jumlahtitik(n:int):
    if (n==1):
        return 3
    else:
        return 2*jumlahtitik(n-1)-1
# Round
def round(n):
    if (n> int(n)+0.5):
        return math.ceil(n)
    else:
        return math.floor(n)
