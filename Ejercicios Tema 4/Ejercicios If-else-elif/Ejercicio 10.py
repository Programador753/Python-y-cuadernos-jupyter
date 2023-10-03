print("Una Ecuacion de primer grado tiene esta estructura: Ax + B = 0 ")
print("LA FORMULA QUE RESUELVE LA ECUACION DE PRIMER GRADO ES: x = -b / a")

a = float(input("Escriba el valor del coeficiente a: "))
b = float(input("Escriba el valor del coeficiente b: "))

print(a,"x +",b,"= 0")

if a == b == 0:
    print("Todos los números son solución.")
elif a == 0:
    print("La ecuación no tiene solución.")
else:
    print("La ecuación tiene una solución: X =",(- b / a))