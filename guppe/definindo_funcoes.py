"""
Definindo Funções

- Funções são pequenas partes de código que realizam tarefas específicas:
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- Muito úteis para executar procedimentos similares por repetidas vezes;

OBS: Se vc escrever uma função que realiza várias tarefas dentro dela,
é bom fazer uma verificação para que a função seja simplificada.


Já utilizamos várias funções desde que iniciamos este curso:

- print()
- len()
- max()
- min()
- count()
- etc.

# Exemplo de utilização de funções:

cores = [ 'verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada (Built-in) do Python print()

#print(cores)

curso = "Programação em Python Essencial"

#print(curso)

cores.append('roxo')

#print(cores)

#curso.append("Mais dados...") # error de atributo. string não possui o atributo append.

cores.clear()
#print(cores)


# DRY -  Don't Repeat Yourself - Não repita você mesmo / Não repita seu código

# Mas então, como definir funções?

Em python, a forma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao

onde:

noma_da_funcao -> SEMPRE com letras minúscula e se for nome composto, as palavras são separadas por underline;

parametros_de_entrada -> Opcionais, onde, tendo mais de um, cada um separados por vírgula;

bloco_da_funcao -> Também chamado de corpo da função ou implememtação, é onde o processamento da função acontece
podendo ter ou não retorno da função.

OBS.: Veja que para definir uma função, utilizamos a palavra reservada "def" informando ao Python
que estamos definindo uma função. Também abrimos o bloco de código com o já conhecido dois pontos:
que é utilizado em python para definir blocos.

OBS func1.:

- Veja que, dentro das nossas funções podemos utilizar outras funções (como o print);

- Veja que nossa função só executa uma tarefa, ou seja, a unica coisa que ela faz é dizer '"oi"':,

- Veja que esta função não recebe nenhum parâmetro de entrada;

- Veja que esta função não retorna nada;


"""

# Definindo a primeira função:

def diz_oi():
    print("Oi!")

# Utilizando funções:
# Chamada de execução

diz_oi() # nunca esqueça de utilizar o () antes de executar a função!

# Exemplo 2:

def cantar_parabens():
    print("Parabéns pra você")
    print("Nesta data querida")
    print("Muitas felicidades")
    print("Muitos anos de vida")
    print("Viva o aniversariante!")

# Chamando a função:

#cantar_parabens()


#for n in range(5):
    #print(n)
    #cantar_parabens()

# Em Python, podemos inclusive, criar variáveis do tipo de uma função e executar esta função através da variavel:

canta = cantar_parabens

canta()




