def algorsmewallis():
    while True:
        try:
            termes = int(input("Introduix el número de termes: "))
        except ValueError:
            print("Entrada invàlida. Introdueix un número enter")
            continue
        else:
            producte = 1.0

            for i in range(1, termes + 1):
                numerador = 4 * i * i
                denominador = (4 * i * i) - 1
                producte *= numerador / denominador

            pi_aproximat = producte * 2

            print(f"Aproximació de pi amb {termes} termes: {pi_aproximat}")
            print(f"Valor real de pi: 3.141592653589793")
            print(f"Error: {abs(3.141592653589793 - pi_aproximat)}")
            break


algorsmewallis()
