def comptadorlletres(cadena, lletra):
    vegades = 0

    for caracter in cadena:
        if caracter == lletra:
            vegades += 1

    return vegades


# Programa principal
cadena = input("Introdueix una cadena: ")
lletra = input("Introdueix una lletra a comptar: ")

resultat = comptadorlletres(cadena, lletra)

print(f"La lletra '{lletra}' apareix {resultat} vegades a '{cadena}'")

if __name__ == "__main__":
    comptadorlletres("pablo","o")
