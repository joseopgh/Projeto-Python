import time
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint (0, 2)
print('O computador escolhei {}'.format(itens[computador]))     ##Estrutudo do codigo
print ('''Suas opção:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogada = int(input('Qual a sua jogada? '))
print ('jo')
time.sleep(1)
print ('KEM')                                                       ##Time sleep de contador do gamer
time.sleep(1)
print ('POW')
time.sleep(1)

print ('-='*15)
print('O computador escolhei {}'.format(itens[computador]))           ##Emprimir na tela o resultado do jogo
print('O jogador jogou {}'.format(itens[jogada]))
print ('-='*15)

if computador == 0:
    if jogada == 0:
        print('EMPATE')
    elif jogada == 1:
        print('JOGADOR VENCE')
    elif jogada == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif computador == 1:
    if jogada == 0:
        print('COMPUTADOR VENCE')
    elif jogada == 1:
        print('EMPATE')
    elif jogada == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif computador == 2:
    if jogada == 0:
        print('JOGADOR VENCE')
    elif jogada == 1:
        print('COMPUTADOR VENCE')
    elif jogada == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')