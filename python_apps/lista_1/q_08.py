# Questão 8
# Escreva um programa que leia dois valores inteiros X e Y. A seguir,
# mostre uma sequência de 1 até Y, passando  para a proxima linha a cada X números.

x_str = input('Digite um valor inteiro para X: ')
y_str = input('Digite um valor inteiro para Y: ')

x = int(x_str)
y = int(y_str)

intervalo = x

for i in range(1,y + 1):
    
    pular_linha = ' \n' if i == x else ' '
    x = x if i != x else x + intervalo 
    print(i,end=pular_linha)
    
    

        