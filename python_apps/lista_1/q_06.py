# Questão 6
# Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço
# normal de etiqueta e a escolha da condição de pagamento. Utilize os códigos a seguir para
# ler qual a condição de pagamento escolhida e efetuar o cálculo adequado (1 a 4).
# 1. A vista em dinheiro ou pix, recebe 15% de desconto;
# 2. A vista no cartão de crédito, recebe 10% de desconto;
# 3. Parcelado em duas vezes, preço normal de etiqueta sem juros;
# 4. Parcelado em três vezes, preço normal de etiqueta mais juros de 10%.
print('Produto no valor de R$ 1000,00;')
print('1. A vista em dinheiro ou pix, recebe 15% de desconto;')
print('2. A vista no cartão de crédito, recebe 10% de desconto;')
print('3. Parcelado em duas vezes, preço normal de etiqueta sem juros;')
print('4. Parcelado em três vezes, preço normal de etiqueta mais juros de 10%.')

tipo_pagamento = input('Digite o número da forma de pagamento: ')

match tipo_pagamento:
    case "1":
      valor = 1000 * 0.85
      print('O valor é R$ ', str(valor))
    case "2":
      valor = 1000 * 0.90
      print('O valor é R$ ', str(valor))
    case "3":
      valor = 1000 / 3
      valor = round(valor,2)
      print('O valor de cada parcela é R$ ', str(valor))
    case "4":
      valor = (1000 * 1.1) / 3
      valor = round(valor,2)
      print('O valor de cada parcela é R$ ', str(valor))
    case other:
      print('Não é uma opção válida')
        


