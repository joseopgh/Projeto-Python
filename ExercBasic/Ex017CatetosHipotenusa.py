import math
oposto = float(input ('Digite o cateto oposto: '))
adjacente = float(input ('Digite o cateto adjacente: '))
hi = math.hypot(oposto, adjacente)
print ('A hipotenusa vai medir {:.2f}' .format(math.hypot(hi)))
