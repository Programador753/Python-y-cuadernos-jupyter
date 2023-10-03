print("El programa empieza pidiendo entre qué números está el número a adivinar, se un número al azar y después el usuario va probando valores y el programa va diciendo si son demasiado grandes o pequeños.")
minimo = int(input("Ingrese el valor mínimo:"))
maximo = int(input("Ingrese el valor máximo:"))

print()
print("El valor mínimo es:",minimo)
print("El valor máximo es:",maximo)
print()
print("He pensado un número del",minimo,"al",maximo,"intenta adivinarlo.")
print()


from random import randint
aleatorio = randint (minimo,maximo)

numero = int(input("Ingrese el primer número:"))

while numero != aleatorio:

  if aleatorio > numero:
    print("El número que has ingresado es demasiado pequeño")
    numero = int(input("Ingrese otro número:"))
    
  else:
    print("El número que has ingresado es demasiado grande")
    numero = int(input("Ingrese otro número:"))

print("El numero es correcto")