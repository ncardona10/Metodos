import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("mat.dat")
Ex = np.loadtxt("Ex.dat")
Ey = np.loadtxt("Ey.dat")





y,x = np.mgrid[0:512:512j,0:512:512j]
u = Ex
v = Ey 
plt.streamplot(x, y, u, v, density=[1, 1],color="black",maxlength=0.5)
plt.imshow(data)

plt.tick_params

plt.xticks( [x for x in range(0,512,102)],[x for x in range(6)])
plt.yticks( [x for x in range(0,512,102)],[x for x in range(6)])
plt.xlabel("x (cm)")
plt.ylabel("y (cm)")
plt.title("Campo eléctrico y potencial")

plt.savefig('placas.pdf')
