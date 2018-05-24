import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt("monthrg.dat")
agnios = np.array(data[:,0])
manchas = np.array(data[:,3])
dias = np.array(data[:,2])
meses = np.array(data[:,1])
#Genera un array con true si se cumple la condicion y false en otro caso
i = dias>0
#Crea un nuevo array que solo contiene las posicion con true del i
t = agnios[i]+ meses[i]/12
manchas_agnios = manchas[i]
#Grafica la cantidad de manchas en funcion del tiempo
plt.plot(t,manchas_agnios)
plt.savefig("manchas.png")
plt.close()

#Encontrar la funcion que se ajusta a los datos
puntos=len(t)
#Crea y transpone las dos matrices
A= np.transpose(np.array([np.cos(((2*np.pi)/11)*t),np.sin(((2*np.pi)/11)*t),np.ones(puntos)]))
manchas=np.transpose(manchas_agnios)

new_A=np.dot(np.transpose(A),A)
new_manchas=np.dot(np.transpose(A),manchas)
sol=np.linalg.solve(new_A,new_manchas)
a=np.sqrt(sol[0]+sol[1])
b=np.arccos(sol[0]/a)
c=sol[2]

tiempo = np.linspace(min(t),max(t),puntos)
manchitas =  a*np.cos(((2*np.pi)/11)*tiempo+b)+c*np.ones(puntos)

plt.scatter(t,manchas,alpha=0.5, label="Datos")
plt.plot(tiempo,manchitas,label="Fit")
plt.grid()
plt.legend()
plt.xlabel("Tiempo (s)")
plt.ylabel("Manchas")
plt.savefig("fit.png")
plt.close()
