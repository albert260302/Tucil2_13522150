from lib.subFunction import *

def findControlPoint(point, result, cpoint, iter):
    length = len(point)
    if length == 2:
        midPoint = mid(point[0], point[1])
        result[:] = [point[0], midPoint, point[1]]
        cpoint[iter].append(result)

    else:
        midarr = []
        temp = []
        for i in range(length - 1):
            midPoint = mid(point[i], point[i + 1])
            midarr.append(midPoint)
            temp.extend([point[i], midPoint])
        temp.append(point[length - 1])


        resultN = []
        findControlPoint(midarr, resultN, cpoint, iter)

        cpoint[iter].append(temp)


        result[:] = [point[0], *resultN, point[length - 1]]

    return result

def dncRekursi(n:int, point, result, cpoint, max_val):
    length = len(point)
    if n == 0:
        result = []
    else:
        newPoint = []
        findControlPoint(point, newPoint, cpoint, max_val - n + 1)
        newLength = len(newPoint)
        resultL = []

        dncRekursi(n - 1, newPoint[0:newLength // 2 + 1], resultL, cpoint, max_val)
        resultR = []
        dncRekursi(n - 1, newPoint[newLength // 2:newLength], resultR, cpoint, max_val)
        result[:] = resultL + [newPoint[newLength // 2]] + resultR

def dvnconq(n:int, pointx, pointy):
    recordx = {}
    recordy = {}
    cpointx = {}
    cpointy = {}
    for i in range(n):
        cpointx[i+1] = []
        cpointy[i+1] = []
    arrx = []
    arry = []
    dncRekursi(n, pointx, arrx, cpointx, n)
    dncRekursi(n, pointy, arry, cpointy, n)
    arrx = [pointx[0]] + arrx + [pointx[-1]]
    arry = [pointy[0]] + arry + [pointy[-1]]
    for i in range(n, -1, -1):
        if i == n:
            recordx[i] = arrx
            recordy[i] = arry
        else:
            recordx[i] = recordx[i + 1][::2]
            recordy[i] = recordy[i + 1][::2]

    return recordx, recordy, cpointx, cpointy
