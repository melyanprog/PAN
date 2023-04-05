import numpy as np
import matplotlib.pyplot as plt

n=3;
RO=[1.16727,1.11166,1.00655,0.90925,0.81934,0.73642,0.66011];
H=[500,1000,2000,3000,4000,5000,6000];
func_RO_H=np.polyfit(H,RO,n)
zRO_H=np.polyval(func_RO_H,H)
plt.plot(RO,H,'b--s')
plt.plot(zRO_H,H,'m')
plt.title('plotnost')
plt.grid(True);
plt.show()