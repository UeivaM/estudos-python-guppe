'''
Listas

Listas em Python finciona como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem DINÂMICAS e também d podermos colocar QUALQUER tipo de dado.

Nas linguagens C/Java elas possuem tamanho e tipo de dado fixo;

Ou seja, se vc criar um array do tipo int e com tamanho , este arrey será sempre do tipo inteiro e poderá ser sempre no máximo .

Já no Python:
-  Dinâmico: Não possui tamanho fixo: ou seja, podemos criar a lista e ir simplemesnte adicionando elementos
Enquanto houver memória disponível, você pode adicionar elementos.

- Qualquer tipo de dado: não possuem tipo de dado fixo, ou seja, podemos colocar qualquer tipo de dado.

As listas em Python, são representadas por colchetes []

#Podemos checar se determinado valor está contido na lista, com qualquer tipo de dado:

print(lista4)
num = 2
if num in lista4:
    print(f"Encontrei o num {num}")

else:
    print(f"Não encontrei o num {num}")

#Podemos facilmente ordenar uma lista;

print(lista1)
lista1.sort()

print(lista1)

print(lista5)
lista5.sort()
print(lista5)

#POdemos facilmente contar o número de ocorrências de um valor
# em uma lista:

print(lista1.count(1))
print(lista5.count('e'))

# Adicionar elementos em listas:

Para adicionar elementos/valores em listas, utilizamos a função append
OBS.: Com appedn, nós só conseguimos adicionar 1 elemento por vez, mas posso adicionar outra lista, mas fica uma lista dentro de outra lista

print(lista1)
lista1.append(42)
print(lista1)

#lista1.append(42,3,8) => erro

lista1.append([8,3,1]) #objetos únicos
print(lista1)

if [8,3,1] in lista1:
    print("Encontrei a lista")
else:
    print("Não encontrei a lista")

#Com o extend coloca cada elemento da lista como valor adcional à lista
#adciona um a um
#O extend não aceita valores únicos, deve ser iterável: lista, string com mais de uma letra
lista1.extend([123,'U',67])
print(lista1)


#Podemos também inserir um valor numa determinada posição (usando insert):
#Isso não substitui o valor origina, que será deslocado para a direita
lista1.insert(2,'Novo Valor')
print(lista1)


#Podemos facilmente juntar duas listas:

#lista6 = lista1 + lista2
lista1.extend(lista2) #adiciono a lista2 no fim da lista1, sem precisar comprar uma nova lista
print(lista1)

print(lista6)

#Invertendo listas:
#Forma1:

lista1.reverse()
lista2.reverse()

print(lista1)
print(lista2)

#Invertendo com slice:
#Forma2:
print(lista1[::-1])
print(lista2[::-1])

#Podemos copiar uma lista na outra:

lista6= lista2.copy()
print(lista6)

#Podemos contar quantos elementos existem dentro da lista
#o count conta as ocorrências de um elemento

print(len(lista5))


#Removendo o último elemento de uma lista ou de qualquer posição que for definida (pelo índice):
#OBS> O POP não só remove o elemento, como retorna o dado se solicitado


print(lista5)
lista5.pop()
print(lista5)

lista5.pop(3)
print(lista5)

#Podemos eliminar todos os itens da lista de uma vez:

print(lista5)
lista5.clear()
print(lista5)

print(nova)
nova = nova*3
print(nova)

#Convertendo string em lista (O slpit separa cada item pelo espaço, por padrão. Mas vc pode delimitar o divisor, como uma virgula):

curso = "Python Essencial"

print(curso)
curso = curso.split()
print(curso)

curso = 'Curso,de,python,essencial'
curso = curso.split(',')

print(curso)

#Convertendo lista em string:

lista6 = ['Programação', 'em', 'python', 'essencial']

print(lista6)

#Comando join() usado abaixo: pegue a lista6, coloque um espaço entre cada elemento e transforme em uma string:

lista6 = ' '.join(lista6)
print(lista6)

lista6 = lista6.split()
print(lista6)

#pegue a lista6, coloque um $ entre cada elemento e transforme em uma string:
lista6 = '$'.join(lista6)
print(lista6)

#Podemos colocar qualquer tipo de dados dentro da liste, inclusive misturando-os:

lista6 = [1, 2.4, True, "Geek", "G", [1,2,3], 458593]
print(lista6)
print(type(lista6))


# Iterando sobre lista:
#Ex. 1 Usando o FOR:

soma = 0
for pqp in lista4:
    print(pqp)
    soma = soma + pqp

print(soma)

#com string:

soma = " "
for i in lista2:
    print(i)
    soma = soma + i

print(soma)

#Ex. 2 Usando WHILE:
# Carrinho de compras:

carrinho = []
produto = ''

while produto != "sair":
    produto = input("Insira um produto no carrinho ou digite 'sair' para sair: \n ")
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

print(carrinho)

#É possível colocar variáveis em listas:

numeros = [1,2,3,4,5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]

print(numeros)


for cor in cores:
    print(cor)

i = 0
while i < len(cores):
    print(cores[i])
    i = i + 1

print(len(cores))

for i, cor in enumerate(cores):
    print(i, cor)

#listas aceitam valores repetidos:

lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)

print(lista)

# Encontrar o indice de algum valor/elemento com index:

numeros = [5, 6, 7, 5, 8, 9, 10, 11, 12]

# Em qual indice da lista está o valor 6?
print(numeros.index(6))

# Em qual indice da lista está o valor 9?
print(numeros.index(9))

#OBS.: Caso não haja o elemento na lista ele apresentará um erro e para valores repetidos ele retorna o primeiro encontrado:

# Em qual indice da lista está o valor 20?
#print(numeros.index(20))

# Em qual indice da lista está o valor 5?
print(numeros.index(5))

#podemos fazer buscas dentro de um range, ou seja, de onde começar a busca:
print(numeros.index(5, 1)) # Buscando a partir do indice 1
print(numeros.index(5, 2)) # Buscando a partir do indice 2
print(numeros.index(5, 3)) # Buscando a partir do indice 3
#print(numeros.index(5, 4)) # Buscando a partir do indice 4

#podemos fazer buscas dentro de um range, com início e fim:
print(numeros.index(8, 3, 6)) # Buscando entre o indice 3 e 6

# Revisão slicing:
#lista[inicio:fim:passo]
#range[inicio:fim:passo]

#Trabalhando com slice de lista com o parâmetro "inicio";

lista = [1, 2, 3, 4, 5, 6]
print(lista[1:]) # definindo que será iniciado no indice 1
print(lista[3:]) # definindo que será iniciado no indice 3

# Trabalhando com slice de lista com o parâmetro "fim":

print(lista[:2]) #começa em 0, pega até o indice 2 -1

print(lista[:4]) # começa em 0, pega até o indice 4 - 1

print(lista[1:4]) # começa em 1 e vai até o 4 -1


# Trabalhando com slice de lista com o parâmetro "passo":

print(lista[1::2]) # começa a partir do indice 1, contando de dois em dois

print(lista[1:4:2]) # começa a partir do indice 1, vai até o indice 4 -1, contando de dois em dois

print(lista[::2]) # começa em 0, vai até o fim, de 2 em 2

#Invertendo valores em uma lista;

nome = ["Geek", "University"]

print(nome)
nome.reverse()

print(nome)

# Soma*, Valor máximo*, Valor mínimo, Tamanho:

# * se todos números inteiros (int) e reais (float)

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista))
print(max(lista))
print(min(lista))
print(len(lista))


#Transformando lista em tuplas:

print(lista1)
print(type(lista1))

tupla = tuple(lista1)

print(tupla)
print(type(tupla))


# Desempacotamento de lista:

lista = [1, 2, 3, 4]

num1, num2, num3, num4 = lista
print(num1)
print(num2)
print(num3)
print(num4)

#OBS.: Se tivermos mais elementos para desempacotar do que váriaveis para rebecer os valores, teremos vallue error e vice versa

#métodos úteis:

#Cpiando uma lista para outra (Shalow Copy e Deep Copy)

#Forma 1 DEEP COPY

lista = [1, 2, 3]
print(lista)

nova = lista.copy()

nova.append(4)

print(lista)
print(nova)

#Com o copy(), as listas são idependentes. Modificando uma lista, não afeta a outra. Isso em python é chamado de deep copy (cópia profunda)


# Forma 2 SHALOW COPY:

lista = [1, 2, 3]
print(lista)

nova = lista
nova.append(4)

print(lista)
print(nova)

# Cópia via atrubuição: copiamos os dados da lista para a nova lista, mas modificando uma lista, modifica a outra. Em Python isso é chamado de shalow copy



'''

type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G','e', 'e','k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

nova = [1,2,3]

cores = ['verde', 'amarelo', 'azul', 'branco']



