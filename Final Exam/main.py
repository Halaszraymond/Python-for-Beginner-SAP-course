import random


def word_list():
    with open("5_letter_words.txt", "r") as words:
        list_of_words = [word.strip() for word in words]
    return list_of_words


def random_word(list_of_words):
    word_choice = random.choice(list_of_words)
    return word_choice


def is_real_word(guess, list_of_words):
    if guess in list_of_words:
        return True
    return False


def check_guess(guessed_word, the_word):
    string = ""
    counter = 0
    for character in guessed_word:
        if guessed_word.count(character) > the_word.count(character) and character in the_word:
            if character == the_word[counter]:
                string += "X"
            else:
                for letter in the_word:
                    number = 0
                    if character == letter:
                        number += 1
                if number > 0:
                    string += "O"
                elif guessed_word[:counter+1].count(character) <= the_word.count(character):
                    string += "O"
                else:
                    string += "_"
        elif character == the_word[counter]:
            string += "X"
        elif character in the_word:
            string += "O"
        else:
            string += "_"
        counter += 1
    return string


def next_guess(list_of_words):
    guess = input("Please enter a guess: ").lower()
    while not is_real_word(guess, list_of_words):
        print("That's not a real word!")
        guess = input("Please enter a guess: ").lower()
    return guess


def play():
    wordlist = word_list()
    word_to_find = random_word(wordlist)
    guesses = 0
    while guesses <= 6:
        guess = next_guess(wordlist)
        guesses += 1
        print(check_guess(guess, word_to_find))
        if check_guess(guess, word_to_find) == "XXXXX":
            print("You won!")
            break
        if guesses == 6:
            print("You lost")
            print(f"The word was: {word_to_find}")
            break


play()
