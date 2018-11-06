import numpy as np
import matplotlib.pyplot as plt
#Ejercicio de practica
xp = np.array([1,2,3])
yp = np.array([4,3,1])
A = np.zeros((3,3))
b = np.zeros(3)
for i in range(3):
    A[i] = xp[i]**2, xp[i], 1
    b[i] = yp[i]
#print("Array A")
#print(A)
#print("Array b")
#print(b)
sol = np.linalg.solve(A,b)
#print('La solucion es:', sol)
#print('A dot sol:', np.dot(A,sol))
plt.plot(xp,yp,'ro')
x = np.linspace(-3,5,100)
y = sol[0]*x**2 + sol[1]*x + sol[2]
plt.plot(x,y,'b')
plt.savefig('parabola.png')
plt.close()
#Ejercicio 1
tp = np.array([0,0.25,0.5,0.75])
yp2 = np.array([3,1,-3,1])
C = np.zeros((4,4))
l = np.zeros(4)
for i in range(4):
    C[i] = np.cos(np.pi*tp[i]), np.cos(2*np.pi*tp[i]) , np.cos(3*np.pi*tp[i]),np.cos(4*np.pi*tp[i])
    l[i] = yp2[i]
sol2 = np.linalg.solve(C,l)
plt.plot(tp,yp2,'ro')
xx = np.linspace(0,np.pi,500)
yy = sol2[0]*np.cos(np.pi*xx)+sol2[1]*np.cos(2*np.pi*xx)+sol2[2]*np.cos(3*np.pi*xx)+sol2[3]*np.cos(4*np.pi*xx)
plt.plot(xx,yy,'b')
plt.savefig('solucion.png')
plt.close()
#Minimos cuadrados
data = np.loadtxt("../../ejercicios/2018-10/05.SistemasEcuaciones/tendencia.dat")
plt.scatter(data[:,0], data[:,1], s=1.0)
plt.savefig('puntos.png')
plt.close()
xxx = np.array(data[:,0])
yyy = np.array(data[0,:])
