num = int(input('''Digite seu numero para
calcular o seu fatorial: '''))
c = num
f = 1
print('calculando {}! = '.format(num,), end='')
while c > 0:
    print('{} '.format(c), end='')             #Fazer o fatorial
    print(' x ' if c > 1 else ' = ', end='')   #Para mostra o X na hora certa eo = no final
    f = f * c
    c = c - 1
print('{}'.format(f))                          #Fora do laço para que faça todo o calculo fora do laço