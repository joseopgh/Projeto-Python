from random import randint
comput = randint(1, 9)
tentativa = 0
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegui adivinhar qual foi?''')
valor = int(input('Qual é seu palpite? '))

if valor > 0 and valor < 10:
    while valor != comput:
        if comput > valor:
            valor = int(input('MAIS... Tente novamente: '))
        if comput < valor:
            valor = int(input('MENOS... Tente novamente: '))
        if valor > comput and valor < comput:
            tentativa += 1
        if valor == comput:
            print('VOÇÊ ACERTOU MISERAVEL! Na {} Tentativa.'.format(tentativa))
else:
    print('Valor incorreto! Voçê não sabe brincar!!')
