"""PAN DZ1"""

import numpy as np
import matplotlib.pyplot as plt
from array import array

#H = array('f', [0,500,1000,2000,3000,4000,5000,6000,7000])
#Ro = array('f', [1.22,1.17, 1.11, 1.00, 0.91, 0.82, 0.74, 0.66, 0.59])
class Approx():
    def __init__(self):
        """data input"""
        self.H = array('f', [0,500,1000,2000,3000,4000,5000,6000,7000])
        self.Ro = array('f', [1.22,1.17, 1.11, 1.00, 0.91, 0.82, 0.74, 0.66, 0.59])
        self.A = array('f', [340.294, 338.370, 336.435, 332.532, 328.584, 324.589, 320.545, 316.452,312.306])
        self.Alpha = array('f', [1, 7.5, 10, 13, 16, 20])
        self.Cy = array('f', [0, 0.55, 0.75, 1, 1.25, 1.4])
        self.Cx = array('f', [0.02, 0.04, 0.05, 0.07, 0.1, 0.12])
        # self.Pv = array('f', [10000, 9000, 8500, 8000, 7000, 6500])
        # self.Ph = array('f', [6200, 6100, 6050, 6000, 5800, 5600, 5500, 4600, 4100 ])
        self.P = array('f', [10000*0.9, 9500*0.9, 9000*0.9, 8000*0.9, 7000*0.9, 6500*0.9])
        self.M = array('f', [0.2, 0.3, 0.4, 0.5, 0.6, 0.7])
        self.V = array('f', [300, 400, 500, 600, 700, 800])

    def stepen(self):
        print("введите степень полинома")
        self.n = int(input())
       
    def approx(self, x, y):
        """approx func"""
        koefs = np.polyfit(y, x, self.n)
        self.val = np.polyval(koefs,y)
        print(koefs)
        print(self.val)

    def draw(self, x, y, name, number):
        """draw func"""
        plt.figure(number)
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title(f"{name}")
        plt.plot(x, y, 'o',label = 'исходные данные')
        plt.plot(self.val, y, 'b', label = 'аппроксимированные данные')
        plt.grid(True)
        plt.legend()
        plt.show()
    
    def go(self):
        self.__init__()
        self.stepen()
        self.approx(self.H, self.Ro)
        self.draw(self.H, self.Ro, "Плотность от высоты", 1)
        self.approx(self.H, self.A)
        self.draw(self.H, self.A, "Скорость звука от высоты", 2)
        self.approx(self.M, self.P)
        self.draw(self.M, self.P, "Тяга от числа маха", 3)
        self.approx(self.Alpha, self.Cy)
        self.draw(self.Alpha, self.Cy, "Cy от альфа", 4)
        self.approx(self.Alpha, self.Cx)
        self.draw(self.Alpha, self.Cx, "Cx от альфа", 5)
        # self.approx(self.V, self.Pv)
        # self.draw(self.V, self.Pv, "Тяга от скорости", 5)
        


    
ap = Approx()
ap.go()


