"""
Dicionários

OBS.: Em algumas liguagens de programação, os dicionários python
são conhecidos por mapas.

Dicionários são coleções do tipo chave/valor

Dicionários são representados por chaves {}.

print(type({}))

OBS.: -  Chave e valor são separados por dois pontos "chave: valor"
      - Tanto a chave quanto o valor podem ser de qualquer tipo de dado;
      - Podemos misturar tipos de dados

# Criação de dicionários;

# Forma 1 (mais comum)

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

# Forma 2 (menos comum):

paises = dict(br='Brasil', eua = 'Estados Unidos', py='Paraguai')

print(paises)
print(type(paises))

#Dicionários n]ao são indexados, pois tem chave definida

# Acessando elementos

# Forma 1 - Acesando via chave, da mesma forma que lista/tupla:

print(paises['br'])
print(paises['py'])
#print(paises['ru'])

#Acesso a chave q não existe teremos o erro: KeyError

# Forma 2 -  Acessando via get - Recomendado!

print(paises.get('br'))
print(paises.get('ru'))  #Mostra NONE quando não existe, não dá erro
print(paises.get('eua'))

russia = paises.get('ru')

Caso o GET não encontre o objeto com a chave informada, será retornado o valor None e não será gerado o KEY ERROR

if russia:
    print("Encontrei o país!\n")

else:
    print("Não encontrei o país!\n")

pais = paises.get('py')

if pais:
    print(f"Encontrei o país {pais}!\n")

else:
    print("Não encontrei o país!\n")

pais = paises.get('ru', 'Não encontrado.')

print(f"Encontrei o país {pais}!\n")



pais = paises.get('py', 'Não encontrado.')

print(f"Encontrei o país {pais}!\n")

OBS.: Com o get podemos definir um valor padrão para caso não encontremos o objeto da chave informada

# Verificando se determinada chave se encontra no dicionario
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises) # Estados unidos não é chave é valor. Ele busca pela chave

if 'ru' in paises:
    russia = paises['ru']

# podemos utilizar qualquer tipo de dado (int, float, str, bolean), inclusive lista, tupla, dicionario,
# como chaves de dicionarios.

localidades = {
    (35.6895, 39.6917): 'Escritótio em Tókyo',
    (40.7128, 74.0060): 'Escritótio em Nova York',
    (37.7749, 122.4194): 'Escritótio em São Paulo'

}
# OBS: Tupla como chave, pois são imutáveis, dados do tipo float indicandoo longitude e latitude

print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionário

receita = {'jan' : 100, 'fev': 120, 'mar': 300}
print(receita)
print(type(receita))

# Forma 1 - Mais comum:

receita['abr'] = 350

print(receita)

# Forma 2

novo_dado = {'mai': 500}

receita.update(novo_dado) # ou receita.update({'mai':500)

print(receita)

#Com o update() é possível atualizar dados de um dicionário:

#Forma 1

receita['mai'] = 550

print(receita)

#Forma 2

receita.update({'mai': 600})

print(receita)

# Conclusão 1: A forma de adicionar e atualizar dados em um dicionário é a mesma.

# Conclusão 2: Em dicionários, NÃO podemos ter chaves repetidas.

# Removendo dados de um dicionário

receita = {'jan' : 100, 'fev': 120, 'mar': 300}

# Forma 1 - Mais comum

ret = receita.pop('mar')

print(receita)

print(ret)

# OBS 1.: Aqui precisamos SEMPRE informar a chave, e caso não encontre o elemento, um KeyError é informado
# OBS 2.: Ao removermos um objeto, o valor deste objeto é sempre retornado.

# Forma 2

del receita['fev']

print(receita)

# del receita ['fev'] -> se a chave não existir será gerado um kayError

# Neste caso, o valor removido não é retornado.

# Imagine que você tem um comércio eletrônico, onde temos um carrinho de compras na qual adicionamos produtos

# 1 - Poderíamos utilizar uma lista para isso? Sim.

carrinho = []

produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['God of war 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teríamos que saber qual é o indice de cada informação no produto.

# 2 - Poderíamos utilizar uma Tupla para isso? Sim.

produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('God of War 4 ', 1, 150.00)

carrinho = (produto1, produto2)

print(carrinho)

# Também teríamos que saber qual é o indice de cada informação no produto.

# 3 - Poderíamos utilizar um Dicionário para isso? Sim

carrinho = []

produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preço': 2300.00}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preço': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Desta foorma, facilmente adicionamos ou removemos produtos do carrinho
# e em cada produto podemos ter a certeza sobre cada informação.


# Métodos de Dicionários

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

# Limpar o dicionário (zerar dados):

d.clear()

print(d)


# Copiandoo um dicionário para outro

# Forma 1 - Deep Copy

novo = d.copy()
print(novo)

novo['d'] = 4

print(novo)
print(d)

# Forma 2 - Shallow Copy

novo = d

print(novo)

novo['d'] = 4

print(d)
print(novo)

"""

# forma não usual de criação de dicionários

outro = {}.fromkeys('a','b')

print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')

print(usuario)
print(type(usuario))

# O método fromkeys recebe dois parâmetros: um iterável e um valor
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado

veja = {}.fromkeys('teste', 'valor')

print (veja)

veja = {}.fromkeys(range(1,11), 'novo')

print(veja)






