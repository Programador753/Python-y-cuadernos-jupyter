numero_1 = float(input("Escriba un número: "))
numero_2 = float(input("Escriba otro número: "))
numero_3 = float(input("Escriba otro número más: "))

if (numero_1 == numero_2 != numero_3 or numero_1 == numero_3 != numero_2 or numero_2 == numero_3 != numero_1):
  print("Ha escrito uno de los números dos veces.")
elif numero_1 == numero_2 == numero_3:
  print("Ha escrito tres veces el mismo número.")
else:
  print("Los tres números que ha escrito son distintos.")