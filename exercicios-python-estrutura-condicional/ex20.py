'''Faça um Programa que peça um número
inteiro e determine se ele é par ou impar. Dica:
utilize o operador módulo (resto da divisão).'''

numero=int(input('Digite um numero: '))
if (numero%2)==0:
    print('O numero {} é par :'.format(numero))
else:
    print('O numero {} é impar'.format(numero))