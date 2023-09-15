lista = {}
lista['11'] = 'São Paulo'
lista['19'] = 'Campinas'
lista['21'] = 'Rio de Janeiro'
lista['27'] = 'Vitória'
lista['31'] = 'Belo Horizonte'
lista['32'] = 'Juíz de Fora'
lista['61'] = 'Brasília'
lista['71'] = 'Salvador'

n = input('Digite um DDD: ')

consta_na_lista = n in lista

if consta_na_lista :
    print('O DDD {} é de {}'.format(n,lista[n]))
else:
    print('DDD não cadastrado')
 

