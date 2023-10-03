valores = int(input("¿Cuántos valores va a introducir? "))
if valores < 0:
    print("¡Imposible!")
else:
    pares = 0
    for i in range(1, valores + 1):
        numero = int(input("Escriba el valor %s:" %i))
        if numero % 2 == 0:
            pares += 1
    print("Ha escrito",pares,"números pares y",(valores - pares),"números impares.")