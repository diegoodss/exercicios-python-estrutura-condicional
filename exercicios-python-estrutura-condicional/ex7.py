'''Faça um programa que pergunte o preço de três
produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato'''

p1=int(input('Informe o preço do produto: '))
p2=int(input('Informe o preço do segundo produto: '))
p3=int(input('Informe o preço do terceiro produto: '))

if p1<p2 and p3:
    print('O primeiro produto é o mais barato!')
elif p2<p1 and p3:
    print('O segundo produto é o mais barato!')
elif p3<p2 and p1:
    print('O terceiro produto é o mais barato!')