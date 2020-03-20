import numpy as np
import math
import copy
import scipy.constants
import pytest
from EMField import EMField
from Chargedparticle import Proton

class TestEMField:

    def __init__(self):
        self.field=0
        self.proton=0
        self.time=0

    def setUp(self):
        self.field = EMField(np.array([0,0,0.0000001], dtype=float), np.array([0.0,0.00001,0.0], dtype=float))
        self.proton=Proton(np.array([0,0,0], dtype=float), np.array([0,1000,0], dtype=float), np.array([0,0,0], dtype=float), "Proton")
        self.time = 5        

    def test_lorentzaccel(self):
        assert(self.field.lorentzaccel(self.proton, self.time) == np.array([9578.83322415,-667.00632589,0.0])).all()