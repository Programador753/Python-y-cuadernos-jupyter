print("Elija una figura geométrica:")
print("T) Triángulo")
print("C) Círculo")
respuesta = input("¿Qué figura quiere calcular (Escriba T o C)? ")

if respuesta == "T" or respuesta == "t":
    base = float(input("Escriba la base: "))
    altura = float(input("Escriba la altura: "))
    print("Un triángulo de base:",base,"y altura",altura,"tiene un área de",(base * altura / 2))
elif respuesta == "C" or respuesta == "c":
    radio = float(input("Escriba el radio: "))
    print("Un círculo de radio",radio,"tiene un área de",(3.141592*(radio**2)))