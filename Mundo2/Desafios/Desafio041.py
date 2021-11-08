from time import sleep
from datetime import date

print('-='*12)
print('Confederação Nacional de Natação')
print('-='*12)
sleep(1)

ano = int(input('Digite sua data de nascimento: '))
conta =date.today().year - ano 

if conta <= 9:
    print('De acordo com sua idade {}, sua categoria é MIRIM.'.format(conta))
elif conta <= 14:
    print('De acordo com sua idade {}, sua categoria é INFANTIL.'.format(conta))
elif conta <= 19:
    print('De acordo com sua idade {}, sua categoria é JÚNIOR.'.format(conta))
elif conta <= 25:
    print('De acordo com sua idade {}, sua categoria é SÊNIOR.'.format(conta))
elif conta > 25:
    print('De acordo com sua idade {}, sua categoria é MASTER.'.format(conta))
else:
    print('Digite uma data válida')

