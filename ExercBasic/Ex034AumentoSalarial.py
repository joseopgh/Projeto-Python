salario = int(input('Qual éo salario do funcionario? R$'))
if salario <= 1250:
    print('Quem ganhava R$\033[1;31m{}\033[m passa a ganhar R$\033[1;34m{:.2f}\033[m agora'.format(salario, salario + (salario * 0.15)))
else:
    print('Quem ganhava R$\033[1;31m{}\033[m passa a ganhar R$\033[1;34m{:.2f}\033[m agora'.format(salario, salario + (salario * 0.10)))
