km = int(input('Qual é a distancia da sua viagem? '))
if km <= 200:
    print('Você esta prestes a começar uma viagem de {}km' .format(km))
    print('E o preço da sua passagem será de R${}' .format(km * 0,50))
else:
    print('Você esta prestes a começar uma viagem de {}km'.format(km))
    print('E o preço da sua passagem será de R${}' .format(km * 0,45))