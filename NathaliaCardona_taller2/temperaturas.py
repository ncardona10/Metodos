import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("nottem.csv", skiprows=1, delimiter=",")
num = np.array(data[:,0])
year = np.array(data[:,1])
temp = np.array(data[:,2])
plt.plot(year,temp)
maximos = []
tiempo = []
subiendo = False
crece=[]
t=[]
for i in range(len(temp)-1):
        if temp[i]<temp[i+1]:
            crece.append(temp[i])
            t.append(year[i])
            subiendo=True
        if temp[i]>temp[i+1]:
            if subiendo:
                maximos.append(temp[i])
                tiempo.append(year[i])
                crece.append(temp[i])
                t.append(year[i])
                plt.plot(t,crece,c="red")
                crece=[]
                t=[]
            subiendo=False


plt.scatter(tiempo,maximos,c="red", label="Maximos")
plt.plot(year[0],temp[0],c="red",label="Intervalos crecientes")
plt.xlabel(r"$Tiempo\ (A\~nos)$")
plt.ylabel(r"$Temperatura(^{\circ} C)$")
plt.legend()
plt.grid()
plt.savefig("temp_analisis.png")
plt.close()
