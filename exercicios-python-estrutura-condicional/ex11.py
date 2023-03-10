'''Faça um programa para o cálculo de uma folha de
pagamento, sabendo que os descontos são do Imposto de
Renda, que depende do salário bruto (conforme tabela abaixo) e
3% para o Sindicato e que o FGTS corresponde a 11% do
Salário Bruto, mas não é descontado (é a empresa que
deposita). O Salário Líquido corresponde ao Salário Bruto
menos os descontos. O programa deverá pedir ao usuário o
valor da sua hora e a quantidade de horas trabalhadas no
mês.Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20%
Imprima na tela as informações, dispostas conforme o exemplo
abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é
220.'''

valorhora=float(input('Qual o seu salalrio por hora: '))
horas_trabalhadas=float(input('Quantas horas voce trabalhou esse mes: '))
salariobruto=valorhora*horas_trabalhadas

salariobruto = valorhora * horas_trabalhadas
if salariobruto <= 900:
    desconto_ir = 0.0
elif salariobruto <= 1500:
    desconto_ir = 5
elif salariobruto <= 2500:
    desconto_ir = 10
else:
    desconto_ir = 20

ir= salariobruto*(desconto_ir/100)
inss= salariobruto*(desconto_ir/100)
fgts= salariobruto*(11/100)
totaldescontos=ir+inss
salarioliquido=salariobruto-totaldescontos

print('\nSalario bruto   :R$ {:.2f} '
      '\n(-) IR (5%)     :R$ {:.2f} '
      '\n(-) INSS (10%)  :R$ {:.2f} '
      '\n(-) FGTS (11%)  :R$ {:.2f}'
      '\nTotal de descontos : R$ {:.2f}'
      '\nSaláraio Liquido : R$ {:.2f}'.format(salariobruto,ir,inss,fgts,totaldescontos,salarioliquido))