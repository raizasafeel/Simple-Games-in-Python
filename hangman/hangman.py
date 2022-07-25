words = ['ten', 'twenty', 'capitalism', 'list', 'auspicious', 'neville goddard', 'peter petigrinne', 'light switch', 'contemplation', 'aesthetic', 'neverland', 'Sarah Bullocks', 'anhorrent', 'conspicuous', 'candlelight']
import random
import string

def get_valid_word(words):
    word = random.choice(words) #randomly chooses sth from list
    while '-' in word or ' ' in word: word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    limit = 5
    word_letters = set(word) # letters in the word saved as set
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what user has guessed


    while len(word_letters) > 0 and limit > 0:

        #used letter print
        print("you have used these letters: ", ' '.join(used_letters))

        #what current word is with dashes
        word_list = [letter if letter in used_letters else ' __ ' for letter in word]
        print('current word: ', ' '.join(word_list))

        user_letter = input("Enter a letter: ").upper()

        if user_letter in alphabet - used_letters: # if new letter
            used_letters.add(user_letter) # add to used letters
            if user_letter in word_letters: word_letters.remove(user_letter) # if in word, remove the word
            else:
                limit -= 1
                print(f"you've got {limit} lives left 0.0")

        elif user_letter in used_letters: print("you already used that -_-")
        else:
            print("Invalid character, pls try again") # wrong letter


    if limit > 0: print('YOU WON')
    else: print("HANGMAN IS HANGED")


hangman()

