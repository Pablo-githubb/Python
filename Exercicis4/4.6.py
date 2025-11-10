def cadena_find():

    cad = 'X-DSPAM-Confidence: 0.8475 Km'

    """
    .strip() elimina els espais en blanc
    .find(:) troba la posició dels dos punts
    """
    numero = float(cad[cad.find(':') + 1 : cad.find('Km')].strip())

    print(numero)  # 0.8475

if __name__ == "__main__":
    cadena_find()