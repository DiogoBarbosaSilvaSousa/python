a = 0

b = input('Você pediu - e ganhou - um animal de estimação ? (S/N)')
if b == 'S':
    a = a + 1
    
b = input('Você sempre teve o seu próprio quarto ? (S/N)')
if b == 'S':
    a = a + 1
    
b = input('Você levava dinheiro para comprar lanche na cantina da escola ? (S/N)')
if b == 'S':
    a = a + 1
    
b = input('Havia uma foto sua emoldurada em posição destaque na casa ? (S/N)')
if b == 'S':
    a = a + 1
    
if a >= 3:
    print('Certamente Mimada')
elif a >= 1:
    print('Um pouco Mimada')
else:
    print('Nada Mimada')