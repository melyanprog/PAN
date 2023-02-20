"""PAN DZ1"""

import numpy as np
import matplotlib.pyplot as plt

class Aprox:
    def input(self):
        """data input"""
        print("введите массив X")
        self.x = list(map(float, input().split()))
        print("введите массив Y")
        self.y = list(map(float, input().split()))
       
    def approx(self):
        """approx func"""
        print("введите степень полинома")
        n = int(input())
        koefs = np.polyfit(self.y, self.x, n)
        self.val = np.polyval(koefs,self.y)

    def draw(self):
        """draw func"""
        plt.plot(self.x,self.y,'o',label = 'исходные данные')
        plt.plot(self.val,self.y,'b', label = 'аппроксимированные данные')
        plt.grid(True)
        plt.legend()
        plt.show()
    
    def go(self):
        self.input()
        self.approx()
        self.draw()

    
ap = Aprox()
ap.go()


