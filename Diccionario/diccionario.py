def run():
    # mi_diccionario = {
    #     'llave1' : 1,
    #     'llave2' : 2,
    #     'llave3' : 3,

    # }
    # print(mi_diccionario['llave1'])
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3'])

 poblacion_paises = {
    'Argentina' : 10000,
    'Peru': 5555555
    
    }

#  print(poblacion_paises['Argentina'])

 for pais, poblacion in poblacion_paises.items():
    print(pais + " tiene " + str(poblacion) + " habitantes. ")


if __name__ == '__main__':
    run()
