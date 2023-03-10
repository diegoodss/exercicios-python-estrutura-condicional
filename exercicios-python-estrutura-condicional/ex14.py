'''Faça um Programa que peça os 3 lados de um triângulo. O
programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é:
equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de
quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;'''

primeirlado=float(input('Informe o primeiro lado: '))
segundolado=float(input('Inorme o segundo lado: '))
terceirolado=float(input('Informe o terceiro lado : '))

if (primeirlado+segundolado<terceirolado) or (primeirlado+terceirolado<segundolado) or (segundolado+terceirolado<primeirlado):
    print('Nao é um triangulo')
elif (primeirlado==segundolado) and (primeirlado==terceirolado):
    print('Equilatero')
elif (primeirlado==segundolado) or (primeirlado== terceirolado) or (segundolado == terceirolado):
    print('Isósceles')
else:
    print('Escaleno')