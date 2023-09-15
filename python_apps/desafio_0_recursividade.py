# Desafio criar uma função recursiva que ache um elemento dentro
# de uma lista.

lista = []

for a in range(5):
    lista.append(input('Digite um nome: '))
    
print(lista)


def procura(a,b,c = 'Descomplica'):
    if(a[b] == c):
        return 'Sim'
    if(b == 0):
        return 'Não'
    return procura(a,b - 1,c)

lista_tamanho = len(lista) - 1

print(procura(lista,lista_tamanho))