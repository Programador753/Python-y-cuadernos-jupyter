from random import randint
Valor_a = randint (2,11)
Valor_b = randint (2,11)

Respuesta = int(input("¿Cual es el resultado de %d x %d ?" %(Valor_a, Valor_b) ))

if Respuesta == Valor_a * Valor_b:
  print("La respuesta es correcta")
else:
  print("La respuesta es incorrecta")
