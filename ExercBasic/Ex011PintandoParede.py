largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
tinta = area / 2
print('Sua parede tem a dimensão de {} x {} e sua area é de {:.2f}m².'.format(largura, altura, area))
print('Para pintar essa parede, você precisara de {}l de tinta.'.format(tinta))
