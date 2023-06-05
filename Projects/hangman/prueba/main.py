import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letras en la palabra
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # Lo que el usuario ha adivinado

    while len(word_letters) > 0:

        print('Tu has elegidos estas letras: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Palabra actual: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print('Ya introduciste ese caracter. Por favor intenta nuevamente')

        else:
            print('Caracter Invalido. Por favor intenta nuevamente')

hangman()