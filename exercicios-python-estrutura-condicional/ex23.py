'''Faça um programa que faça 5 perguntas para uma pessoa sobre
um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?“
O programa deve no final emitir uma classificação sobre a
participação da pessoa no crime. Se a pessoa responder
positivamente a 2 questões ela deve ser classificada como
"Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".'''

count=0
pergunta=str(input('Algumas perguntas \ntelefonou para vitima ? : ')).casefold()
if pergunta == 'sim' or pergunta == 's':
    count = count + 1
pergunta=input('Esteve no local do crime ? :').casefold()
if pergunta == 'sim' or pergunta == 's':
    count = count + 1
pergunta=input('Mora perto da vitima ? : ').casefold()
if pergunta == 'sim' or pergunta == 's':
    count = count + 1
pergunta=input('Devia para vitima ?:  ').casefold()
if pergunta == 'sim' or pergunta == 's':
    count = count + 1
pergunta=input('Ja trabalhou para vitima ? : ').casefold()
if pergunta == 'sim' or pergunta == 's':
    count = count + 1
if count == 2:
    print('Suspeita')
if count == 3 or count == 4:
    print('Cúmplice')
if count == 5:
    print('Assasino')
else:
    print('Inocente')