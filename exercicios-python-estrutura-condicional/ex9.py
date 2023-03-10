'''Faça um Programa que pergunte em que turno você
estuda. Peça para digitar M-matutino ou V-Vespertino ou
N- Noturno. Imprima a mensagem "Bom Dia!", "Boa
Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o
caso.'''

turno=str(input('Qual turno você estuda ? : ')).casefold()
if turno == 'm' or turno =='matutino':
    print('Bom dia!')
elif turno=='v' or turno== 'vespertino':
    print('Boa tarde!')
elif turno=='n' or 'noturo':
    print('Boa noite!')
else:
    print('Valor invalido')