# Questão 5
# Neste problema você deverá ler 3 palavras que definem um possível animal, segundo o esquema
# abaixo, da esquerda para a direita. Em seguida, informe qual dos animais foi escolhido,
# através das três palavras fornecidas. Assuma que não será informada nenhuma palavra fora do
# esquema.

animais = {}
animais['vertebrado'] = {}

animais['vertebrado']['ave'] = {}
animais['vertebrado']['ave']['carnivoro'] = {'aguia'}
animais['vertebrado']['ave']['onivoro'] = {'pomba'}

animais['vertebrado']['mamifero'] = {}
animais['vertebrado']['mamifero']['onivoro'] = {'homem'}
animais['vertebrado']['mamifero']['herbivoro'] = {'vaca'}

animais['invertebrado'] = {}

animais['invertebrado']['inseto'] = {}
animais['invertebrado']['inseto']['hematofago'] = {'pulga'}
animais['invertebrado']['inseto']['herbivoro'] = {'lagarta'}

animais['invertebrado']['anelideo'] = {}
animais['invertebrado']['anelideo']['hematofago'] = {'sanguessuga'}
animais['invertebrado']['anelideo']['onivoro'] = {'minhoca'}

esqueleto = input('Escolha um dos números 1-Vertebrado ou 2-Invertebrado: ')
#esqueleto = 'vertebrado' if int(esqueleto) == 1 else 'invertebrado'


if(int(esqueleto) == 1):
    tipo = input('Escolha um dos números 1-Mamífero ou 2-Ave: ')
    
    if(int(tipo) == 1):
        alimentacao = input('Escolha um dos números 1-Onívoro ou 2-Herbívoro: ')
        if(int(alimentacao) == 1):
            print(animais['vertebrado']['mamifero']['onivoro'])
            
        if(int(alimentacao) == 2):
            print(animais['vertebrado']['mamifero']['herbivoro'])
            
    if(int(tipo) == 2):
        alimentacao = input('Escolha um dos números 1-Carnívoro ou 2-Onívoro: ')
        if(int(alimentacao) == 1):
            print(animais['vertebrado']['ave']['carnivoro'])
            
        if(int(alimentacao) == 2):
            print(animais['vertebrado']['ave']['onivoro'])

if(int(esqueleto) == 2):
    tipo = input('Escolha um dos números 1-Inseto ou 2-Anelídeo: ')
    
    if(int(tipo) == 1):
        alimentacao = input('Escolha um dos números 1-Hematofago ou 2-Herbívoro: ')
        
        if(int(alimentacao) == 1):
            print(animais['invertebrado']['inseto']['hematofago'])
            
        if(int(alimentacao) == 2):
            print(animais['invertebrado']['inseto']['herbivoro'])
            
    if(int(tipo) == 2):
        alimentacao = input('Escolha um dos números 1-Hematofago ou 2-Onívoro: ')
        
        if(int(alimentacao) == 1):
            print(animais['invertebrado']['anelideo']['hematofago'])
            
        if(int(alimentacao) == 2):
            print(animais['invertebrado']['anelideo']['onivoro'])
    
    