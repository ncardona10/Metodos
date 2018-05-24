import numpy as np
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join
import pandas as pd
import sys

files = [f for f in listdir("./s3_files/berlin/") if isfile(join("./s3_files/berlin/", f))]
files = sorted(files)

def mensaje(data,fecha):
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



    for i in range(len(data[0,:])):
        media=np.mean(data[:,i])
        d_est=np.std(data[:,i])
        if d_est!=0:
            data[:,i]=(data[:,i]-media)/d_est


    datos = ["overal_satisfaction","acommodates","bedrooms","price","minstay"]
    matriz = matriz_covarianza(data)
    maximo= -sys.float_info.max
    indices_max=np.zeros(2)
    minimo= sys.float_info.max
    indices_min=np.zeros(2)
    for i in range(len(data[0,:])-1):
        for j in range(i+1,len(data[0,:])):

            if (maximo<matriz[i][j]):
                maximo=matriz[i][j]
                indices_max[0]=i
                indices_max[1]=j

            if (minimo>matriz[i][j]):
                minimo=matriz[i][j]
                indices_min[0]=i
                indices_min[1]=j

    correlacion1= datos[int(indices_max[0])]
    correlacion2= datos[int(indices_max[1])]
    anti_correlacion1= datos[int(indices_min[0])]
    anti_correlacion2= datos[int(indices_min[1])]
    f = open ("variables_berlin.txt", "a")
    aImprimir = fecha + " " + correlacion1 + " " + correlacion2 + " " + anti_correlacion1 + " " + anti_correlacion2 + "\n"
    f.write(aImprimir)
    f.close()

def procesar(nomArch):

    data = pd.read_csv("s3_files/berlin/"+nomArch)
    data =  data[['overall_satisfaction', 'accommodates', 'bedrooms','price', 'minstay']]
    data = np.array(data.values)

    fecha = nomArch.split("_")[-1].split(".")[0]

    mensaje(data,fecha)

for f in files:
    procesar(f)
