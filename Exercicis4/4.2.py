def cadena():
    cadena = input("Introdueix una cadena: ")

    i = len(cadena) - 1  # Comença en l'últim caràcter

    while i >= 0:
        print(cadena[i])
        i -= 1


if __name__ == "__main__":
    cadena()
