# Questão 9
# A corrida de lesmas é um esporte que cresceu muito nos últimos anos, fazendo com que várias pessoas
# dediquem suas vidas tentando capturar lesmas velozes, e treina-las para faturar milhões em corridas pelo
# mundo. Porém a tarefa de capturar lesmas velozes não é uma tarefa muito fácil, pois praticamente todas as
# lesmas sao muito lentas. Cada lesma é classificada em um nível dependendo de sua velocidade:
# • Nível 1: Se a velocidade é menor que 10 cm/h
# • Nível 2: Se a velocidade é maior ou igual a 10 cm/h e menor que 20 cm/h
# • Nível 3: Se a velocidade é maior ou igual a 20 cm/h
# Sua tarefa  identificar qual nível de velocidade da lesma mais veloz em um grupo de dez lesmas. Leia a
# velocidade de cada uma e informe o nível de velocidade da mais rápida.

lesma = {}

lesma[1] = 8
lesma[2] = 18
lesma[3] = 10
lesma[4] = 9
lesma[5] = 8
lesma[6] = 22
lesma[7] = 18
lesma[8] = 15
lesma[9] = 12
lesma[10] = 23

maior_velocidade = 0

for i in range(1, len(lesma) + 1):
    maior_velocidade = lesma[i] if lesma[i] > maior_velocidade else maior_velocidade
        
if(maior_velocidade >= 20):
    print('Nível 3: A velocidade é maior ou igual a 20 cm/h')
elif(maior_velocidade >= 10):
    print('Nível 2: A velocidade é maior ou igual a 10 cm/h e menor que 20 cm/h')
else:
    print('Nível 1: A velocidade é menor que 10 cm/h')

print('A maior velocidade é de {} cm/h '.format(str(maior_velocidade)))