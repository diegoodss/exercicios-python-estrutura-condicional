'''Faça um Programa que leia três números e mostre o
maior e o menor deles.'''

numero=int(input('Digite um numero: '))
numero2=int(input('Digite um numero: '))
numero3=int(input('Digite um numero'))
maior=numero
menor=numero
if numero2>numero and numero2> numero3:
    maior=numero2
elif numero3>numero2 and numero3 > numero:
    maior=numero3
if numero2<numero and numero2< numero3:
    menor=numero2
elif numero3<numero2 and numero3> numero:
    menor=numero3
print('Maior: {} '.format(maior))
print('Menor : {}'.format(menor))