def run():
    my_list = [1,"hello",True,4.5]
    my_dict = {"firstname": "Jose", "lastname": "Delgado" }

    super_list = [
        {"firstname": "Jose", "lastname": "Delgado" },
        {"firstname": "Leo", "lastname": "Avila" },
        {"firstname": "kiko", "lastname": "Contreras"}
    ]

    super_dict = {
        "narutal_nums": [1,2,3,4,5],
        "integer_nums": [-1,-2,0,15,20],
        "floating_nums": [1.1,2.6,4.5,6.85]
    }
    for key, value in super_dict.items():
        print(key,"-",value)





if __name__ == '__main__':
    run()