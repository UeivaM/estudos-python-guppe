"""
Módulo Collections: Ordered Dict

# Em um dicionário, a ordem de inserção dos elementos não é garantida
dicionario = { 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

print(dicionario)

for chave, valor in dicionario.items():
    print(f'Chave={chave}: valor={valor}')

OPrderedDict -> É um dicionário que nos garante a ordem de inserção dos elementos.


# Fazendo o imort:

from collections import OrderedDict

dicionario = OrderedDict({ 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'Chave={chave}: valor={valor}')

"""

# Entendendo a diferença entre Dict e Ordered Dict:

# Dicionários comuns

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2) # True -> Para o dicionário comum a ordem não importa.

# Ordered Dict

from collections import OrderedDict

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2) # False -> neste caso a ordem importa. Só seriam iguais se seguissem a mesma ordem.



