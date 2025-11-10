def comptador():
    # Programa principal
    cadena = input("Introdueix una cadena: ")
    lletra = input("Introdueix una lletra a comptar: ")

    # Calcula el número de vegades que surt la lletra que tu demanes
    comptar = cadena.count(lletra)

    print(f"La lletra '{lletra}' apareix {comptar} vegades a '{cadena}'")


if __name__ == "__main__":
    comptador()
