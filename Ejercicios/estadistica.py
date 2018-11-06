import numpy as np
import matplotlib.pyplot as plt
data_A = np.loadtxt("data_A.txt")
data_B = np.loadtxt("data_B.txt")
xa = data_A[:,0]
ya = data_A[:,1]
xb = data_B[:,0]
yb = data_B[:,1]
plt.scatter(xa,ya,label="Datos A")
plt.savefig("dataA.png")
plt.legend()
plt.close()
plt.scatter(xb,yb,label="Datos B")
plt.savefig("dataB.png")
plt.legend()
plt.close()
#Funcion que genera la matriz de covarianza
def matriz_covarianza_2x2(data):
    x = data[:,0]
    y = data[:,1]
    n = len(x)
    meanx = np.mean(x)
    meany = np.mean(y)
    var_x = np.sum((x-meanx)*(x-meanx)/(n-1))
    var_y = np.sum((y-meany)*(y-meany)/(n-1))
    var_xy = np.sum((x-meanx)*(y-meany)/(n-1))
    M = np.array([[var_x,var_xy],[var_xy,var_y]])
    return M
#Matriz de covarianza de A
print ("Matriz A", matriz_covarianza_2x2(data_A))
#Matriz de covarianza de B
print ("Matriz B", matriz_covarianza_2x2(data_B))
#Descarga y grafica los datos para C
data_C = np.loadtxt("data_C.txt")
xc = data_C[:,0]
yc = data_C[:,1]
zc = data_C[:,2]
plt.scatter(xc,yc, c="red")
plt.scatter(yc,zc, c= "green")
plt.scatter(xc,zc)
plt.savefig("dataC.png")
plt.close()
def matriz_covarianza_3x3(data):
    x = data[:,0]
    y = data[:,1]
    z = data[:,2]
    n = len(x)
    meanx = np.mean(x)
    meany = np.mean(y)
    meanz = np.mean(z)
    var_x = np.sum((x-meanx)*(x-meanx)/(n-1))
    var_y = np.sum((y-meany)*(y-meany)/(n-1))
    var_xy = np.sum((x-meanx)*(y-meany)/(n-1))
    var_xz = np.sum((x-meanx)*(z-meanz)/(n-1))
    var_yz = np.sum((y-meany)*(z-meanz)/(n-1))
    var_z = np.sum((z-meanz)*(z-meanz)/(n-1))
    M = np.array([[var_x,var_xy,var_xz],[var_xy,var_y,var_yz],[var_xz,var_yz,var_z]])
    return M
print (matriz_covarianza_3x3(data_C))

#Autovectores y autovalores
def valores(M):
        valores, vectores = np.linalg.eig(M)
        return vectores
#Autovectores de A
vectoresA = valores(matriz_covarianza_2x2(data_A))

m = vectoresA[0,0]/vectoresA[0,1]
