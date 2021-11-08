"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas.

Existem basicamente duas diferenças:
1 - As tuplas são representadas por parênteses
print(type([]))
print(type(()))


2 - As tuplas são imutáveis: isso significa que ao criar uma tupla,
ela não muda.

# Cuidado 1: As tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

# Cuidado 2: Tuplas com 1 elemento (não é uma tupla):

tupla3 = (4)
print(tupla3)
print(type(tupla3))

tupla4 = (4, ) #Isso é uma tupla!
print(tupla4)
print(type(tupla4))

#Conclusão: podemos concluir que as tuplas são definidas pelas vírgulas e não pelo paenteses

tupla5 = 4,
print(tupla5)
print(type(tupla5))


# Podemos gerar uma tupla, dinamicamente, com o range (início, fim, passo)
tupla = tuple(range(11))
print(tupla)

# Desempacotamento de tupla:

tupla = ("Geek University", "Programação em Python: Essencial",)

escola, curso = tupla

print(escola)
print(curso)

print(tupla)

#Obs.: Gera erro se colocarmos um numero diferente de elementos para desempacotar

# Métodos para adição e remoção de elementos nas tuplas não existem, por serem imutáveis

# Soma*, valor máximo*, valor minimo* e tamanho (* se os valores forem todos inteiros e rais)

tupla = (1, 2, 3, 4, 5, 6,)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de tuplas:

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

tupla3 = tupla1 + tupla2  #tuplas são imutáveis!
print(tupla3)

print(tupla1)
print(tupla2)

tupla1 = tupla1 + tupla2   #podemos sobrescrever seus valores
print(tupla1)

# Verificar se determinado elemento está contido na tupla:

tupla = (1, 2, 3)

print(3 in tupla)

print(33 in tupla)


#Iterando sobre uma tupla:

tupla = (1, 2, 3)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando elementos dentro de uma tupla:

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')

print(tupla.count("a"))

print(tupla.count("d"))

escola = tuple("Geek University")

print(escola)
print(escola.count("e"))


# O acesso a elementos de uma tupla é semelhante a de uma lista
print(meses[5])

# Iterar com while:

i = 0

while i < len(meses):
    print(meses[i])
    i = i + 1
# Verificamos em qual indice um elemento está na tupla:

print(meses.index('Junho'))

#OBS.: Caso o elemento não exista, será gerado erro:

#print(meses.index('Saturno'))

# Dá para definir a partir de quando fazer as buscas, como em listas:

print(meses.index('Agosto', 6))

# Dicas na utilização de tuplas:

# Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados contidos numa coleção:

# Exemplo 1:

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro','Dezembro')

# Slicing

# tupla[inicio:fim:passo]

print(meses[0:])

print(meses[5:])

print(meses[0:9])

print(meses[2:11:2])

# Por quê utilizar tuplas:

# - Tuplas são mais rápidas do que listas.
# - Tuplas deixam seu código mais seguro, por não ser possível fazer alterações

# Copiando uma tupla para outra

tupla = (1, 2, 3)

print(tupla)

nova = tupla # Na tupla não temos o problema de shallow copy

print(nova)
print(tupla)

outra = (4, 5, 6)

nova = nova + outra

print(nova)

print(tupla)
print(outra)

"""

