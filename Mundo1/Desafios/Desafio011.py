alt = float(input('Digite a altura da sua parede'))
lar = float(input('Digite a largura da sua parede'))
area = alt * lar

print('Sua parede tem a dimensão de {}x{} e sua área é: {}m².\n'
      'Para pintar essa parede você precisará de: {}L de tinta'.format(alt, lar, area, (area/2)))
