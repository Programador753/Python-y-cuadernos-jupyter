#Este programa pide una cantidad de segundos y te la da en minutos y segundos 

#Declaro variables Tiempo solicitado y tiempo devuelto
Tiempo_solicitado = int(input("Escriba tiempo en segundos:"))
#Tiempo devuelto en minutos
Tiempo_Devuelto = float(Tiempo_solicitado/60)
#Imprimo en pantalla los dos resultados
print("Su tiempo en minutos es de:",Tiempo_Devuelto,"Minutos")
print("Su tiempo en segundos es de:",Tiempo_solicitado,"Segundos")