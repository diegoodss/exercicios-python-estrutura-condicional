'''Faça um Programa que leia três números e
mostre-os em ordem decrescente.'''

a = float(input('Escreva um número: '))
b = float(input('Escreva um número: '))
c = float(input('Escreva um número: '))

if a >= b and a >= c and b >= c:
    print('A ordem decrescente é {}, {} e {}'.format(a,b,c))
elif a >= b and a >=c and c >= b:
    print('A ordem decrescente é {},{} e {}'.format(a,c,b))
elif b >= a and b >= c and a >= c:
    print('A ordem decrescente é {},{} e {}'.format(b,a,c))
elif b >= a and b >= c and c >= a:
    print('A ordem decrescente é {},{} e {}'.format(b,c,a))
elif c >= a and c >= b and a >=b:
    print('A ordem decrescente é {},{} {}'.format(c,a,b))
elif c >= a and c >= b and b >= a:
    print('A ordem decrescente é {},{} {} '.format(c,b,a))