#open('teste.txt','x')
# R = READ
# W = WRITE
# E = eXecute
# A = Append
# R+
# WB
# Link - https://www.geeksforgeeks.org/writing-to-file-in-python/

# Python 3
# Python programa para demonstração
# Escrevendo em um arquivo

arquivo = 'D:\\python_apps\\manipulacao_de_arquivos\\arquivo3.txt'

conteudo = open(arquivo,'a')
linha = ["Texto 1 \n", "Texto 2 \n", "Texto 3 \n"]
conteudo.writelines(linha)
conteudo.close()

conteudo = open(arquivo, 'r')
print(conteudo.read())
conteudo.close()

path = 'D:\\python_apps\\manipulacao_de_arquivos\\arquivo1.txt'

# Opening a file
file1 = open(path, 'w')
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
s = "Hello\n"
 
# Writing a string to file
file1.write(s)
 
# Writing multiple strings
# at a time
file1.writelines(L)
 
# Closing file
file1.close()
 
# Checking if the data is
# written to file or not
file1 = open(path, 'r')
print(file1.read())
file1.close()