
def run():
    
    book_name = str(input("What is the name of the book?: "))
    book_pages = int(input("How many pages has?: "))
    book_days_hours = int(input("How many hours you read in one day?: "))
        
    if book_pages >= 300:
        print("Tu libro " + str(book_name) + " es grande.")
    else:
        print("Tu libro " + str(book_name) + " es corto")
    if book_days_hours > 1:
        print("Lo deberias acabar en 6 dias")
    else:
        print("Lo deberias acabar en menos de 3 dias")

if __name__ == '__main__':
    run()