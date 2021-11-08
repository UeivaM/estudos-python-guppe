"""
Recebendo dados do usuário

Todo dado recebido via input é do tipo string

Tudo que estiver em aspas simples, asplas duplas, aspas simples triplas, aspas duplas triplas, são strings

cast é quando eu converto um tipo de dado para ouro
"""
# entrada de dados
#print('Qual o seu nome?')
#nome = input()

nome = input('Qual o seu nome?')

#Exemplo de print antigo:
#print("Seja bem-vindo(a) %s" %nome)

#Exemplo de print moderno:
#print('Seja bem vindo(o) {0}'.format(nome))

#Exemplo de print mais atual:
print(f'Seja bem-vindo(a) {nome}')

#print('Qual a sua idade?')
#idade = input()

idade = int(input('Qual a sua idade?'))

# processamento

# saída de dados:

#Exemplo de print antigo:
#print('A(o) %s tem %s anos.' % (nome, idade))


#Exemplo de print moderno:
#print('A {0} tem {1} anos'.format(nome,idade))

#Exemplo de print mais atual:
print(f'A {nome} tem {idade} anos')

print(f'A {nome} nasceu em {2021 - idade}')

