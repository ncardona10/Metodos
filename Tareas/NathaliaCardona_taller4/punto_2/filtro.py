import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import cmath as cmath
import sys

N = 0
M = 0


def centrarFourier(matriz):
    matr = np.array(matriz)
    rear = []
    for i in range(N):
        rear.append(int((i+N/2+1)%N))
    # print(rear)
    matr = matr[:,rear]

    rear = []
    for i in range(M):
        rear.append(int((i+M/2+1)%M))
    # print(matr)
    matr = matr[rear,:]
    return matr.tolist()

def desCentrarFourier(matriz):
    matr = np.array(matriz)
    rear = []
    for i in range(N):
        rear.append(int((i+N/2)%N))
        # print(str(i)+" " + str(int((i+N/2)%N)))
    # print(rear)
    matr = matr[:,rear]

    rear = []
    for i in range(M):
        rear.append(int((i+M/2)%M))
    # print(matr)
    matr = matr[rear,:]
    return matr.tolist()

                

    
def distDelOrigen(x, y):
    # print(int(N/2))
    return ((x-int(N/2))**2+(y-int(M/2))**2)**0.5


def filtroBajo(x, y):
    global N, M
    cutoff = int(min(N,M)/4)
    w = 1
    r = distDelOrigen(x, y)
    # print(r)
    # print(int(N/2))
    if(r < cutoff - w):
        return 1
    elif(r > cutoff+w):
        # print("enra")
        return 0
    else:
        return 0.5*(1-np.sin(np.pi*(r-cutoff))/(2.0*w))


def filtroAlto(x, y):
    global N, M
    cutoff = int(min(N,M)/4)
    w = 1
    r = distDelOrigen(x, y)
    if(r < cutoff - w):
        # print("entra")
        return 0
    elif(r > cutoff+w):
        return 1
    else:
        return 0.5*(1-np.sin(np.pi*(-r-cutoff))/(2.0*w))


def filtrarBajo(matriz):

    for i in range(N):
        for j in range(M):
            matriz[i][j] *= filtroBajo(i, j)
    

def filtrarAlto(matriz):
    for i in range(N):
        for j in range(M):
            matriz[i][j] *= filtroAlto(i, j)


def initMatrix(n, m):
    matriz = []
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(0.0)
        matriz.append(temp)
    return matriz


def DFT2D(imagen):
    global M, N

    N = imagen.size[0]
    M = imagen.size[1]
    pixeles = imagen.load()

    ans = [initMatrix(N, M), initMatrix(N, M), initMatrix(N, M)]

    for u in range(N):
        for v in range(M):

            sumaRojo = 0.0
            sumaVerde = 0.0
            sumaAzul = 0.0
            for x in range(M):
                for y in range(N):
                    sumaRojo += pixeles[x, y][0] * np.exp(
                        np.pi*2 * (- 1j) * (float(v * x) / M + float(u * y) / N))
                    sumaVerde += pixeles[x, y][1] * np.exp(
                        np.pi*2 * (- 1j) * (float(v * x) / M + float(u * y) / N))
                    sumaAzul += pixeles[x, y][2] * np.exp(
                        np.pi*2 * (- 1j) * (float(v * x) / M + float(u * y) / N))

            ans[0][u][v] = sumaRojo / (M*N)
            ans[1][u][v] = sumaVerde / (M*N)
            ans[2][u][v] = sumaAzul / (M*N)
    return ans


def invDFT2D(dft2d):
    global M, N
    imagen = Image.new("RGB", (M, N))
    pixeles = imagen.load()

    for x in range(N):

        for y in range(M):

            sumaRojo = 0.0
            sumaVerde = 0.0
            sumaAzul = 0.0

            for k in range(M):
                for l in range(N):
                    sumaRojo += dft2d[0][l][k] * \
                        np.exp(np.pi * 2 * 1j *
                               (float(k * y) / M + float(l * x) / N))
                    sumaVerde += dft2d[1][l][k] * np.exp(
                        np.pi * 2 * 1j * (float(k * y) / M + float(l * x) / N))
                    sumaAzul += dft2d[2][l][k] * \
                        np.exp(np.pi * 2 * 1j *
                               (float(k * y) / M + float(l * x) / N))

            rojof = int(sumaRojo.real + 0.5)
            verdef = int(sumaVerde.real + 0.5)
            azulf = int(sumaAzul.real + 0.5)

            pixeles[x, y] = (rojof, verdef, azulf)
    return imagen


if(len(sys.argv)!=3):
    print("Formato invalido. Uso:")
    print()
    print("     python3 filtro.py <nombre imagen.png> <tipo de filtro(alto, bajo)>")
    print()
    sys.exit()

if(not((sys.argv[2] == "alto" )| (sys.argv[2] == "bajo") )):
    print("Tipo de filtro no valido")
    print()
    print("Favor usar bajo o alto")
    print()
    sys.exit()




imagen = Image.open(sys.argv[1])

temp = DFT2D(imagen)

temp[0] = centrarFourier(temp[0])
temp[1] = centrarFourier(temp[1])
temp[2] = centrarFourier(temp[2])


if(sys.argv[2] == "alto"):

    filtrarAlto(temp[0])
    filtrarAlto(temp[1])
    filtrarAlto(temp[2])
else:
    filtrarBajo(temp[0])
    filtrarBajo(temp[1])
    filtrarBajo(temp[2])

temp[0] = desCentrarFourier(temp[0])
temp[1] = desCentrarFourier(temp[1])
temp[2] = desCentrarFourier(temp[2])


image = invDFT2D(temp)
image.save("output.png", "PNG")




#mostrar transformada fourier para rojo 
# for i in range(N):
#     for j in range(M):
#         temp[0][i][j] = (temp[0][i][j].real**2 + temp[0][i][j].imag**2)**0.5
#         temp[1][i][j] = (temp[1][i][j].real**2 + temp[1][i][j].imag**2)**0.5
#         temp[2][i][j] = (temp[2][i][j].real**2 + temp[2][i][j].imag**2)**0.5

# plt.imshow(temp[0])
# plt.show()
# plt.close()