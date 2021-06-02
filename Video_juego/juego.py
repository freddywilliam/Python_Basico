import random

def run():
    
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("Ingresa numero: "))

    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("Mas alto")
            

        else:
            print("Mas bajo")
        numero_elegido = int(input("Ingresa otro numero: "))

    print("Ganaste!!")






if __name__ == '__main__':
    run()