# Questão 10
# Escreva um algoritmo que leia uma quantidade indeterminada de números e
# conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100].
# A entrada de dados deve terminar quando for lido um número negativo
print('****************************************************')
print('Para encerrar as entradas digite um número negativo.')
print('****************************************************')

lista = {}
lista['[0-25]'] = 0
lista['[26-50]'] = 0
lista['[51-75]'] = 0
lista['[76-100]'] = 0

i = 0
while True:
    i += 1
    num_str = input('{} - Digite um número: '.format(str(i)))
    num = int(num_str)
    if(num >= 76 and num <= 100):
        lista['[76-100]'] += 1
    elif(num >= 51 and num <= 75):
        lista['[51-75]'] += 1
    elif(num >= 26 and num <= 50):
        lista['[26-50]'] += 1
    elif(num >= 0 and num <= 25):
        lista['[0-25]'] += 1
    elif(num < 0):
        break
        
print(lista)