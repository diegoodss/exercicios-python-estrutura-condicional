'''Faça um Programa que leia 2 números e em
seguida pergunte ao usuário qual operação ele
deseja realizar. O resultado da operação deve ser
acompanhado de uma frase que diga se o
número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.'''

num1=float(input('Digite um numero: '))
num2=float(input('Digite outro numero: '))
operaçao=int(input('Digite o numero da opeção que deseja fazer \n1-Par ou ímpar \n2-Positivo ou negativo\n3-Inteiro ou decimal\n '))

if operaçao==1:
    if (num1 % 2) == 0:
        print('O numero1 {} é par: '.format(num1))
    else:
        print('O numero1 {} é impar: '.format(num1))
    if (num2 % 2) == 0:
        print('O numero2 {} é par : '.format(num1))
    else:
        print('O numero 2{} é impar: '.format(num1))
if operaçao ==2:
    if num1>0:
        print('O Primeiro numero {} é positivo'.format(num1))
    elif num1<0:
        print('O Primeiro numero {} é negativo'.format(num1))
    if num2>0:
        print('O Segundo numero {} é positivo'.format(num2))
    elif num2<0:
        print('O Segundo {} é negativo'.format(num2))
if operaçao == 3:
    if num1 % 1 == 0:
        print('O primeiro numero {} é Inteiro'.format(num1))
    else:
        print('O primerio numero {} é Decimal'.format(num1))
    if num2 % 1 == 0:
        print('O Segundo numero {} é Inteiro'.format(num2))
    else:
        print('O Segundo numero é Decimal'.format(num2))