import numpy as np
import math
import copy
import scipy.constants
from Particle import Particle

class Chargedparticle(Particle):

    eCharge=scipy.constants.e
    
    def __init__(self, Position=np.array([0,0,0], dtype=float),
        Velocity=np.array([0,0,0], dtype=float),
        Acceleration=np.array([0,0,0], dtype=float),
        Name='Ball',
        Mass=scipy.constants.m_p,
        Charge=eCharge):
        super().__init__(Position=Position, Velocity=Velocity, Acceleration=Acceleration, Name=Name, Mass=Mass)
        self.Charge=Charge

    def __repr__(self):
        return 'Charged Particle: {0}, Mass: {1.12.3e}, Charge:{2.12.3e}, Position: {3}, Velocity: {4}, Acceleration: {5}'.format(self.Name, self.mass,self.Charge,self.position,self.velocity,self.acceleration)

class Proton(Chargedparticle):

    def __init__(self, Position=np.array([0,0,0], dtype=float),
        Velocity=np.array([0,1000,0], dtype=float),
        Acceleration=np.array([0,0,0], dtype=float),
        Name='Proton'):
        Mass=scipy.constants.m_p
        Charge = scipy.constants.e
        super().__init__(Position=Position, Velocity=Velocity, Acceleration=Acceleration, Name=Name, Mass=Mass,Charge=Charge)