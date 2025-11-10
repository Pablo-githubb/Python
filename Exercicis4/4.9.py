def nomes_consonants(cadena):
    vocals = "aeiouàèéíòóúïüAEIOUÀÈÉÍÒÓÚÏÜ"
    return ''.join([c for c in cadena if c.isalpha() and c not in vocals])


def nomes_vocals(cadena):
    vocals = "aeiouàèéíòóúïüAEIOUÀÈÉÍÒÓÚÏÜ"
    return ''.join([c for c in cadena if c in vocals])


def es_palindrom(cadena):
    cadena_neta = ''.join([c.lower() for c in cadena if c.isalpha()])
    return cadena_neta == cadena_neta[::-1]

nomes_consonants("supercalifagilistocoespialidoso")
nomes_vocals("")
es_palindrom("")
