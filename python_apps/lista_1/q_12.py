# Questão 12
# A conjectura de Collatz diz que, dado um inteiro positivo N, é sempre possível
# alcançar N=1 realizando as  seguintes operações repetidamente:
# N = N/2, se N é par
# N = 3N + 1, se N é ímpar
# Escreva um programa que imprima a sequência de Collatz para um dado numero inteiro N.
# Por exemplo, a sequência de Collatz para N=13 é:
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1


n_str = input('Digite um valor inteiro para N: ')
n = int(n_str)

while True:
    print('{} ->'.format(n), end = ' ')
    
    if((n % 2 == 0)):
        n = int(n / 2)
    elif((n % 2 != 0)):
        n = int(3 * n + 1)
    
    if(n == 1):
      print('{}'.format(int(n)), end = ' ')
      break
    