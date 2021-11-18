print("Calculadora da área de um trapézio. \n")

base1 = print(float(input("Insira a base menor:\n")))

while base1 <= 0.00:
  print("Número inválido!")
  base1 = print(float(input("Insira a base menor:\n")))


base2 = print(float(input("Insira a base maior:\n")))

while base2 <= 0.00:
  print("Número inválido!")
  base2 = print(float(input("Insira a base maior:\n")))


altura = print(float(input("Insira a altura:\n")))

area = ((base1 + base2)*altura)/2

print(area)