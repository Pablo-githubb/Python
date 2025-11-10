import random


def algorismedau():
    contador = 0

    for i in range(100):
        # Genera un número entre 1 i 6
        dau = random.randint(1, 6)
        # Pot sortir: 1, 2, 3, 4, 5 o 6

        # Genera 0 o 1
        moneda = random.randint(0, 1)
        # 0=creu, 1=cara

        if dau % 2 != 0 and moneda == 1:
            contador += 1

    print(f"Ha sortit número senar i cara: {contador} vegades")


if __name__ == "__main__":
    algorismedau()
