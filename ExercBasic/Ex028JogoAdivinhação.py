from random import randint
computador = randint(0,5)            # Faz o computador "Pensar"
print('-=-' *20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' *20)
jogador = int(input('Em que número pensei? ')) #Jogador tenta adivinhar
if jogador == computador:
    print('PARABENS! você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}.' .format(computador, jogador))
