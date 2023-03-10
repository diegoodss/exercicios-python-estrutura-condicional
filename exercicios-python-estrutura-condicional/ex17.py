'''Faça um Programa que peça uma data no
formato dd/mm/aaaa e determine se a mesma é
uma data válida.'''

dia=int(input('Qeu dia você nasceu ? :'))
mes=int(input('Que mes voce nasceu ? :'))
ano=int(input('Que ano voce nasceu? :'))

if dia>31:
    print('data invalida!!'.format(dia,mes,ano))
elif mes > 12:
    print('Data invalida!!'.format(dia,mes,ano))
elif dia <31:
    print('{}/{}/{}'.format(dia,mes,ano))
elif mes <12:
    print('{}/{}/{}'.format(dia,mes,ano))