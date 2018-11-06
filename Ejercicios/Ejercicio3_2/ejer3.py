import numpy as np
pals = {}

m = 10
n = 3

f = open("pg5200.txt")
data = f.readlines()
#crear diccionario
for line in data:
    for pal in line.split():
        if(len(pal)==n):
            if(pal in pals):
                pals[pal] = pals[pal] + 1
            else:
                pals[pal] = 1

f.close()

cont = 1
#ordenar diccionario
for key, value in sorted(pals.iteritems(),reverse = True, key=lambda (k,v): (v,k)):
    print "%s: %s" % (key, value)
    if(cont == m):
        break
    cont +=1
