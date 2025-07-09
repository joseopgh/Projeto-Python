num = int(input('Digite um número inteiro: '))
print('Escolha uma das base para conversão:')
print('[ 1 ] converter para Binario')
print('[ 2 ] converter para Octal')
print('[ 3 ] converter para Hexadecimal')
opcao = int(input('Sua opção: '))

binario = bin(num)
octal = oct(num)
hexadecimal = hex(num)

if opcao == 1:
    print('{} convertido para Binario é igual a {}' .format(num, binario [2:]))
elif opcao == 2:
    print('{} convertido para Octal é igual a {}' .format(num, octal [2:]))
elif opcao == 3:
    print('{} convertido para Hexadecimal é igual a {}' .format(num, hexadecimal [2:]))
else:
    print('A Opção digitada esta incorreta, Tente novamente..')
