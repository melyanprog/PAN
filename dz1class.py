"""PAN DZ1"""

import numpy as np
import matplotlib.pyplot as plt

class Aprox:
    def input(self):
        print("введите число точек N")
        N = int(input())
        print("введите массив X")
        self.x = []
        for i in range(N):
            self.x.append(int(input()))
        print("введите массив Y")
        self.y = []
        for i in range(N):
            self.y.append(int(input()))
       

    def approx(self):
        koefs = np.polyfit(self.y, self.x, 5)
        self.val = np.polyval(koefs,self.y)

    def draw(self):
        plt.plot(self.y,self.x,'o',label = 'исходные данные')
        plt.plot(self.y,self.val,'b', label = 'апроксимированные данные')
        plt.grid(True)
        plt.legend()
        plt.show()
    
    def go(self):
        self.input()
        self.approx()
        self.draw()

    
ap = Aprox()
ap.go()


