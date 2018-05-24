import numpy as np
import matplotlib.pyplot as plt

plt.figure()

angulos = np.linspace(0,10*np.pi,10000)
a=0.5
b=0.5
r=a + b*angulos

x = r*np.cos(angulos)
y = r*np.sin(angulos)

plt.plot(x,y,"o",ms=3)
plt.axis("scaled")
plt.xlim(-20, 20)

plt.show()
