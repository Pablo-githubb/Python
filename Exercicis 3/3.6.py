def es_triangular(numero):
    """
    Determina si un número es pot apilar triangularment.
    Un número triangular és de la forma: n * (n + 1) / 2
    """
    if numero <= 0:
        return False

    suma = 0
    n = 1

    while suma < numero:
        suma += n
        n += 1

    return suma == numero


def es_quadrat(numero):
    """
    Determina si un número es pot apilar en forma quadrada.
    Un número quadrat és de la forma: n²
    """
    if numero <= 0:
        return False

    arrel = int(numero ** 0.5)
    return arrel * arrel == numero


def piles_llaunes():
    """
    Demana un número de llaunes i determina si es poden apilar
    triangularment, quadradament, ambdues formes, o cap.
    """
    while True:
        try:
            numero = int(input("Introdueix el número de llaunes: "))

            if numero < 0:
                print("El número ha de ser natural (positiu o zero)")
                continue

            triangular = es_triangular(numero)
            quadrat = es_quadrat(numero)

            if triangular and quadrat:
                print(f" {numero} llaunes es poden apilar TRIANGULARMENT i QUADRADAMENT")
                continue
            elif triangular:
                print(f"{numero} llaunes es poden apilar només TRIANGULARMENT")
                continue
            elif quadrat:
                print(f"{numero} llaunes es poden apilar només QUADRADAMENT")
                continue
            else:
                print(f"{numero} llaunes NO es poden apilar ni triangular ni quadradament")
                break

        except ValueError:
            print("Entrada invàlida")


if __name__ == "__main__":
    piles_llaunes()