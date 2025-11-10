def es_subcadena(cadena1, cadena2):
    return cadena2 in cadena1


def anterior_alfabetic(cadena1, cadena2):
    return min(cadena1, cadena2)

print(es_subcadena('subcadena', 'cadena'))        # True
print(anterior_alfabetic('kde', 'gnome'))         # 'gnome'


if __name__ == "__main__":
    es_subcadena("","")
    anterior_alfabetic("","")