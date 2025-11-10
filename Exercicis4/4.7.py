def cada_dos_caracters(cadena):
    """
    Retorna una cadena extraient cada dos caràcters.
    """
    return cadena[::2]  # Des del principi, saltant de 2 en 2


def cadena_inversa(cadena):
    """
    Retorna la cadena concatenada amb ella mateixa invertida.
    """
    return cadena + cadena[::-1]

print(cada_dos_caracters("recta"))      # 'rca'
print(cada_dos_caracters("programació")) # 'pormció'

print(cadena_inversa("reflex"))         # 'reflexxelfer'
print(cadena_inversa("hola"))           # 'holaaloh'


if __name__ == "__main__":
    cadena_inversa("")