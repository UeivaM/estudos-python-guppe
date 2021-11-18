"""
Módulo Collections: Named Tuple

# Recap tupla

tupla = (1, 2, 3)

print(tupla[1])

Named tuple -> São tuplas diferenciadas, onde especificamos um nome a mesma e também parâmetros.


"""

# Importando:

from collections import namedtuple

# Precisamos definir o nome e parâmetros.

# Forma 1 - Delcaração Named Tuple

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 = Declaração Named Tuple (parâmetros separados por vírgula)

cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declaração Named Tuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando

ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')

print(ray)

# Acessando os dados
# Forma 1

print(ray[0])
print(ray[1])
print(ray[2])

# Forma 2

print(ray.idade)
print(ray.raca)
print(ray.nome)

print(ray.index('Chow-Chow'))
print(ray.count('Chow-Chow'))
