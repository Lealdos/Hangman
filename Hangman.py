import random
import os
import unicodedata

def word_random()->str:
    """
    This function create a list with the all the word of a file,
    pick a random word of that list and clean the word of special charater like ' ó,é,ú,í,á '
    -----
    Args:
        clean_word: is a str with the word that must be guessed
        f: is just a name for the file
        word: is a list with all the words of the file
    returns
    ------------
    This function return a str
    """
    word= []
    with open("./files/data.txt","r", encoding="utf-8") as f:
        [word.append(words.strip("\n")) for words in f]
        clean_word = random.choice(word)
    clean_word = ''.join(c for c in unicodedata.normalize('NFD', clean_word) if unicodedata.category(c) != 'Mn')
    return clean_word


def draw(message: int, random_word: str,lives: int ,character: str, hangman: list )->None:
    """
    This function show the message according to game moment
    ---------------------------------------------------------------
    Args:
        message: ID of the message
        random_word: word to guess
        lives: user lives
        character: imput character
        hangman: user progress
    returns
    ---------------------------------------------------------------
    this function return None
    """
    match message:
        case 1:
            print(f"\nYOU WIN! \nThe word is: {random_word}\n")
            print("__   _______ _   _   _    _ _____ _   _ ")
            print("\ \ / /  _  | | | | | |  | |_   _| \ | |")
            print(" \ V /| | | | | | | | |  | | | | |  \| |")
            print("  \ / | | | | | | | | |/\| | | | | . ` |")
            print("  | | \ \_/ / |_| | \  /\  /_| |_| |\  |")
            print("  \_/  \___/ \___/   \/  \/ \___/\_| \_/")
                                        
        case 2:
            print(f"\nYou already used this character: {character}\nlives: {lives}\n{hangman}")
        case 3:
            print(f"\nYou lose, word was:{random_word}\n")
            print('▄██   ▄         ▄██████▄       ███    █▄        ▄█             ▄██████▄          ▄████████         ▄████████')
            print('███   ██▄      ███    ███      ███    ███      ███            ███    ███        ███    ███        ███    ███')
            print('███▄▄▄███      ███    ███      ███    ███      ███            ███    ███        ███    █▀         ███    █▀')
            print('▀▀▀▀▀▀███      ███    ███      ███    ███      ███            ███    ███        ███              ▄███▄▄▄ ')
            print('▄██   ███      ███    ███      ███    ███      ███            ███    ███      ▀███████████      ▀▀███▀▀▀ ')
            print('███   ███      ███    ███      ███    ███      ███            ███    ███               ███        ███    █▄ ')
            print('███   ███      ███    ███      ███    ███      ███▌    ▄      ███    ███         ▄█    ███        ███    ███ ')
            print('▀█████▀        ▀██████▀       ████████▀       █████▄▄██       ▀██████▀        ▄████████▀         ██████████')

def guess(random_word:str)->str:
    """
    this function is the logic of hangman game
    ----------------
    Args:
        ramdon_word: word to be guess
        hangman: is the variable that full the gammer
        lives: count of lives of the gammer
        control_chain: used to transfort str to list for be easier of comparate
        x: the character input by the gammer
    retunrs
    ------------
    This function return message message of win or lose through call the function draw

    """
    hangman = []
    control_chain=[]
    control_chain = [n for n in random_word]
    lives = 5
    for i in range(len(random_word)):
        hangman.append("-")

    print(hangman)
    while True:
        if hangman == control_chain:
            os.system("cls")
            return draw(1,random_word,lives,x,hangman)
        find = False
        x = input("enter a letter: ")
        while True:
            if len(x) == 0 or x.isnumeric() or len(x)>1:
                os.system("cls")
                print("You can't enter empty chart, a number or longer the one character")
                print("lives: ",lives)
                print(hangman)
                x = input("enter a letter: ")
                os.system("cls")
            else: break

        x = x.lower()
        os.system("cls")
        if hangman.count(x)!=0:
            draw(2,random_word,lives,x,hangman)
            continue
        os.system("cls")
        for i,e in enumerate(control_chain):
            if x == e:
                hangman[i]= x
                find = True
        if find is False:
            lives-= 1
        if lives== 0:
            return draw(3,random_word,lives,x,hangman)
        print("Lives: ",lives)
        print(hangman)
     
def run()->None:
    """
    This function star the program
    --------------------
    Args:
        word_ramdon: function bring a word(str) from a file
        aletorio: is a str variable
        guess: is the hangman game
    returns None
    -----
    this function return None
    """
    print("¡Guess the word! \n You have 5 live")
    aleatorio = word_random()
    guess(aleatorio)

if __name__ == '__main__':
    run()
