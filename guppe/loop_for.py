nome = "Geek University"
"""
for letra in nome:
    print(letra)

numero = [4, 5, 8, 9, 10]

for lista in numero:
    print(lista)

for a in range(1,11):
    print(a)

for i, letra in enumerate(nome):
    print(i)

    print(letra)


for i, letra in enumerate(nome):
  print(letra)

#Quando não precisamos de um valor, podemos descartá-lo com um _:
for _, letra in enumerate(nome):
  print(letra)

for valor in enumerate(nome):
    #print(valor)

    #print(valor[0])

    print(valor[1])

qtd = int(input("Quantas vezes esse loop deve rodar? \n"))

for n in range(1,qtd+1):
    print(f"Imprimindo {n}")


qtd = int(input("Quantas vezes esse loop deve rodar? \n"))
soma = 0

for n in range(1,qtd+1):
    num = int(input(f"Insira o valor {n} de {qtd}: \n"))
    soma = num + soma

print(f"A samotória dos valores é {soma}")

TABELA DE EMOJIS: https://apps.timwhitlock.info/emoji/tables/unicode

"""
nome = "Geek "

for i in range (1,11):
    print(nome * i)

#Original: U+1F63B

#Modificado: U0001F63B

emoji = "\U0001F63B"
for _ in range(3):
    for i in range (1,15):
        print (emoji * i)