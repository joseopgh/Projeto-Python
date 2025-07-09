valor = float(input('Valor da casa: R$'))
salario = float(input('Salario do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
mensal = (valor / anos) / 12
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}' .format(valor, anos, mensal))
if mensal < salario * 0.3:
    print('\033[0;32mEmprestimo aprovado!\033[m')
else:
    print('\033[0;31mEmprestimo reprovado!\033[m')
