numero = int(input("Escriba un número entero mayor que 1: "))

if numero <= 1:
   print("¡Le he pedido un número entero mayor que 1!")
else:
   contador = 0
   for i in range(1, numero + 1):
       if numero % i == 0:
          contador = contador + 1
   if contador == 2:
       print("%d es primo." %numero)
   else:
       print("%d no es primo." %numero)