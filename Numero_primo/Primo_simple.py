def run():

    numero = int(input("Escriba el numero: "))
    contador = 0

    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1  
    
    if contador == 0:
        print("Es primo")            
    else:
        print("No es primo")
           
if __name__ == '__main__':
        run()



# def run():
#     contador = 0
#     import math
#     numero = int(input("Escribe un numero: "))
#     numero_raiz = int(math.sqrt(numero))
#     if numero == 2 or numero == 3:
#         print("Es primo")

#     for i in range(1, numero_raiz + 1):
#         if numero % i == 0:
#             contador += 1
#             break

#     if contador >= 2:
#         print("No es primo")
       

# if __name__ == '__main__':
#     run()



