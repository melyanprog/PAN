"""PAN DZ1"""

import numpy as np
import matplotlib.pyplot as plt

class Approx():
    def __init__(self):
        """data input"""
        self.H =  [0,500,1000,2000,3000,4000,5000,6000,7000]
        self.Ro = [1.22,1.17, 1.11, 1.00, 0.91, 0.82, 0.74, 0.66, 0.59]
        self.A =  [340.294, 338.370, 336.435, 332.532, 328.584, 324.589, 320.545, 316.452,312.306]
        self.Alpha = [1, 7.5, 10, 13, 16, 20]
        self.Cy = [0, 0.55, 0.75, 1, 1.25, 1.4]
        self.Cx = [0.02, 0.04, 0.05, 0.07, 0.1, 0.12]
        self.P = [10000*0.9, 9500*0.9, 9000*0.9, 8000*0.9, 7000*0.9, 6500*0.9]
        self.M = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
        self.V = [300, 400, 500, 600, 700, 800]

    def stepen(self):
        print("введите степень полинома")
        self.n = int(input())
       
    def approx(self, x, y, n1, n2):
        """approx func"""
        self.koefs = np.polyfit(x, y, self.n)
        self.val = np.polyval(self.koefs,x)
        print(f"koefs {n1} от {n2}")
        print(self.koefs)

    def draw(self, x, y, name, number):
        """draw func"""
        plt.figure(number)
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title(f"{name}")
        plt.plot(x, y, 'o',label = 'исходные данные')
        plt.plot(x, self.val, 'b', label = 'аппроксимированные данные')
        plt.grid(True)
        plt.legend()
        plt.show()
    
    def go(self):
        self.__init__()
        self.stepen()
        self.approx(self.H, self.Ro, "Ro", "H")
        self.draw(self.H, self.Ro, "Плотность от высоты", 1)
        self.approx(self.H, self.A, "A", "H")
        self.draw(self.H, self.A, "Скорость звука от высоты", 2)
        self.approx(self.M, self.P, "P", "M")
        self.draw(self.M, self.P, "Тяга от числа маха", 3)
        self.approx(self.Alpha, self.Cy, "Cy", "a")
        self.draw(self.Alpha, self.Cy, "Cy от альфа", 4)
        self.approx(self.Alpha, self.Cx, "Cx", "a")
        self.draw(self.Alpha, self.Cx, "Cx от альфа", 5)
        
ap = Approx()
ap.go()


