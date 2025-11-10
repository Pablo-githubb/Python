def buclefimaxmin():
    numeros = []

    while True:
        entrada = input("Introduix un número: ")
        if entrada == "fi":
            break
        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Entrada invàlida")

    if len(numeros) != None:
        maxims = max(numeros)
        minims = min(numeros)
        print(f"Màxims: {maxims}")
        print(f"Mínims: {minims}")
    else:
        print("Erros al mostrar dades")


buclefimaxmin()
