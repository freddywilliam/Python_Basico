Menu =
"""
 Bienvenid@ a mi kokoro.
 ❤❤❤❤❤❤❤❤❤❤❤❤❤condicion
"""

valor_dolar_colombianos = 3875
valor_dolar_mexicanos = 20

peso = float(input("Ingresa cuantos pesos tienes: "))
tipo_peso = str(input("Mexicano (1) o Colombiano (2): "))

if tipo_peso == "1":
    dolares_mexicanos = peso / valor_dolar_mexicanos
    dolares_mexicanos = str(round(dolares_mexicanos, 2))
    print("En dolares tienes: " + dolares_mexicanos)

elif tipo_peso == "2":
    dolares_colombianos = peso / valor_dolar_colombianos
    dolares_colombianos =str(round(dolares_colombianos, 2))
    print("En dolares tienes: " + "$ " + dolares_colombianos)



