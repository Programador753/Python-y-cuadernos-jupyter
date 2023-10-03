#Escriba un programa que pida una cantidad y que escriba cuántas gruesas, docenas y unidades son
print ("Escriba una cantidad (entera): ")
#Declaro Variables
cantidad=int(input())
gruesas=cantidad/144
restogruesas=cantidad%144
docenas=restogruesas/12
restodocenas=restogruesas%12
#Imprimo resultado en pantalla
print ('%s unidades son %s gruesas, %s docenas y %s unidades' % (str(cantidad), str(gruesas), str(docenas), str(restodocenas)))