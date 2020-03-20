import numpy as np
import math
import copy
import scipy.constants
import random
from Chargedparticle import Proton
from EMField import EMField
from Bunch import Bunch


class Synchrotron:
    def __init__(self, timestep, totaltime, intmethod, ElectricF, MagneticF, BunchSize):
        self.timestep = timestep
        self.totaltime = totaltime
        self.intmethod = intmethod
        self.ElectricF = ElectricF
        self.MagneticF = MagneticF
        self.BunchSize = BunchSize
        Field = EMField(Magnetic=self.MagneticF, Electric=self.ElectricF)
        self.Field = Field
        ParticleBunch = Bunch(self.BunchSize)
        self.Bunch = ParticleBunch
        self.Bunch.CreateBunch()

    """Loops over all the particles and updates their, acceleration, position and velocity using the defined update method.
    """
    def updateaccel(self, time):
        for i in self.Bunch.particles:
            i.acceleration = np.array([0,0,0], dtype=float)
            accel = self.Field.lorentzaccel(i, time)
            i.acceleration += accel
            i.update(self.timestep, self.intmethod)

    #def Orbit(self):
        #for i in self.particles:
            #gamma=1/(np.sqrt(1-((np.linalg.norm(i.velocity))*2)/(scipy.constants.c**2)))
            #rad=(i.mass*gamma*np.linalg.norm(i.velocity))/(scipy.constants.e*np.linalg.norm(self.MagneticF))
            #return rad

