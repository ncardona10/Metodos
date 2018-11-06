import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("fecha_manchas.dat")
t=data[:,0]
manchas=data[:,1]
plt.plot(t,manchas)
plt.savefig("fecha_manchas.pdf")
plt.close()
