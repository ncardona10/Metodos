import numpy as np
import matplotlib.pyplot as plt

def integral (f,a,b,N,p=""):
    sum=0.0
    if(p=="trap"):
        x= np.linspace(a,b,N)
        y= f(x)
        for i in range(N-1):
            sum+= 0.5 * (y[i]+y[i+1]) * (x[i+1] - x[i])
    else:
        x= np.linspace(a,b,N)
        y= f(x)
        for i in range(1,N-1,2):
            sum+= (1.0/3.0) * (x[i+1] - x[i]) * (y[i-1] + 4*y[i] + y[i+1])
    return(sum)

print integral(np.exp, 0.0, 1.0, 11, "trap")
print integral(np.exp, 0.0, 1.0, 11)

logN=[]
logE=[]
logN2=[]
logE2=[]
for i in range(1,10000, 10):
    real = np.exp(1)-np.exp(0)
    trap = integral(np.exp, 0.0, 1.0,2*i+1, "trap")
    simps = integral(np.exp, 0.0, 1.0,2*i+1)
    e = (trap-real)/real
    e2 = (simps-real)/real
    logE.append(-abs(np.log10(e)))
    logN.append(np.log10(2*i+1))
    logE2.append(-abs(np.log10(e2)))
    logN2.append(np.log10(2*i+1))
imagen = plt.plot(logN,logE, label="Trapecio")
imagen2 =  plt.plot(logN2,logE2, label="Simpson")
plt.legend(loc=3)
plt.xlabel('$\log_{10}$ N_points')
plt.ylabel('$\log_{10}$ Error')
plt.savefig("Grafica_Error.png")
