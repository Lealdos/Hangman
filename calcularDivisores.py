def div(num):
        return [i if num % i ==0 else 0 for i in range(1,num+1)]
       

def run():
    while True:
        try:
                num = int(input("ingresa un numero: "))
                if num<0:
                    raise ValueError("ingresa un numero positivo mayor a 0")
                print(div(num))
                break
        except ValueError as nn:
                print(nn)


if __name__ == '__main__':
    run()