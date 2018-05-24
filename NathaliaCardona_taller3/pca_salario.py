import numpy as np
import matplotlib.pyplot as plt



def matriz_covarianza(data):
    n = len(data[0,:])
    M = np.zeros((n,n))
    for i in range(n):
        for j in range(i,n):
            M[i][j] = covarianza(i,j,data,n)
            M[j][i] = covarianza(i,j,data,n)
    return M

def covarianza(i,j,data,n):
    x = np.array(data[:,i])
    y = np.array(data[:,j])
    return sum((x-np.mean(x))*(y-np.mean(y))/(len(x)-1))


def predi(column,ind, val):
    return (val/column[ind])*column[6]

def predice_salario(age,edu,black,hisp,marr,nodeg):
    data = np.loadtxt("cps1.csv",skiprows=1,delimiter=",",usecols=(2,3,4,5,6,7,8))
    data_normalizado = data.copy()
    for i in range(len(data[0,:])):
        media=np.mean(data[:,i])
        d_est=np.std(data[:,i])
        data_normalizado[:,i]=(data[:,i]-media)/d_est

    M = matriz_covarianza(data_normalizado)

    # percentvals = valores*100/sum(valores)
    ultFila = len(data[0,:])-1
    # print(M[ultFila])
    ind = np.where((M[ultFila,:][:-1]>=0.1) | (M[ultFila][:-1]<=-0.1 ))
    # print ind[0]
    valores, vectores = np.linalg.eig(matriz_covarianza(data_normalizado))

    params = [age,edu,black,hisp,marr,nodeg]
    numpar = len(ind[0])
    ans = 0
    de = np.std(data[:,-1])
    media = np.mean(data[:,-1])
    for i in range(numpar):
        ans += predi(vectores[:,ind[0][i]], ind[0][i], params[ind[0][i]])*de+media

    return ans/12
