peso = input("Ingresa cuantos pesos tienes: ") 
peso = float(peso)
valor_dolar_colombianos = 3875
dolares_colombianos = peso / valor_dolar_colombianos
dolares_colombianos = round(dolares_colombianos, 2)
dolares_colombianos = str(dolares_colombianos)
print("Tienes $" + dolares_colombianos + " dolares")

