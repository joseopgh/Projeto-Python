salario = int(input('Qual éo salario do funcionario? R$'))
if salario < 1250:
    print('Quem ganhava R${} passa a ganhar R${:.2f} agora'.format(salario, salario + (salario * 0.15)))
else:
    print('Quem ganhava R${} passa a ganhar R${:.2f} agora'.format(salario, salario + (salario * 0.10)))
