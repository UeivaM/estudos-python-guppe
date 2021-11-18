"""
Módulo Collections - Counter (contador)

Collections -> High-performancer Conteiner Datatypes

Tipos de dados conteiners de alta performancer

Counter -> Recebe um interável como parâmetro e cria um objeto do tipo Collections Counter
que é parecido com um dicionário, contendo como chave o elemento da lista passado como parâmetro e como valor a quantidade
de ocorrências desse elemento.

# Utilizando o Counter

from collections import Counter

# Podemos utilizar qualquer iterável. Aqui usamos uma lista.

lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

res = Counter(lista)

print(type(res))
print(res)

# Veja que, para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrèncias:

# Counter({1: 5, 3: 5, 2: 4, 5: 4, 4: 3, 45: 2, 66: 2, 43: 1, 34: 1})

print(Counter("Geek University"))

# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})

"""

from collections import Counter

texto = """ Dreaming of You é o quinto e último álbum de estúdio da cantora americana Selena. 
Lançado postumamente em 18 de julho de 1995, pelas gravadoras EMI Latin e EMI. 
Depois de assinar um contrato de gravação com a EMI Latin em 1989, o selo negou a Selena um disco que pudesse transiciona-la ao mercado pop de língua inglesa, 
o solicitado somente após ela realizar três gravações demonstrativas nesse idioma. 
Após a liberação de seu primeiro disco ao vivo, Live (1993), que a rendeu uma indicação vitoriosa ao prêmio Grammy, 
a cantora assinou com a gravadora SBK para começar as gravações de seu projeto de transição, que foi notícia de primeira página 
na revista Billboard. Em março de 1994, ela lançou Amor Prohibido; em entrevistas, Selena disse que seu álbum em inglês ainda estava sendo desenvolvido. 
As sessões de gravação de Dreaming of You começaram em dezembro de 1994; a cantora gravou quatro faixas programadas para o projeto. 
No entanto, em 31 de março de 1995, ela foi morta a tiros por Yolanda Saldívar, ex-gerente de suas butiques Selena Etc. por causa de uma disputa sobre ações de peculato.

"""
palavras = texto.split()

#print(palavras)

res = Counter(palavras)
print(res)

# Encontrando as 5 palavras com mais ocorrência no texto

print(res.most_common(5))


