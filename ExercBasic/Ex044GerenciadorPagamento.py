print ('='*10,'\033[0;36mLojas Santos\033[m','='*10)
valor = float(input('Preço das  Compras: R$'))
print ('''FORMA DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mas no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    print('Sua compra vai custa R${:.2f}! Vai custar R${:.2f} no final. '.format(valor , valor - (valor*0.10)))
elif opcao == 2:
    print('Sua compra foi de R${:.2f}! Com o desconto vai ficar {:.2f} no final.' .format(valor , valor - (valor*0.05)))
elif opcao == 3:
    print('Sua compra foi de R${:.2f}! E no final ficou por 2x de R${:.2f} valor total de {:.2f}' .format(valor, valor / 2 , valor))
elif opcao ==  4:
    print('Sua compra foi de R${:.2f}!'.format(valor))
    vezes = int(input('Quantas vezes você que fazer? '))
    juros = valor - (valor * 0.40)
    print ('Voçê vai pagar {}x de R${:.2f}! Com o valor toral de R${:.2f}.' .format(vezes, juros / vezes,valor + juros))
else:
    print('Opção INVALIDA! Tente novamente.')
