import random
import os
import sys
import unicodedata

def word_random():
     word = []
     with open("./files/data.txt","r", encoding="utf-8") as f:
         character = dict.fromkeys (c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
         [word.append(unicodedata.normalize('NFD',words.strip("\n"))) for words in f]
     palabra = random.choice(word)
     palabra = "".join(palabra)
     return palabra.translate(character)

def draw(messege,random_word,lives,charater,hangman):

    match messege:
        case 1:
            print(f"YOU WIN! \nThe word is: {random_word}")
        case 2:
            print(f"You already used this character: {charater}\nlives: {lives}\n{hangman}")
        case 3:
            print(f"You lose, word was:'{random_word}'")




def guess(random_word):
    hangman = []
    control_chain=[]
    control_chain[:0] = random_word 
    lives = 5
    for i in range(len(random_word)):
        hangman.append("-")

    print(hangman)
    while True:
        if hangman==control_chain:
            os.system("cls")
            draw(1,random_word,lives,x,hangman)
            break
        find=False
        x = input("enter a letter: ")
        x = x.lower()
        os.system("cls")
        if hangman.count(x)!=0:
            draw(2,random_word,lives,x,hangman)
            continue
        os.system("cls")
        for i in range(len(control_chain)):
            if x==control_chain[i]:
                hangman[i]= x
                find = True
        if find==False:
            lives-=1
        if lives==0:
            draw(3,random_word,lives,x,hangman)
            break
    
        print("Lives: ",lives)
        print(hangman)
        
 
def run():
    print("¡Guess the word! \n You have 5 live")
    aleatorio = word_random()
    guess(aleatorio)

if __name__ == '__main__':
    run()
