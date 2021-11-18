"""
Mapas -> Conhecidos em Python como Dicionários.

Dicionários em Python são representados por chaves {}

#Iterar sobre dicionários:

for chave in receita:
    print(chave)

# Ou:

for chave in receita:
    print(receita[chave])

for chave in receita:
    print (f'\n Em {chave} recebi R$ {receita[chave]} \n')

# Acessando as chaves:

print(receita.keys())

for chave in (receita.keys()):
    print(receita[chave])

#Acessando os valores:

print(receita.values())

for valor in receita.values():
    print(valor)

# Desempacotamento de dicionários:

print(receita.items())

for chave, valor in receita.items():
    print(f"chave={chave} e valor={valor}")

# Soma*, valo máximo*, valor minimo* e tamanho:

# * Só  para quando os valores forem inteiros e reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))

"""

receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(receita)



