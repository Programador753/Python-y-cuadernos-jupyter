Valor_limite = int(input("Introduzca valor limite positivo:"))
while Valor_limite <= 0:
  Valor_limite = int(input("Introduzca valor limite positivo por encima de 0:"))

print()
numero = float(input("Escriba un número: "))
suma = numero

while suma < Valor_limite:
  numero = float(input("Escriba otro número: "))
  suma += numero

print()
print("Ha superado el límite. La suma de los números introducidos es",suma)