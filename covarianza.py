
import numpy as np
import matplotlib.pyplot as plt

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

data_C = np.loadtxt("data_C.txt")
print(matriz_covarianza_nxn(data_C))
