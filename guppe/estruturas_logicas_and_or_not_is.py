"""
Estruturas lógicas: and, or, not, is

Operadores unários:

   - not;
Operadores binários:

   - and, or, is

REGRAS DE FUNCIONAMENTO:

Para 'and', ambos os valores precisam ser verdadeiros
Para o 'or" um ou outro precisa ser verdadeiro
Para 'NOT' o valor do boleano é invertido
Para o 'IS" o primeiro valor é comparado com o segundo
"""
"""
ativo = True
logado = False

if ativo:
    print("Usuário ativo no sistema")
"""

"""
AND:

ativo = True
logado = False

if ativo and logado:
    print("Bem-vindo ao sistema!")

else:
    print("Você precisa ativar sua conta. Por favor, cheque seu e-mail")
"""

"""
#OR
ativo = False
logado = False

if ativo or logado:
    print("Bem-vindo ao sistema!")

else:
    print("Você precisa ativar sua conta. Por favor, cheque seu e-mail")

"""
"""
#NOT

ativo = True
logado = False

if not ativo:
    print("Você precisa ativar sua conta. Por favor, cheque seu e-mail")

else:
    print("Bem-vindo ao sistema!")

"""

#IS

ativo = True
logado = False

if ativo is False:
    print("Você precisa ativar sua conta. Por favor, cheque seu e-mail")

else:
    print("Bem-vindo ao sistema!")

