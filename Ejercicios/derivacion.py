import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return np.exp(-(x**2))
def deriva (f,x,h,metodo=" "):
     df=0.0
     if(metodo=="fd"):
         df=(f(x+h)-f(x))/h
     elif(metodo=="cd"):
         df=(f(x+h)-f(x-h))/(2.*h)
     else:
         df=(f(x+(h/4.))-f(x-(h/4.)))/(h/2.)
     return df

iteracion = 100
logh = 10**np.linspace(-16, 6, iteracion)
error_fd = np.zeros(iteracion)
error_cd = np.zeros(iteracion)
error_ed = np.zeros(iteracion)
analitico = -2*f(1)
for i in range(iteracion):
    numerico=deriva(f, 1.0, logh[i], metodo="fd")
    error_fd[i]= abs((analitico-numerico)/analitico)

    numerico=deriva(f, 1.0, logh[i], metodo="cd")
    error_cd[i]= abs((analitico-numerico)/analitico)

    numerico=deriva(f, 1.0, logh[i], metodo="ed")
    error_ed[i]= abs((analitico-numerico)/analitico)

logh = np.log10(logh)
plt.plot(logh, np.log10(error_fd), label = "fd")
plt.plot(logh, np.log10(error_cd), label = "cd")
plt.plot(logh, np.log10(error_ed), label = "ed")
plt.xlabel('$\log_{10} h$')
plt.ylabel('$\log_{10}$ Error')
plt.title("Error en el calculo de la derivada")
plt.legend()

plt.savefig('error.png')
