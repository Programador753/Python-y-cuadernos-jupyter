valores = int(input("¿Cuántos valores va a introducir? "))
if valores < 1:
    print("¡Imposible!")
else:
    primero = int(input("Escriba un número: "))
    for i in range(valores - 1):
        numero = int(input("Escriba un número más grande que %d:" %primero))
        if numero <= primero:
            print("¡ %d no es mayor que %d!" % (numero, primero) )