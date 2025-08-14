from time import sleep
valor1 = int(input('Primeiro valor: '))
valor2 = int(input('segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] SOMA
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    opcao = int(input('>>>>> Qual é a sua opção? '))

    if opcao == 1:
        soma = valor1 + valor2
        print('A soma entre {} + {} é {}' .format(valor1, valor2, soma))
    elif opcao == 2:
        multiplica = valor1 * valor2
        print('A multiplicação entre {} x {} é {}' .format(valor1, valor2, multiplica))
    elif opcao == 3:
        maior = valor1 if valor1 > valor2 else valor2
        print('O maior numero entre {} e {} é {}' .format(valor1, valor2, maior))
    elif opcao == 4:
        print('Informe os números novamente: ')
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção invalida tente novamente!')
    print('=-='*10)
    sleep(1)
print('Fim do programa!!')