def buclefi():
    total = 0
    count = 0

    while True:
        entrada = input("Introduix un número: ")
        if entrada == "fi":
            break
        try:
            numero = float(entrada)
            total += numero
            count += 1
        except ValueError:
            print("Entrada invàlida")

    if count > 0:
        mitjana = total / count
        print(int(total), count, mitjana)


buclefi()
