'''
Tipo númerico

Tipo float , tipo ral, tipo decimal

Obs.: o separador de casas decimais na programação é o ponto, não a vírgula

Tipo boleano

Algebra boleana, criada por George Boole
Temos duas constantes: verdadeiro e falso (no python em ingles0:

True -> Verdadeiro
False ->

OBS.: Sempre com a letra maiúscula
'''

"""
#erradodo ponto de vista do float, mas gera uma tupla:
Valor = 1, 88
print(Valor)

#Certo

valor = 1.88
print(valor)
print(type(Valor))
print(type(valor))


# É possível fazer dupla atribuição:

valor, valor2 = 2, 55

print(valor)
print(valor2)

# Podemos converter um float para inteiro
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com números complexos
variavel = 5j

ativo = True

print(ativo)

#Operações básicas:
# Negação (not): fazendo a negação, se o valor boleano for verdadeiro, o resultado será falso
# Se for falso, o resultado será verdadeiro

print(not(ativo))

# Ou (or):
# É uma operação binária, ou seja, depende de dois valores
#Ou um ou outro deve ser verdadeiro

#True or True = True; True or False = True; False or True = True; False or False =  False

ativo = False

logado = True

print (ativo or logado)

# E (and)
# Depende dos dois valores, ambos devem ser verdadeiros

num = 7
num2 = 9

num >= num2

"""

# O Tipo string

nome = 'Geek University'
print(nome.split())

nome2 = 'Geek'
print(nome2.split())
print(nome.split()[0])

# slice de string:

print(nome[5:15])

# [:: -1] -> comece do primeiro elemeto, vá até o último e inverta.

print(nome[:: -1])  # inversão da string

print(nome.replace('e', 'i'))

nome = 'ueiva'
print(nome[:: -1])