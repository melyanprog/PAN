import numpy as np
import matplotlib.pyplot as plt

H = [0,500,1000,2000,3000,4000,5000,6000,7000]
A =  [340.294, 338.370, 336.435, 332.532, 328.584, 324.589, 320.545, 316.452,312.306]
A =  [340.294, 338.370, 336.435, 332.532, 328.584, 324.589, 320.545, 316.452,312.306]
Alpha = [1, 7.5, 10, 13, 16, 20]
Cy = [0, 0.55, 0.75, 1, 1.25, 1.4]
Cx = [0.02, 0.04, 0.05, 0.07, 0.1, 0.12]
P = [10000*0.9, 9500*0.9, 9000*0.9, 8000*0.9, 7000*0.9, 6500*0.9]
M = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7]

def Ro_H():
    res = []
    for i in H:
        res.append(-0.0001*i + 1.2)
    return res

def A_H():
    res = []
    for i in H:
        res.append(-0.0038*i + 340)
    return res

def P_M():
    res = []
    for i in M:
        res.append(33333.3*pow(i, 3) - 48214.3*pow(i, 2) + 14773.8*i + 7671.4)
    return res

def Cy_Alpha():
    res = []
    for i in Alpha:
        res.append(-0.0002*pow(i, 3) + 0.0039*pow(i, 2) + 0.059*i - 0.061)
    return res

def Cx_Alpha():
    res = []
    for i in Alpha:
        res.append(0.0007*pow(i, 2) - 0.0025*i + 0.022)
    return res

def draw(x,y,n1,n2 ):
    plt.figure()
    plt.plot(x, y , 'r')
    plt.title(f'График {n1} от {n2}')
    plt.grid(True)
    plt.show()

draw(H, Ro_H(), 'плотности', 'высоты')
draw(H, A_H(), 'скорости звука', 'высоты')
draw(M, P_M(), 'тяги', 'числа маха')
draw(Alpha, Cy_Alpha(), 'Cy', 'альфа')
draw(Alpha, Cx_Alpha(), 'Cx', 'альфа')
