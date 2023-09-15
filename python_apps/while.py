a = []
b = 1

while b <= 3:
    a.append(input("Digite um nome de aluno: "))
    b = b + 1
    
print("Alunos:")
for a in a:
    print(a)