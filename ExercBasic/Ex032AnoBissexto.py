ano = int(input('Qua ano quer analizar? '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:    #Calculo para saber se o ano é bisxesto ou não
    print('O ano {} é BISSEXTO' .format(ano))
else:
    print('O ano {} NÃO é BISSEXTO' .format(ano))
