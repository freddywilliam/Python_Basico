def run():
    # for contador in range(0, 1001):
    #     if contador % 2 != 1:
    #         continue
    #     print(contador)

    # for i in range(0, 1000):
    #     print(i)
    #     if i == 500:
    #         break

    texto = input("Escribe: ")
    for letra in texto:
         if letra == "o":
            break
         print(letra)




if __name__ == '__main__':
    run()