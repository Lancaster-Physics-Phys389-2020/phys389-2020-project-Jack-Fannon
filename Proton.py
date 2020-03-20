import numpy as np
import math
import copy
import scipy.constants
import matplotlib.pyplot as plt
from Synchrotron import Synchrotron

EField=np.array([0.0,0.00001,0.0], dtype=float)
BField=np.array([0,0,scipy.constants.m_p*10000/(500*scipy.constants.e)], dtype=float)

Period=(2*scipy.constants.pi*scipy.constants.m_p)/(scipy.constants.e*np.linalg.norm(BField))
print("Period =",Period)
Iterations=10000
Totaltime=10*Period
Timestep=Totaltime/Iterations
BunchSize=10
ProtonBunch = Synchrotron(Timestep,Totaltime,"Euler Cromer",EField,BField,BunchSize)

data=[]
for i in range(1,Iterations):
    time=ProtonBunch.timestep*i
    ProtonBunch.updateaccel(time)
    AverageVelocity=ProtonBunch.Bunch.AverVelocity()
    AverageKinetic=ProtonBunch.Bunch.AverKinetic()
    AveragePosition=ProtonBunch.Bunch.AverPosition()
    BunchSpread=ProtonBunch.Bunch.BunchSpread()
    PositionSpread=ProtonBunch.Bunch.PositionSpread()
    EnergySpread=ProtonBunch.Bunch.EnergySpread()
    item=[np.array([time]), copy.deepcopy(AveragePosition), copy.deepcopy(AverageVelocity), copy.deepcopy(AverageKinetic), copy.deepcopy(BunchSpread), copy.deepcopy(EnergySpread), copy.deepcopy(PositionSpread)]
    data.append(item)

print(data[0])

np.save("ProtonBunch",data,allow_pickle=True)
