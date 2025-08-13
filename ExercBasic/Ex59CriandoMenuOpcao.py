
valor1 = int(input('Primeiro valor: '))
valor2 = int(input('segundo valor: '))
print('''    [ 1 ] SOMA
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
opcao = int(input('>>>>> Qual é a sua opção? '))

    if opcao == 1:
        soma = valor1 + valor2
        print('A soma entre {} + {} é {}' .format(valor1, valor2, soma))
    if opcao == 2:
        multiplica = valor1 * valor2
        print('A multiplicação entre {} x {} é {}' .format(valor1, valor2, multiplica))
    if opcao == 3:
        maior = valor1 if valor1 > valor2 else valor2
        print('O maior numero entre {} e {} é {}' .format(valor1, valor2, maior))
    if opcao == 4:
        print('Escolha novos numeros')
    if opcao == 5:
        print('Programa encerrado!')
    if opcao == 0 or opcao >= 6  :
        print('Opção invalida tente novamente!')
