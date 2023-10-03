numero = int(input("¿Cuántos valores va a introducir? "))

if numero <= 0:
   print("¡Imposible!")
else:
   suma = 0
   for i in range(1, numero + 1):
       valor = float(input("Escriba el número %d:" %i))
       suma = float(suma + valor)
   print("La suma de los números que ha escrito es %f" %suma)