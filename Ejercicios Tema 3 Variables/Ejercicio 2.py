#Este programa lo que hace es solicitar al usuario sus datos de peso y altura para calcular su imc

#Las siguientes variables son de tipo float para poder meter los datos con decimales
Peso = float(input("Introduzca su peso en Kilogramos:") )
Altura = float(input("Introduzca su altura en metro:") )
#La siguiente linea opera la formula del imc 
imc = (Peso/(Altura**2))

print("Su imc es de:",imc,)