import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("monthrg.dat")
agnios = np.array(data[:,0])
manchas = np.array(data[:,3])
d = np.array(data[:,2])
meses = np.array(data[:,1])
t = agnios+ meses/12
ii = t>1900
year = t[ii]
manch = manchas[ii]
sol=np.array([year,manch])
neu_data = np.savetxt("fecha_manchas.dat", sol.T, delimiter=' ')
