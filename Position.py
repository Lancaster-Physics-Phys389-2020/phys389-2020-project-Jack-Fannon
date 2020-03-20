import numpy as np
import math
import copy
import scipy.constants
import matplotlib.pyplot as plt
from Chargedparticle import Chargedparticle

data=np.load("Data.npy")

x=[]
y=[]

for lists in data:
    Proton = lists[1]
    x.append(Proton.position[0])
    y.append(Proton.position[1])
    #print(x,y)
    
plt.plot(x,y,'r-',linewidth = 0.7,label='Proton')
plt.xlabel('x-position (m)')
plt.ylabel('y-position (m)')
plt.legend()
plt.show() 
