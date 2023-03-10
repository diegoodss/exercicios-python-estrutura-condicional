'''As Organizações Tabajara resolveram dar um aumento de salário aos seus
colaboradores e lhe contrataram para desenvolver o programa que calculará os
reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o
seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado,
informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.'''

salario=float(input('Informe seu salario : '))
conta=salario+(salario*20/100)
conta2=salario+(salario*15/100)
conta3=salario+(salario*10/100)
conta4=salario+(salario*5/100)

if salario<=280:
    salario=conta
    print('Salario atual: {} \nPorcentagem do aumento: 20% \nValor do reajuste : {} '.format(salario,conta))
elif salario <=700:
    salario=conta2
    print('Salario atual: {} \nPorcentagem do aumento: 15% \nValor do reajuste : {} '.format(salario,conta2))
elif salario <= 1500:
    salario=conta3
    print('Salario atual: {} \nPorcentagem do aumento: 10% \nValor do reajuste : {} '.format(salario,conta3))
elif salario > 1500:
    salario=conta4
    print('Salario atual: {} \nPorcentagem do aumento: 5% \nValor do reajuste : {} '.format(salario,conta4))