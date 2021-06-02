def run():
    LIMITE = 1000000

    contador = 0
    potencia_dos = 2**contador

    while potencia_dos < LIMITE:
        print("2 Elevado a " + str(contador) + " es igual a " + str(potencia_dos))
        contador = contador + 1
        potencia_dos = 2**contador

    


if __name__ == '__main__':
    run()