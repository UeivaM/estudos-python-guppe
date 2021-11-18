"""
Módulo Collections - Deque

Podemos dizer que o deque é uma lista de alta performance.

"""

# Importando:

from collections import deque

# Criando deques

deq = deque('Geek')

print(deq)

# Add elementos no deque

deq.append('y') # ADD no final

print(deq)

deq.appendleft('k') # Add no começo (só com o deque)
print(deq)

# Remover elementos:

print(deq.pop()) # remove e retorna o último elemento

print(deq)

print(deq.popleft())
 # remove e retorna o primeiro elemento

print(deq)