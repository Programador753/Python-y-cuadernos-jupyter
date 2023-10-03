def rectangulo(ancho, alto):
    for i in range(alto):
        for j in range(ancho):
            print("* ", end="")
        print()

anchura = int(input("Anchura del rectángulo: "))
altura = int(input("Altura del rectángulo: "))
rectangulo(anchura, altura)