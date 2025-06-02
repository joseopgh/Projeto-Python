import math
num = float(input('Digite o ângulo que você deseja: '))
grau = math.radians(num)
seno = math.sin(grau)
cosseno = math.cos(grau)
tangente = math.tan(grau)
print ('O Angulo de {} tem o Seno de {:.2f}' .format(num, seno))
print ('O Angulo de {} tem o Cosseno de {:.2f}' .format(num, cosseno))
print ('O Angolo de {} tem o Tangente de {:.2f}' .format(num, tangente))
