from threading import main_thread
from unicodedata import name
from unittest.main import MAIN_EXAMPLES
from pip import main


DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]




def run():
    all_pythondevs = list(filter(lambda worker: worker["language"]=="python", DATA))
    all_pythondevs =list(map(lambda worker:worker["name"], all_pythondevs))
    all_platziworker = list(filter(lambda worker:worker["organization"]=="Platzi",DATA))
    all_platziworker =list(map(lambda worker:worker["name"],all_platziworker))
    adults = list(filter(lambda worker: worker["age"]>=18, DATA ))
    adults = list(map(lambda worker:worker["name"], adults))
    
    old_people = list(map(lambda worker: worker |{"old": worker['age']>=70}, DATA))
    for worker in all_platziworker:
        print(worker)


if __name__ == '__main__':
    run()

