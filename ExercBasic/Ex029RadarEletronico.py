km = int(input('Qual é a velocidade atual do carro? '))
if km > 80:
    print('MULTADO! Você excedeu o limite de velocidade de 80km/h')
    print('Você deve pagar uma multa de R${:.2f}'.format((km - 80)*7))
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('Tenha um bom dia! Dirija com segurança!')