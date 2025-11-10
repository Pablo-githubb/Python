from cloudinit.handlers import call_end
from samba.netcmd.domain.auth.silo import cmd_domain_auth_silo_delete


def insertar_caracter_cadena():
    cadena = input("Introduix una cadena: ")
    caracter = input("Introduix una caracter: ")

    # La cadena indicada "," sintercala per cada caracter de la cadena "pablo" = "p,a,b,l,o
    print(caracter.join(cadena))


def substituir_caracteres():
    cadena = input("Introduix una cadena per substituir: ")
    caracter = input("Introduix una caracter per substituir: ")

    print(caracter.join(cadena).strip(" "))

def substiuir_digits():
    clau = input("Introduix la clau: ")
    caracter = input("Introduix una caracter: ")

    for i in range(len(clau)):
        print(caracter.)





def afegir_caracteres():
    cadena = input("Introduix una cadena: ")
    caracter = input("Introduix una caracter: ")
    print(caracter.join(len(cadena[:3])))

if __name__ == "__main__":
    insertar_caracter_cadena()
    substituir_caracteres()
    substiuir_digits()
    afegir_caracteres()
