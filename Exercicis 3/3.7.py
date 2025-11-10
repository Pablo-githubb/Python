def factorial(n):
    """
    Calcula el factorial d'un número n.
    n! = n × (n-1) × (n-2) × ... × 1
    """
    if n <= 1:
        return 1

    resultat = 1
    for i in range(2, n + 1):
        resultat *= i

    return resultat


def combinacions_repeticio(m, n):
    """
    Calcula les combinacions amb repetició.
    CR(m,n) = (m + n - 1)! / (n! × (m - 1)!)

    m: nombre de tipus diferents de pastissos
    n: nombre de pastissos a escollir
    """
    if m <= 0 or n < 0:
        return 0

    if n == 0:
        return 1

    numerador = factorial(m + n - 1)
    denominador = factorial(n) * factorial(m - 1)

    return numerador // denominador


def pastisseria():
    """
    Demana el nombre de tipus de pastissos i quants se'n volen escollir,
    i calcula de quantes maneres diferents es poden escollir.
    """
    print("=== COMBINACIONS AMB REPETICIÓ DE PASTISSOS ===\n")

    while True:
        try:
            m = int(input("Quants tipus diferents de pastissos hi ha? (m): "))

            if m <= 0:
                print("El número de tipus ha de ser positiu")
                continue

            n = int(input("Quants pastissos vols escollir? (n): "))

            if n < 0:
                print("El número de pastissos ha de ser zero o positiu")
                continue

            resultat = combinacions_repeticio(m, n)

            print(f"\nAmb {m} tipus de pastissos, escollint {n} pastissos:")
            print(f"Hi ha {resultat} maneres diferents de fer l'elecció\n")


        except ValueError:
            print("Entrada invàlida\n")
        except OverflowError:
            print("Els números són massa grans per calcuar-se\n")


if __name__ == "__main__":
    pastisseria()