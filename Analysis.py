import numpy as np
import math
import matplotlib.pyplot as plt
from Synchrotron import Synchrotron

data=np.load("ProtonBunch.npy")
plot="EnergySpread"

timelist=[]
for lists in data:
    timelist.append(np.linalg.norm(lists[0]))

if plot == "Velocity":
    vel=[]
    for lists in data:
        vel.append(np.linalg.norm(lists[2]))
    plt.plot(timelist,vel,'b-', linewidth=0.7, label='Average Bunch Velocity')
    plt.xlabel('Time (s)')
    plt.ylabel('Average Velocity (ms-1)')
    plt.legend()
    plt.show()
elif plot == "Position":
    x=[]
    y=[]
    for lists in data:
        x.append(lists[1][0])
        y.append(lists[1][1])
    plt.plot(x,y,'r-',linewidth = 0.7,label='Average Bunch Position')
    plt.xlabel('Average x Position (m)')
    plt.ylabel('Average y Position (m)')
    plt.legend()
    plt.show()
elif plot == "Kinetic":
    kin=[]
    for lists in data:
        kin.append(lists[3])
    plt.plot(timelist,kin,'g-', linewidth=0.7, label='Average Bunch Kinetic Energy')
    plt.xlabel('Time (s)')
    plt.ylabel('Average Kinetic Energy (eV)')
    plt.legend()
    plt.show()
elif plot == "Spread":
    spread=[]
    for lists in data:
        spread.append(lists[4])
    plt.plot(timelist,spread,'r-', linewidth=0.7, label='Standard deviation of the particle positions')
    plt.xlabel('Time (s)')
    plt.ylabel('Spread of the Bunch (m)')
    plt.legend()
    plt.show()
elif plot == "EnergySpread":
    spread=[]
    for lists in data:
        spread.append(lists[5])
    plt.plot(timelist,spread,'m-', linewidth=0.7, label='Standard deviation of the particle kinetic energies')
    plt.xlabel('Time (s)')
    plt.ylabel('Standard deviation in the kinetic energy (J)')
    plt.legend()
    plt.show()
elif plot == "PosSpreadXY" or "PosSpreadXT" or "PosSpreadYT":
    Xspread=[]
    Yspread=[]
    for lists in data:
        Xspread.append(lists[6][0])
        Yspread.append(lists[6][1])
    if plot == "PosSpreadXY":    
        plt.plot(Xspread,Yspread,'r-', linewidth=0.7, label='Standard deviation of the particle positions')
        plt.xlabel('Spread in the x positions (m)')
        plt.ylabel('Spread in the y positions (m)')
        plt.legend()
        plt.show()
    elif plot == "PosSpreadXT":
        plt.plot(timelist,Xspread,'r-', linewidth=0.7, label='Standard deviation of the x positions against time')
        plt.ylabel('Spread in the x positions (m)')
        plt.xlabel('Time (s)')
        plt.legend()
        plt.show()
    elif plot == "PosSpreadYT":
        plt.plot(timelist,Yspread,'r-', linewidth=0.7, label='Standard deviation of the y positions against time')
        plt.ylabel('Spread in the y positions (m)')
        plt.xlabel('Time (s)')
        plt.legend()
        plt.show()
