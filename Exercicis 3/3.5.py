def es_triangular(numero):
    """
    Comprova si un número és triangular sumant 1+2+3+... fins trobar-lo.
    """
    if numero <= 0:
        return False

    suma = 0
    n = 1

    while suma < numero:
        suma += n
        n += 1

    if suma == numero:
        print(f"El número {numero} és triangular")
    else:
        print(f"El número {numero} no és triangular")

    return suma == numero


es_triangular(6)
