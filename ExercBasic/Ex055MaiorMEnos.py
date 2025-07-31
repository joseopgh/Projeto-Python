maiorpeso = 0
menorpeso = 0
for pessoa in range(1,6):
    peso = float(input('Peso da {}ª pessoa: '.format(pessoa)))
    if pessoa == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso
print('O maior peso lido foi de {}Kg'.format(maiorpeso))
print('O menos peso lido foi de {}kg'.format(menorpeso))
