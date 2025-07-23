for c in range(1, 7):
    num = int(input('Digite o {}º valor: '.format(c)))
if num % 2 == 0:
    print('A soma dos numeros pares é \033[0;31m{}\033[m' .format(num + num))