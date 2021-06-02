
def conversor(tipo_peso, valor_dolar):
    peso = input("Cuantos pesos " + tipo_peso + "tienes?")
    dolares = tipo_peso / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("En dolares tienes: " + dolares)

Menu = 
"""
Argentinos = 1
Colombianos = 2
Mexicanos = 3

"""
opicion = int(input(menu))

if peso == 1:
    conversion("Argentinos", 65) 

elif peso == 2:
    conversion("Colombianos", 3875)

elif peso == 3:
    conversion("Mexicanos", 20)

else:
    print("Chupaloo!!")
