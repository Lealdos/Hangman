import os

def run():
    palabrita = "leer"
    ahorcado =""
    count= 0
    letra = []
    while count<5:
        letra= input("Ingrese un caracter: ")
        ahorcado+= letra
        os.system("cls")
        print("palabra que va: ",ahorcado, " \n vidas: ",count)
        if ahorcado == palabrita:
            return True
        elif count>4:
            return False
        else:
            if letra!=palabrita[::1]:
                count=+1

    


if __name__ == '__main__':
    print(run())