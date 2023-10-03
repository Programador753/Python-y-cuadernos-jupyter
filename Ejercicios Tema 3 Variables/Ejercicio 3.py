#Este programa solicita una distancia en pies y pulgadas y te la da en centimetros

#Declaro las variables Pies, Pulgadas
Pulgadas = float(input("Introduzca distancia en Pulgadas:") )
Pies = float(input("Introduzca distancia en Pies:"))
#Declaro una variable que almacenara el resultado de la distancia pasada a centimetros
Total = float(((Pies*12)+Pulgadas)*2.54)
#Imprimo en pantalla el total de la distancia en Centimetros
print("Su distancia es de:",Total,"cm")