def es_perfecte():
    numero = int(input("Introdueix un número natural: "))

    suma = 0

    for i in range(1, numero):
        if numero % i == 0:
            suma += i

    if suma == numero:
        print(f"{numero} és perfecte")
    else:
        print(f"{numero} NO és perfecte")

if __name__ == "__main__":
    es_perfecte()