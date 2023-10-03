#Este programa solicita una distancia en pies y te la da en centimetros.

#Declaro variables Pies y Total
Pies = float(input("Introduzca distancia en Pies:") )
Total = float(Pies*12*2.54)
#Imprimo en pantalla la distancia en centimetros 
print("Su distancia es de:",Total,"cm")