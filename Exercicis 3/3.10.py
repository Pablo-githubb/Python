def es_primer():
    while True:
        try:
            numero = int(input("Introdueix un número natural: "))

            if numero <= 1:
                print(f"{numero} NO és primer")
            else:
                es_primer = True

                for i in range(2, numero):
                    if numero % i == 0:
                        es_primer = False
                        break

                if es_primer:
                    print(f"{numero} és primer")
                else:
                    print(f"{numero} NO és primer")
                    break
        except ValueError:
            print("Introduix SOLAMENT un número enter")
            continue


if __name__ == "__main__":
    es_primer()
