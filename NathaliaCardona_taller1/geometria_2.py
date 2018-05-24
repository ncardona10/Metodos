import numpy as np
def radio_maximo(p):
    l=(p[0]**4+p[1]**4+p[2]**4)/2.0
    return l-max(p)
