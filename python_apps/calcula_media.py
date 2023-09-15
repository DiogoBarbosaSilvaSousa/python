def calcula_media():
    nota_1 = float(input("Digite a primeira nota: "))
    nota_2 = float(input("Digite a segunda nota: "))
    media = (nota_1 + nota_2) / 2
    if media >= 7:
        print("Aprovado")
    elif media >= 3 and media < 6.9:
        print("Prova final")
    else:
        print("Reprovado")
    print("Nota final: ", media)
    
calcula_media()