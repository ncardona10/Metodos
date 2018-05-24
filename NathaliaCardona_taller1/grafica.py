
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("TempPromedios.txt", delimiter=" ")
plt.plot(data[:,1], data[:,0])
plt.xlabel(r"$Tiempo\ (A\~nos)$ ")
plt.ylabel(r"$Temperatura\ promedio\ (^{\circ}C)$")
plt.savefig("temppromedios.png")
