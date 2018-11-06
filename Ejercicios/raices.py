import numpy as np
import matplotlib.pyplot as plt
g=9.8
def deriva(fun,v,h,d,theta):
    h=0.01
    delta=theta+h
    df=(fun(v,h,d,delta)-fun(v,h,d,theta))/h
    return df

def fun(v,h,d,theta):
    rta= d*np.tan(theta) - (g*d**2)/(2*v**2*np.cos(theta)**2) -h
    return rta
theta= np.linspace(0.1, np.pi/3, 10)
f_theta=[]
def grafica(fun,v,h,d):
    for i in theta:
        temp= fun(v,h,d,i)
        f_theta.append(temp)

def apunta(fun,deriva,v,h,d):
    cont=0.0
    epsilon=0.000001
    theta=1.0
    fx=abs(fun(v,h,d,theta))
    while(cont<1000 and epsilon<fx):
        print("fx: ", fx)
        delta_theta=-(fun(v,h,d,theta)/deriva(fun,v,h,d,theta))
        theta+=delta_theta
        fx=abs(fun(v,h,d,theta))
        cont+=1

    if(epsilon < fx):
        return "No existe"
    return theta

grafica(fun, 100.0, 4.0, 6.0)
plt.plot(theta, f_theta)
plt.savefig("funcion.png")
respuesta = apunta(fun,deriva,100.0, 4.0, 6.0)
print respuesta
