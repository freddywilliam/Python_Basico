
def conversor(tipo_peso, valor_dolar):
    peso = input("Cuantos pesos " + tipo_peso + " tienes?: ")
    peso = float(peso)
    dolares = peso / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("En dolares tienes: " + dolares)

menu = """
Argentinos = 1
Colombianos = 2
Mexicanos = 3

Elige """

opcion = int(input(menu))

if opcion == 1:
    conversor("Argentinos", 65) 

elif opcion == 2:
    conversor("Colombianos", 3875)

elif opcion == 3:
    conversor("Mexicanos", 20)

else:
    print("Chupaloo!!") 
