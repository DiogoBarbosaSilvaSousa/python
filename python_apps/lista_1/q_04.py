# Questão 4
# Leia dois valores reais com uma casa decimal (x e y), que devem representar as coordenadas
# de um ponto em um plano. A seguir, determine a qual quadrante pertence o ponto, ou se está
# sobre um dos eixos cartesianos ou na origem (x = y = 0).

c_x = input('Digite a coordenada X: ')
c_y = input('Digite a coordenada Y: ')

x = float(c_x)
y = float(c_y)

origem = (x == 0.0 and y == 0.0) 

if origem:    
    print('O ponto está na origem (0,0)')
elif(x > 0 and y > 0):
    print('Quadrante 1')
elif(x < 0 and y > 0):
    print('Quadrante 2')
elif(x < 0 and y < 0):
    print('Quadrante 3')
elif(x > 0 and y < 0):
    print('Quadrante 4')
else:
    print('O ponto está sobre um dos eixos')