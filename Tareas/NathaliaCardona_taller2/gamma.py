import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate


def functi(x, z):
    return x**(z-1) * np.exp(-x) + (1/x)**(z+1) * np.exp(-(1/x))


def gamma(n):
    n_points = 1000
    x1 = np.linspace(0.00001, 1, n_points)
    return integrate.simps(functi(x1, n), x1)
