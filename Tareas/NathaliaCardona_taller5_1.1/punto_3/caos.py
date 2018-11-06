import numpy as np
import matplotlib.pyplot as plt 

data = np.loadtxt("caos.txt")
q2 = data[:,0]
p2 = data[:,1]
plt.scatter(q2,p2)
plt.xlabel("q2")
plt.ylabel("p2")
plt.title("q2 vs p2")
plt.savefig("caos.pdf")
plt.close()