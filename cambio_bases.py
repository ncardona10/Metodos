import numpy as np
import matplotlib.pyplot as plt
data_B = np.loadtxt("data_B.txt")
plt.scatter(data_B[:,0],data_B[:,1],label="Datos B")
plt.savefig("dataB.png")
plt.legend()
plt.close()
def matriz_covarianza_nxn(data):
    n = len(data[0,:])
    M = np.zeros((n,n))
    for i in range(n):
        for j in range(i,n):
            # print(i,j,covarianza(i,j,data,n))
            M[i][j] = covarianza(i,j,data,n)
            M[j][i] = covarianza(i,j,data,n)
    return M
def covarianza(i,j,data,n):
    x = np.array(data[:,i])
    y = np.array(data[:,j])
    return sum((x-np.mean(x))*(y-np.mean(y))/(len(x)-1))
def eigen(M):
        valores, vectores = np.linalg.eig(M)
        return vectores
#Datos B
matriz_covarianzaB = matriz_covarianza_nxn(data_B)
vectores = eigen(matriz_covarianzaB)
matriz_cambio_base = np.array([[vectores[0,0],vectores[1,0]],[vectores[0,1],vectores[1,1]]])
nuevaBase = np.zeros([len(data_B),2])
for i in range(len(data_B)):
    temp = np.transpose(data_B[i])
    temp_neu = np.dot(matriz_cambio_base,temp)
    nuevaBase[i,:]=np.transpose(temp_neu)
plt.scatter(nuevaBase[:,0],nuevaBase[:,1])
plt.savefig("cambioBase.png")
#Datos C1
data_C = np.loadtxt("data_C.txt")
data_C1 = data_C[:,0:2]
matriz_covarianzaC1 = matriz_covarianza_nxn(data_C1)
vectoresC1 = eigen(matriz_covarianzaC1)
matriz_cambio_baseC1 = np.array([[vectoresC1[0,0],vectoresC1[1,0]],[vectoresC1[0,1],vectoresC1[1,1]]])
nuevaBaseC = np.zeros([len(data_C),2])
for i in range(len(data_C)):
    temp = np.transpose(data_C1[i])
    temp_neu = np.dot(matriz_cambio_baseC1,temp)
    nuevaBaseC[i,:]=np.transpose(temp_neu)
plt.scatter(nuevaBaseC[:,0],nuevaBaseC[:,1])
plt.savefig("cambioBaseC1.png")
#Datos C2
data_C2 = data_C[:,[0,-1]]
matriz_covarianzaC2 = matriz_covarianza_nxn(data_C2)
vectoresC2 = eigen(matriz_covarianzaC2)
matriz_cambio_baseC2 = np.array([[vectoresC2[0,0],vectoresC2[1,0]],[vectoresC2[0,1],vectoresC2[1,1]]])
nuevaBaseC2 = np.zeros([len(data_C),2])
for i in range(len(data_C)):
    temp = np.transpose(data_C2[i])
    temp_neu = np.dot(matriz_cambio_baseC2,temp)
    nuevaBaseC2[i,:]=np.transpose(temp_neu)
plt.scatter(nuevaBaseC2[:,0],nuevaBaseC2[:,1])
plt.savefig("cambioBaseC2.png")
#Datos C3
data_C3 = data_C[:,[1,-1]]
matriz_covarianzaC3 = matriz_covarianza_nxn(data_C3)
vectoresC3 = eigen(matriz_covarianzaC3)
matriz_cambio_baseC3 = np.array([[vectoresC3[0,0],vectoresC3[1,0]],[vectoresC3[0,1],vectoresC3[1,1]]])
nuevaBaseC3 = np.zeros([len(data_C),2])
for i in range(len(data_C)):
    temp = np.transpose(data_C3[i])
    temp_neu = np.dot(matriz_cambio_baseC3,temp)
    nuevaBaseC3[i,:]=np.transpose(temp_neu)
plt.scatter(nuevaBaseC2[:,0],nuevaBaseC2[:,1])
plt.savefig("cambioBaseC3.png")
