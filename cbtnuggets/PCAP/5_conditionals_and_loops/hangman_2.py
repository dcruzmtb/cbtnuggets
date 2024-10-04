import random

wordlist = ["acceptance", "theorist", "overwhelm", "pollution", "asylum", "chauvinist", "dignity", "ignorance", "forestry", "triangle"]
max_tries = 5
current_tries = 0
wrong_tries = 0
word = wordlist[random.randint(0,9)]
guessed_letters = []

word_inprogress = []
for letter in word:
    word_inprogress.append("_")

def print_word(word_to_print):
    for letter in word_to_print:
        print(letter,end=" ")
    print()

def check_letter(guessed_letter):
    found_letter = False
    for i in range(0,len(word)):
        if(word[i] == guessed_letter):
            word_inprogress[i] = guessed_letter
            found_letter = True
    if found_letter:
        return True
    
def guessed_already(guessed_letter):
    for i in range(0,len(guessed_letters)):
        if(guessed_letters[i] == guessed_letter):
            return True
    return False

print("Welcome to Hangman!")
print("You will have 5 wrong tries to guess the word.\n")

while wrong_tries < max_tries:
    print_word(word_inprogress)
    print(f"Current tries: {current_tries}")
    print(f"Current wrong tries: {wrong_tries}")
    print("Guessed Letters: ", end='')
    print_word(guessed_letters)

    current_guess = input("Guess a letter: ")
    current_guess = current_guess.lower()
    current_tries += 1

    while True:
        if guessed_already(current_guess):
            current_guess = input("You guessed that already! Guess a new letter: ")
            current_guess = current_guess.lower()
        else:
            guessed_letters.append(current_guess)
            break
    
    if not check_letter(current_guess):
        wrong_tries += 1

    if word == ''.join(word_inprogress):
        print(f'You win! The word is {word}. You got it in {current_tries} tries with {wrong_tries} wrong tries!')
        exit()
    print()

print(f'Game over. You lost. The word was {word}.')