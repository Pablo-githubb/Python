def conversorCaF():
    celsius = input("Introduix els graus ºC: ")
    fahrenheit = (float(celsius) * (9/5)) + 32
    print(f"Els {celsius}ºC convertits a ºF són: {fahrenheit}")
conversorCaF()