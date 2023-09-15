import math
# Questão 2
# Faça um programa que leia três números inteiros positivos (x, y, z) e efetue o cálculo de
# uma das seguintes médias de acordo com o código digitado pelo usuário (1 a 4):

x = input('1 - Digite um número inteiro: ')
y = input('2 - Digite um número inteiro: ')
z = input('3 - Digite um número inteiro: ')

n = float(x) * float(y) * float(z)
geometrica = (n)**(1/3)

n = float(x) + (2 * float(y)) + (3 * float(z))
ponderada = n/6

n = float(x) + float(y) + float(z)
aritmetica = n/3

print('O resultado pela fórmula geométrica é {}'.format(str(geometrica)))
print('O resultado pela média ponderada é {}'.format(str(ponderada)))
print('O resultado pela média aritmétia é {}'.format(str(aritmetica)))