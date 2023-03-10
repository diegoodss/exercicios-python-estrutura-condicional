'''Faça um Programa que leia três números e mostre o
maior deles.'''

numero=int(input('Digite um numero: '))
numero2=int(input('Digite um numero: '))
numero3=int(input('Digite um numero'))
if numero>numero2 and numero3:
    print(numero)
elif numero2>numero and numero3:
    print(numero2)
elif numero3 >numero and numero2:
    print(numero3)