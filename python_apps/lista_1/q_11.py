# Questão 11
# A sequência infinita de números (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...)
# é conhecida como sequência de Fibonacci.
# Nessa sequência, cada número, depois dos 2 primeiros,
# é igual a soma dos 2 anteriores, ou seja: 
# f(n) = f(n − 1) + f(n − 2)
# Escreva um algoritmo que leia um inteiro N e calcule a soma dos valores pares
# dentre os N primeiros termos desta sequência

n_str = input('Digite um número inteiro: ')

n = int(n_str)

passado = 0
presente = 1
lista = [passado,presente]
soma_pares = 0

for i in range(2,n):    
      # O futuro é a junção do passado com o presente
      futuro = passado + presente
      # O presente se torna passado
      passado = presente
      # O presente recebe o futuro
      presente = futuro      
      
      lista.append(presente)
      
      soma_pares = soma_pares if (presente % 2) != 0 else soma_pares + presente
      
      
      
print(lista)
print('A soma dos números pares é {}'.format(soma_pares))