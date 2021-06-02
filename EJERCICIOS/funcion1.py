def text(name):
    
    user = name.upper()
    if user == 'SARA':
        print("Hola!! mi nombre es " + user.capitalize() + " Mucho gusto!")
    else:
        print("Quien eres?")

def run():

    name = input("Escribe nombre: ")
    text(name)
    
if __name__ == '__main__':
    run()