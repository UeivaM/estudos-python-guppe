"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência à teoria dos conjuntos
da matemática:

  Um conjunto é uma coleção de objetos distintos, com uma descrição precisa que permita decidir
  se um dado objeto está no conjunto.

- Aqui em Python, os conjuntos são chamados de Sets.

Dito isto, da mesma forma que na matemática:

- Sets (conjuntos) não possuem valores duplicados;
- Sets não possuem valores ordenados;
- Elementos não são acessados via indice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos, mas não nos importamos com a ordenação deles
quando não precisamos se preocupar com chaves, valores e itens duplicados.

Os conjuntos (sets) são referenciados em Python com {}.

Diferença entre Conjuntos (Sets) e Dicionários (Mapas) em Python:

-  Um dicionário tem chave/valor;
- Um conjunto tem apenas valor;


# Definindo um conjunto:

# Forma 1:

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3}) # repare que temos valores repetidos.

print(s)
print(type(s))

# OBS.: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo será ignorado
# sem gerar error e não fará parte do conjunto.

# Forma 2 (Mais comum)

s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

# Podemos verificar se determinado elemento está contido no conjunto:

if 3 in s:
    print("Tem o 3")

else:
    print("Não tem o 3")

# Dá para transformar string em conjunto:

s = set ("Geek University")

print(s)

# Dá para transformar lista ou tupla em conjunto, após a conversão, as repetições são excluídas:

lista = [1, 2, 3, 8, 5, 5, 3, 8]

print(lista)
print(set(lista))

# Importante lembrar que, além de não termos valores duplicados, não temos ordem:

# Listas aceitam valores duplicados, então temos 10 elementos.

lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f"Lista: {lista} com {len(lista)} elementos")


# Tuplas aceitam valores duplicados, então temos 10 elementos.

tupla = (99, 2, 34, 23, 2, 12, 1, 44, 5, 34)
print(f"Tupla: {tupla} com {len(tupla)} elementos")


# Dicionários não aceitam chaves duplicados, então temos 8 elementos.

dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f"Dicionário: {dicionario} com {len(dicionario)} elementos")


# Conjuntos não aceitam valores duplicados, então temos 8 elementos.

conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f"Conjunto: {conjunto} com {len(conjunto)} elementos")

# Assim como todo outro conjunto Python podemos colocar tipos de dados nisturadps em Sets:

s ={1, 'b', True, 34, 22, 44}

print(s)
print(type(s))

# Podemos iterar em um Set normalmente:

for valor in s:
    print(valor)

# Usos interessantes com sets:

# Imagine que fizemos um formulário de cadastrado de visitantes em uma feira ou museu.
# E os visitantes informam manualmente a cidade de onde vieram.

# Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos
# e ter repetição.


cidades = ["Belo Horizonte", "São Paulo", "Campo Grande", "Cuiabá", "Campo Grande", "São Paulo", "Cuiabá"]

print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, únicas, temos.

# O que vc faria? Faria um loop na lista...?

# Podemos utilizar o set para isso, já que não pode haver repetições:

print(len(set(cidades))) # o set remove as duplicidades.

print(set(cidades))

# Adicionando elementos em umm conjunto (são mutáveis):

s = {1, 2, 3}
s.add(4)
s.add(4) # Duplicidade não gera erro, simplesmente é ignorado.
print(s)

# Removendo elementos em um conjunto (são mutáveis):

s = {1, 2, 3}
print(s)

# Forma 1:

ret= s.remove(3) # não é indice! informamos o valor a ser removido.
print(s)
print(ret)  # .remove() não retorna o valor removido.

# OBS.: Caso o valor não seja encontrado, será gerado o erro keyError.

# Forma 2:

s.discard(2)
s.discard(22) # Se o valor não for encontrado, nenhum erro é gerado.
print(s)


s = {1, 2, 3}
print(s)

# Copiando um conjunto para outro...

# Forma 1 - Deep Copy:

novo = s.copy()
print(novo)

novo.add(4)
print(novo)
print(s)

# Forma 2 - Shalow Copy:

nova = s
print(nova)

nova.add(4)
print(nova)
print(s)


s = {1, 2, 3}
print(s)

# Podemos remover todos os itens de um conjunto:

s.clear()
print(s)

# Métodos Matemáticos de conjuntos:

# Imagine que temos dois conjuntos: um contendo estudantes do curso Python
# e um contendo estudandes do curso de java.


estudantes_python = {"Marcos", "Patricia", "Ellen", "Pedro", "Julia", "Guilherme"}
estudantes_java = {"Fernando", "Gustavo", "Julia", "Ana", "Patricia"}

# Obs.: Veja que alguns alunos que estrudam Python também estudam Java.

# Precisamos gerar um conjunto com nomes de estudantes únicos

# Forma 1- Utilizando union (mais recomendada:

unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)
unicos1 = estudantes_java.union(estudantes_python)
print(unicos1)
print(len(unicos1))

# Forma 2 - Utilizando o caractere pipe |

unicos2 = estudantes_python | estudantes_java

print(unicos2)


# Forma 3 (teste):

unicos3 = estudantes_python + estudantes_java

# Dá error

# Obs.: Veja que alguns alunos que estrudam Python também estudam Java.

# Gerar um conjunto de estudantes que estão em ambos os curos.

# Forma 1 - Utilizando intersection:

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - Utilizando o &

ambos2 = estudantes_python & estudantes_java
print(ambos2)


# Gerar um conjunto de estudantes que não estão no outro

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)
"""

# Soma*, máximo*, mínimo* e tamanho:

s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))

