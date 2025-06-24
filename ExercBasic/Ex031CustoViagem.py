km = float(input('Qual é a distancia da sua viagem? '))
print('Você esta prestes a começar uma viagem de {:.0f}km' .format(km))
if km <= 200:
    print('E o preço da sua passagem será de R${:.2f}' .format(km * 0.50))
else:
    print('E o preço da sua passagem será de R${:.2f}' .format(km * 0.45))