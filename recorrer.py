def run(string,ending):
    return string[-len(ending):]==ending or len(ending)==0
        



if __name__ == '__main__':
    print(run("leonardo","do"))
    print(run("daniel","l"))
    print(run("angel","diego"))
    print(run("leon",""))


