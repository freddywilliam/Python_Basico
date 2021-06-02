# El primer ciclo se encarga de ingresar los datos en la lista.
# El segundo ciclo se encarga en sumar los datos de la lista.
def operation(times):
    list = []
    for i in range(1, times):
        number = int(input(" Write the number: "))
        list.append(number)
    suma = 0
    for elemento in list:
        suma = suma + elemento
    return suma

def run():
    times = input("How many numbers you have? ")
    times = int(times) + 1
    print(operation(times))
if __name__ == '__main__':
    run()
