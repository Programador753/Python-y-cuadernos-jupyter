numero_1 = int(input("Escriba el primer numero:"))
numero_2 = int(input("Escriba el segundo numero:"))

while numero_1 >= numero_2:
  numero_2 = int(input("Vuelva a escribir el numero dos de manera qque sea mayor que el numero uno:"))
print("Los numeros que has escrito son:",numero_1,"y",numero_2)