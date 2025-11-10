def calculasalari2():
    hores = float(input("Introduix les Hores: "))
    tarifa = float(input("Introduix la Tarifa per hora: "))

    if hores > 40:
        restahores = hores - 40
        novatarifa = (restahores * tarifa) * 1.5
        salari = (((hores - restahores) * tarifa) + novatarifa)
        print(f"Salari: {round(salari)}")
    else:
        salari = hores * tarifa
        print(f"Salari: {round(salari)}")


calculasalari2()
