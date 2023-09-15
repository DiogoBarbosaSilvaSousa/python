# Questão 1
# Elabore um programa que leia o nome de dois times de futebol e dois inteiros correspondendo
# ao número de gols de cada time em uma partida. Informe o resultado da partida.

time_1 = input('Digite o nome do primeiro time: ')
time_1_gols = input('Digite o número de gols do primeiro time: ')
time_2 = input('Digite o nome do segundo time: ')
time_2_gols = input('Digite o número de gols do segundo time: ')
    
if int(time_1_gols) >  int(time_2_gols):
    print('O {} venceu de {} x {}'.format(time_1,time_1_gols,time_2_gols))
elif int(time_1_gols) <  int(time_2_gols):
    print('O {} venceu de {} x {}'.format(time_2,time_1_gols,time_2_gols))
else:
    print('Os times empataram {} x {}'.format(time_1_gols,time_2_gols))