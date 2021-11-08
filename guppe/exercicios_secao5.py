"""
#1

numero1 = 50
numero2 = 91

if numero1 > numero2:
    print("O número {0} é o maior".format(numero1))

else:
    print("O número {0} é o maior".format(numero2))

"""
import math

"""
#2
import math

numero = (float(input("Insira um número")))

if numero > 0:
    raiz = math.sqrt(numero)
    print("A raiz quadrada de {0} é {1}".format(numero, raiz))

else:
    print("O número informado é inválido")
"""
"""
#3

num = (float(input("Insira um número")))

if num > 0:
    raiz1 = math.sqrt(num)
    print("A raiz quadrada de {0} é {1}".format(num, raiz1))

else:
    potencia = num**2
    print("O quadrado de {0} é {1}".format(num, potencia))

"""
"""
#9

salario = (float(input("Insira seu salário")))

prestacao = (float(input("Insira o valor da prestação do empréstimo")))

if prestacao > (0.2 * salario):
    print("Empréstimo não concedido")

else:
    print("Empréstimo concedido")

"""

#10

altura = float(input("Insira a sua altura: \n"))

sexo = input("Insira o seu sexo, M ou F: \n")

if sexo == "M" or "m":
    imc = (72.7 * altura) - 58
    print("O seu peso ideal é {0}".format(imc))

elif sexo == "F" or "f":
    imc = (62.1 * altura) - 44.7
    print("O seu peso ideal é {0}".format(imc))
