def run():

    dinero = input("Cuanto dinero tienes?: ")
    dinero = int(dinero)
    sandia = 0
    PRECIO = 2
    PRECIO_DOS = 1

    while dinero >= PRECIO:
        sandia = sandia + 1  
        dinero = dinero - PRECIO
        print("Compre " + str(sandia) + " sandias")
        print("Me queda " + str(dinero) + " bitcoins")
        if dinero == PRECIO_DOS:
            print("Me compre 1/2 sandias")
        if sandia == 5:
            break
        print("Se acabaron las sandias")
            
        


if __name__ == '__main__':
    run() 