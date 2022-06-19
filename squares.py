def run():
    print(buildlist())

def buildlist():

    return [i for i in range (1,100000) if i % 36 ==0]


if __name__ == '__main__':
    run()