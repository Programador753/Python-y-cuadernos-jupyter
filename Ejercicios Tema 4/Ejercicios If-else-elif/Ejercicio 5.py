dividendo = int(input("Escriba el dividendo: "))
divisor = int(input("Escriba el divisor: "))

if dividendo % divisor == 0:
  print("La división es exacta. Cociente:",dividendo // divisor,)
else:
  print("La división no es exacta. Cociente:",dividendo // divisor,"Resto:",dividendo % divisor,)