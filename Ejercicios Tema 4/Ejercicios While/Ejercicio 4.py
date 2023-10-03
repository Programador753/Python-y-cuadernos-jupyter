minimo = int(input("Escriba un número: "))
maximo = int(input("Escriba un número mayor que %d:" %minimo))
while minimo >= maximo:
  maximo = int(input(" %d no es mayor que %d . Inténtelo de nuevo: " % (maximo, minimo)))

print()
numero = float(input("Escriba un número entre %d y %d :" % (minimo, maximo)))
contador = 0

while minimo <= numero and numero <= maximo:
     contador += 1
     numero = float(input("Escriba otro número entre %d y %d :" % (minimo, maximo)))

print()
if contador == 0:
  print("No ha escrito ningún número entre %d y %d :" % (minimo, maximo))
elif contador == 1:
  print("Ha escrito 1 número entre %d y %d :" % (minimo, maximo))
else:
  print("Ha escrito",contador,"números entre %d y %d." % (minimo, maximo))