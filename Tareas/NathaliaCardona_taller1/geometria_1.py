import numpy as np
def interseccion(p1,p2,c,R):
    p1 = np.array(p1)
    p2 = np.array(p2)
    c = np.array(c)

    r0 = -p1 + c
    delta = p1-p2

    a=delta[0]**2 + delta[1]**2 + delta[2]**2
    b= -2*(delta[0]*r0[0] + delta[1]*r0[1] + delta[2]*r0[2])
    c=r0[0]**2 + r0[1]**2 + r0[2]**2-R**2
    l1=[]
    l2=[]
    d=b**2-4*a*c
    if (d==0):
        lamb=-b/(2.0*a)
        l1=l2=(lamb*delta+p1).tolist()
        return l1, l2
    elif(d>0):
        lamb1=(-b-np.sqrt(d))/(2.0*a)
        lamb2=(-b+np.sqrt(d))/(2.0*a)
        l1=(lamb1*delta+p1).tolist()
        l2=(lamb2*delta+p1).tolist()
        return l1, l2
    else:
        return "False"
