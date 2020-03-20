import numpy as np
import math
import copy
import scipy.constants

class EMField:

    def __init__(self, Magnetic=np.array([0,0,0], dtype=float), Electric=np.array([0,0,0], dtype=float)):   
        self.Magnetic=Magnetic
        self.Electric=Electric
        self.VaryingElectric=np.array([0,0,0], dtype=float)

    """Calculates Lorentz accleration, has a particle instance passed to it, using veloity, charge and mass and the electric and magnetic 
    fields.
    """
    def update(self, time):
        pass

    def electricfield(self, particle, time):
        ElectricFreq=particle.Charge*np.linalg.norm(self.Magnetic)/particle.mass
        self.VaryingElectric=self.Electric*math.sin(ElectricFreq*time)

    def lorentzaccel(self, particle, time):
        self.VaryingElectric=np.array([0,0,0], dtype=float)
        if -25 <= particle.position[2] <= 25:
            self.electricfield(particle, time)
        LorForce=self.VaryingElectric+np.cross(particle.velocity,self.Magnetic)
        scalar=particle.Charge/particle.mass
        return scalar*LorForce