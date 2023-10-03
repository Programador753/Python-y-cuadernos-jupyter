numero = int(input("¿Cuántos valores va a introducir? "))
if numero <= 0:
    print("¡Imposible!")
else:
    valor = float(input("Escriba el número 1: "))
    minimo = maximo = suma = valor
    for i in range(2, numero + 1):
        valor = float(input("Escriba el número %d :" %i))
        suma = suma + valor
        if valor < minimo:
            minimo = valor
        if valor > maximo:
           maximo = valor
    print("El número más pequeño de los introducidos es %f " %minimo)
    print("El número más grande de los introducidos es %f " %maximo)
    print("La media de los números introducidos es %f" %(suma / numero))