def numeroapocaliptic():
    while True:
        try:
            numero = int(input("Introduix un número natural: "))

            if numero < 0:
                print("El número ha de ser natural (positiu)")
                continue
            else:
                # Convertim el número a cadena per buscar "666"
                numero_str = str(numero)

                if any(pattern in numero_str for pattern in
                       ["666", "111", "222", "333", "444", "555", "777", "888", "999"]):
                    print(f"El número {numero} és de l'apocalipsi")
                else:
                    print(f"El número {numero} NO és de l'apocalipsi")
                    break

        except ValueError:
            print("Entrada invàlida. Introdueix un número enter")

numeroapocaliptic()
