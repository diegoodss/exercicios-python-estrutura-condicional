'''Faça um Programa para leitura de três notas
parciais de um aluno. O programa deve calcular a média
alcançada por aluno e presentar:
A mensagem "Aprovado", se a média for maior ou
igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor
do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a
média for igual a 10.'''

valor=float(input('Qual o valor do saque de 10 a 600 ? : '))
cem=int(valor / 100)
valor= valor - (cem * 100)

cinquenta=int(valor / 50)
valor=valor-(cinquenta * 50)

dez=int(valor / 10)
valor=valor - (dez * 10)

cinco=int(valor / 5)
valor=valor - (cinco * 5)

um=int(valor)
print(
'\nNotas R$100,00 = {}'
'\nNotas R$ 50,00 = {}'
'\nNotas R$ 10,00 = {}'
'\nNotas R$  5,00 = {}'
'\nNotas R$  1,00 = {:.0f}'.format(cem,cinquenta,dez,cinco,um))