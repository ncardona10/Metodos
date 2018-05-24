import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt("album.txt")
sobre = np.arange(len(data[:,0]))
plt.plot(sobre,data[:,0],c="red", label="laminas")
plt.plot(sobre,data[:,1], label="repetidas")
plt.legend()
plt.savefig("grafAlbum.png")
plt.close()
