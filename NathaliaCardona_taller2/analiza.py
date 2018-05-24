import numpy as np
import matplotlib.pyplot as plt
#Punto 1:a
data = np.loadtxt("co2_annmean_mlo.txt", skiprows=57)
year = np.array(data[:,0])
mean = np.array(data[:,1])
unc = np.array(data[:,2])
plt.plot(year,mean)
plt.xlabel(r"$Tiempo\ (A\~nos)$")
plt.ylabel(r"$Concentracion\ de\ CO_2\ en\ la\ atmosfera$")
plt.grid()
plt.savefig("C02.png")
plt.close()
#Punto 1:b
d_mean = mean[1:]-mean[:-1]
plt.plot(year[:-1],d_mean)
plt.xlabel(r"$Tiempo\ (A\~nos)$")
plt.ylabel(r"$Tasa\ de\ cambio\ de\ la\ concentracion\ de\ CO_2 $")
plt.grid()
plt.savefig("derivada1_C02.png")
plt.close()
#Punto 1:c
d2_mean = d_mean[1:]-d_mean[:-1]
avg = np.mean(d2_mean)
avg_array = np.ones(len(d2_mean))*avg
plt.plot(year[:-2],d2_mean,label="Segunda derivada")
plt.plot(year[:-2],avg_array,c="red", label="Promedio",linestyle="--")
plt.legend()
plt.xlabel(r"$Tiempo\ (A\~nos)$")
plt.ylabel(r"$Segunda\ derivada\ de\ la\ concentracion\ de\ CO_2 $")
plt.grid()
plt.savefig("derivada2_C02.png")
plt.close()
