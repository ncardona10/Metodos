import numpy as np

def trap(f,a,b,N):
  x= np.linspace(a,b,N)
  y= f(x)
  h= x[1]-x[0]
  integral = np.sum(y)*h
  return integral

print ("Integral por trapecios",trap(np.exp,0.0,1.0,100000))
print ("Integral analitica",np.exp(1)-np.exp(0))
