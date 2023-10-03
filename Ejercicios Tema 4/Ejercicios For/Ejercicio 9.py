Multiplicaciones = int(input("Número de multiplicaciones a plantear: "))
if Multiplicaciones < 1:
  print("El número de multiplicaciones a plantear debe ser al menos 1.")
else:
  for _ in range(Multiplicaciones):
    print()
    from random import randint
    Valor_a = randint (2,11)
    Valor_b = randint (2,11)

    Respuesta = int(input("¿Cual es el resultado de %d x %d ?" %(Valor_a, Valor_b) ))

    if Respuesta == Valor_a * Valor_b:
      print("La respuesta es correcta")
    else:
      print("La respuesta es incorrecta")