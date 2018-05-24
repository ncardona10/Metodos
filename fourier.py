import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq

x_temp = np.linspace(0,2*np.pi,51)
x = x_temp[:50]
y1 = np.sin(x)
y2 = 0.1*np.sin(x)
y3 = np.sin(10*x)
def fourier(x,y,name):
    f_real = x.copy()
    f_im = x.copy()
    temp_real = x.copy()
    temp_im = x.copy()
    for k in range(len(x)):
        for n in range(len(x)):
            temp_real[n] = y[n]*np.cos(-(2*np.pi*k*n)/len(x))
            temp_im[n] = y[n]*np.sin(-(2*np.pi*k*n)/len(x))
        f_real[k] = np.sum(temp_real)
        f_im[k] = np.sum(temp_im)
    norma_f = np.sqrt(f_real**2+f_im**2)

    plt.plot(np.linspace(0,len(x)),norma_f)
    plt.savefig(name)
    plt.close()
    return f_real,f_im
#Grafica las transformadas de fourier
fourier(x,y1,"sin(x).png")
fourier(x,y2,"0.1sin(x).png")
fourier(x,y3,"sin(10x).png")
#Graficas de las funciones
plt.plot(x,y1,label="sin(x)")
plt.plot(x,y2,c='red',label="0.1sin(x)")
plt.plot(x,y3,c='green',label="sin(10x)")
plt.legend()
plt.savefig('funciones.png')
plt.close()
#Manchas solares
data = np.loadtxt("monthrg.dat")
agnios = np.array(data[:,0])
manchas = np.array(data[:,3])
dias = np.array(data[:,2])
meses = np.array(data[:,1])
i = dias>0
#Angios y manchas por agnio
t = agnios[i]+ meses[i]/12
manchas_agnios = manchas[i]
#Agnios y manchas desde 1900
ii = t>1850
year = t[ii]
manch = manchas_agnios[ii]
plt.plot(year,manch)
plt.savefig("manchas2.png")
plt.close()
#transformadas de fourier para los datos anteriores
dt = 1.0 #Unidades: 1/meses
fourier = fft(manch)/len(year)
frecuencia = fftfreq(len(year),dt)
plt.plot(frecuencia,abs(fourier))
plt.savefig("frecuencia.png")
plt.close()
#Busca la frecuencia
iii = frecuencia > 0
indice = np.argmax(fourier[iii])
f=frecuencia[iii]
frec_max = f[indice]
t=1/frec_max
print "El periodo es", t, "meses"
