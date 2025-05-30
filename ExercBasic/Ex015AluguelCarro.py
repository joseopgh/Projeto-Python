dias = int(input('Quantos dias você alugou o carro? : '))
km = int(input('Quantas km você rodou com o carro? : '))
cd = dias * 60
ck = km * 0.15
total = cd + ck
print('O total a pagar pelo aluguel é de R${:.2f}'.format(total))
