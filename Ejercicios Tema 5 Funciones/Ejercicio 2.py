def bisiesto(t):
    return t % 400 == 0 or (t % 100 != 0 and t % 4 == 0)

fecha = int(input("Escriba un año: "))

if bisiesto(fecha):
    print("El año", fecha, "es un año bisiesto.")
else:
    print("El año", fecha, "no es un año bisiesto.")