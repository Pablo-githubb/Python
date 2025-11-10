def puntuacio():
    while True:
        try:
            puntuacio = float(input("Introduix puntuació: "))

            if puntuacio < 0.0 or puntuacio > 1.0:
                print("puntuació incorrecta")
            elif puntuacio >= 0.9:
                print("excel·lent")
            elif puntuacio >= 0.8:
                print("notable")
            elif puntuacio >= 0.7:
                print("bé")
            elif puntuacio >= 0.6:
                print("suficient")
            else:  # puntuacio < 0.6
                print("insuficient")

        except ValueError:
            print("puntuació incorrecta")


puntuacio()