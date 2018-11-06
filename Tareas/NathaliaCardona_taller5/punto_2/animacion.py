import numpy as np
import matplotlib.pyplot as plt
import imageio
from os import listdir
from os import makedirs
from os.path import isfile, join, exists

data = np.loadtxt('cuerda.txt')
dt = 1 
npoints = int(200/dt)
ts = [x*1 for x in range(npoints)]

mypath = "./data/"
if not exists(mypath):
    makedirs(mypath)

print("exporting images...")
for t in ts:
    data = np.loadtxt('cuerda.txt')
    x0 = (np.where(data[:, 0] == t)[0])
    x = (data[x0][:, 1])
    y = (data[x0][:, 2])
    plt.plot(x, y)
    plt.title('t = ' + str(t))
    plt.ylim(-1, 1)
    plt.savefig("./data/imgen"+str(t)+".png")
    plt.close()
print("exported images.")

# HACER GIF
print("making gif...")
images = []
for i in range(200):
    images.append(imageio.imread("./data/" + "imgen" + str(i) + '.png'))
imageio.mimsave('./cuerda.gif', images, duration=0.1)
print("gif exported.")
