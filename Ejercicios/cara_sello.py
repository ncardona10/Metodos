import random
import numpy as np
import matplotlib.pyplot as plt

# (jc)Jugador que recibe 1 peso cada vez que sale cara
# (js)Jugador que recibe 1 peso cada vez que sale sello (Calcular cuanto dinero tiene)

js = 100
n=0
x=[]
y=[]
while (js>0 and js<200):
	datos = np.random.randint(0.0, 1.0)

	if (datos <= 0.49):
		js-=1
		
			
	else:
		js+=1
		
	n+=1
	x.append(n)
	y.append(js)	
			
print ("EL jugador obtiene", js)
plt.figure()
plt.plot(x,y)
plt.show()
    

    
    
    

