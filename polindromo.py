def polindromo(stri):
    try:
        if len(stri) == 0 or  stri[::1] ==" ":
            raise ValueError("No puede ingresar una cadena vacia")    
        return stri==stri[::-1]
    except ValueError as ve:
        print(ve)
        return False

def run():
    try:
        cadena = input("ingresa un string: ")
        print(polindromo(cadena))
    except TypeError:    
        print("solo puedes ingresar caracteres")
    

if __name__ == '__main__':
    run()
