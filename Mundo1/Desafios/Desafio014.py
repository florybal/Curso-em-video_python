'''
Ecreva um programa que converta uma temperatura digitada em °C
e converta para °F.
'''
'incrementar'

num = float(input("Informe a temperatura de hoje em °C: "))
print('A temperatura de hoje é {}°C e em  fahrenheit é {:.2}°F'.format(num, (1.8*num +32)))
