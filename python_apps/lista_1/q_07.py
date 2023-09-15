# Questão 7
# Escreva um programa que receba como entrada o valor (inteiro) do saque requisitado pelo
# cliente de um banco e retorne quantas notas de cada valor serão necessárias para atender
# ao saque com a menor quantidade de notas. Assuma que estão disponíveis notas de R$200,
# R$50, R$10, R$2 e R$1.

valor_str = input('Digite o valor desejado (inteiro): ')

valor = int(valor_str)
quantidade = 0

  
quantidade += int(valor/200)
valor = valor % 200

if(valor > 0):
    quantidade += int(valor/50)
    valor = valor % 50

if(valor > 0):
    quantidade += int(valor/10)
    valor = valor % 10
    
if(valor > 0):
    quantidade += int(valor/2)
    valor = valor % 2

if(valor > 0):
    quantidade += int(valor/1)
    valor = valor % 1
    
print('Quantidade de notas é {}'.format(str(quantidade)))