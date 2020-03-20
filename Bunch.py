import numpy as np
import math
import copy
import scipy.constants
import random
from Chargedparticle import Proton

class Bunch:

    def __init__(self, BunchSize):
        self.BunchSize=BunchSize
        self.particles=[]

    """Used to create charged particles and groups of particles. Checks for negative mass, zero charge and if two particles have the same
    initial position and throws errors for each case.
    """
    def AddParticle(self, initialPosition, initialVelocity, initialAcceleration, Name):
        NewParticle = Proton(initialPosition, initialVelocity, initialAcceleration, Name)
        if NewParticle.mass<0:
            raise ValueError("Particle mass cannot be negative.")
        if NewParticle.Charge==0:
            raise ValueError("Particle must be charged.")
        self.particles.append(NewParticle)

    """Creates a bunch of particles using the above AddParticle method, using a bunchsize and random velocities.
    """
    def CreateBunch(self):
        acc=np.array([0.0,0.0,0.0], dtype=float)
        for i in range(1,self.BunchSize+1):
            vel=np.array([0, random.uniform(9900,10100), 0], dtype=float)
            pos=np.array([random.uniform(0,0.1),random.uniform(0,0.1),0], dtype=float)
            self.AddParticle(pos,vel,acc,"Proton{}".format(i))

    """Using specific position values for each particle the mean average position of the bunch is calculated at each time step and appened to a list called self.avposition
    """
    def AverPosition(self):
        meanposition = np.array([0,0,0], dtype=float)
        for i in self.particles:
            meanposition += i.position
        avposition = (meanposition/len(self.particles))
        return avposition
    
    """Using specific velocity values for each particle the mean average velocity of the bunch is calculated in a numpy array and appened to a list called self.avvelocity
    """
    def AverVelocity(self):
        avervelocity = np.array([0,0,0], dtype=float)
        for i in self.particles:
            avervelocity += i.velocity
        avvelocity = (avervelocity/len(self.particles))
        return avvelocity

    """Using the magnitude of the velocity values for each particle the relativistic kinetic energy is calculated for each one, the average calculated and then appened to a list called self.avkinetic
    """
    def AverKinetic(self):
        averkinetic = 0
        for i in self.particles:
            magvel = np.linalg.norm(i.velocity)
            gamma = math.sqrt(1/(1-(magvel**2)/(scipy.constants.c**2)))
            kineticenergy = (gamma-1)*i.mass*scipy.constants.c**2
            averkinetic += kineticenergy/scipy.constants.e
        avkinetic = (averkinetic/len(self.particles))
        return avkinetic

    """Calculates the spread of the bunch using the positions furthest from the average position of the bunch, and then calculating the standard deviation
    """
    def BunchSpread(self):
        spread=0
        averagepos=self.AverPosition()
        for i in self.particles:
            spread += (np.linalg.norm(i.position - averagepos))**2
        StandardDeviation = math.sqrt(spread/(len(self.particles)-1))
        return StandardDeviation

    def PositionSpread(self):
        xspread=0
        yspread=0
        zspread=0
        averagepos=self.AverPosition()
        for i in self.particles:
            xspread += math.sqrt((i.position[0] - averagepos[0])**2/(len(self.particles)-1))
            yspread += math.sqrt((i.position[1] - averagepos[1])**2/(len(self.particles)-1))
            zspread += math.sqrt((i.position[2] - averagepos[2])**2/(len(self.particles)-1))
        XYSpread = np.array([xspread, yspread, zspread], dtype=float)
        return XYSpread

    def EnergySpread(self):
        energyspread=0
        averagekinetic=self.AverKinetic()
        for i in self.particles:
            magvel = np.linalg.norm(i.velocity)
            gamma = math.sqrt(1/(1-(magvel**2)/(scipy.constants.c**2)))
            energyspread += np.abs((gamma-1)*i.mass*scipy.constants.c**2 - averagekinetic)
        KineticSpread = math.sqrt(energyspread/(len(self.particles)-1))
        return KineticSpread