import numpy as np
import matplotlib.pyplot as plt

def cubica(x,a,b,c,d):
    return a*x**3 + b*x**2 + c*x + d

def determinarIndice(x_in,x_inter):
    for i in range(len(x_in)-1):
        if(x_in[i]<=x_inter and x_inter<=x_in[i+1]):
            return i


def mi_spline(x_in,y_in,x_inter):
    nf = len(x_in)-1
    ncoefs = nf*4
    matr = np.zeros([ncoefs,ncoefs])
    ys = np.zeros(ncoefs)
    for i in range(nf):
        matr[2*i][4*i] = x_in[i]**3
        matr[2*i][4*i+1] = x_in[i]**2
        matr[2*i][4*i+2] = x_in[i]**1
        matr[2*i][4*i+3] = 1

        matr[2*i+1][4*i]   = x_in[i+1]**3
        matr[2*i+1][4*i+1] = x_in[i+1]**2
        matr[2*i+1][4*i+2] = x_in[i+1]**1
        matr[2*i+1][4*i+3] = 1

    for i in range(nf-1):
        matr[2*i+2*nf][4*i]   = 3*(x_in[i+1])**2
        matr[2*i+2*nf][4*i+1] = (2*x_in[i+1])
        matr[2*i+2*nf][4*i+2] = 1

        matr[2*i+2*nf][4*i+4] = -3*(x_in[i+1])**2
        matr[2*i+2*nf][4*i+5] = -(2*x_in[i+1])
        matr[2*i+2*nf][4*i+6] = -1

        matr[2*i+1+2*nf][4*i]   = 6*x_in[i+1]
        matr[2*i+1+2*nf][4*i+1] = 2


        matr[2*i+1+2*nf][4*i+4] = -6*x_in[i+1]
        matr[2*i+1+2*nf][4*i+5] = -2

    matr[-2][0] = 6*x_in[0]
    matr[-2][1] = 2

    matr[-1][-4] = 6*x_in[1]
    matr[-1][-3] = 2

    ys[0] = y_in[0]

    for i in range(nf-1):
        ys[2*i+1] = y_in[i+1]
        ys[2*i+2] = y_in[i+1]

    ys[2*nf-1] = y_in[-1]

    sol = np.linalg.solve(matr,np.transpose(ys))

    if(isinstance(x_inter,float) or isinstance(x_inter,int)):
        ind = determinarIndice(x_in,x_inter)
        return cubica(x_inter,sol[4*ind],sol[4*ind+1],sol[4*ind+2],sol[4*ind+3])

    if(isinstance(x_inter,list) or  type(x_inter).__module__ == np.__name__):
        ans = []
        
        for i in x_inter:
            ind = determinarIndice(x_in,i)
            ans.append(cubica(i,sol[4*ind],sol[4*ind+1],sol[4*ind+2],sol[4*ind+3]))

        if(isinstance(x_inter,list)):
            return ans
        else:
            return np.array(ans)
