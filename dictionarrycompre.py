def run():
    print(builddict())

def builddict():

    return {i: round(i**(1/2),3) for i in range (1,1001) }


if __name__ == '__main__':
    run()