par = int(input("Introduzca un numero par:") )

if par % 2 == 1:
  print("El valor no es par")
else:
  impar = int(input("Escriba un número impar: "))
  if impar % 2 == 0:
    print("El numero no es impar")
  else:
    exit