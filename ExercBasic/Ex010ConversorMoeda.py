moeda = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = moeda/5.65
euro = moeda/6.42
print('Com R${:.2f} você pode comprar US${:.2f} '.format(moeda, dolar))
print('Com R${:.2f} Você pode comprar E${:.2f} '.format(moeda, euro))
