def calculasalari():
    hores = input("Introduix el número d'hores: ")
    tarifa = input("Introduix Tarifa: ")
    salari = float(hores) * float(tarifa)
    print(f"Salari: {round(salari)}")
calculasalari()