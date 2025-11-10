def calculasalarirefinat():
    try:
        hores = float(input("Introduix les Hores: "))
        tarifa = float(input("Introduix la Tarifa per hora: "))
    except ValueError as e:
        print("Error, per favor introduix un número")
        return
    else:
        if hores > 40:
            restahores = hores - 40
            novatarifa = (restahores * tarifa) * 1.5
            salari = (((hores - restahores) * tarifa) + novatarifa)
            print(f"Salari: {round(salari)}")
        else:
            salari = hores * tarifa
            print(f"Salari: {round(salari)}")


if __name__ == "__main__":
    calculasalarirefinat()
