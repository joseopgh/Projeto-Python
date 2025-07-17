import time
import random
print ('''Suas opção:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogada = int(input('Qual a sua jogada? '))
print ('jo')
time.sleep(1)
print ('KEM')
time.sleep(1)
print ('POW')
time.sleep(1)
print ('-='*15)
lista = [0, 1 , 2]

escolhido = random.choice(lista)
if jogada == 1 and escolhido == 0 or jogada == 2 and escolhido == 1:
    print ('COMPUTADOR jogou {}'.format(escolhido))
    print ('JOGADOR jogou {}'.format(jogada))
elif jogada == 0 and escolhido == 1 or jogada == 1 and escolhido == 2:
    print ('COMPUTADOR jogou {}'.format(escolhido))
    print ('JOGADOR jogou {}'.format(jogada))