import random

# List of words for the game
word_list = ["python", "hangman", "programming", "computer", "developer"]

def choose_random_word(word_list):
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word_to_guess = choose_random_word(word_list)
    guessed_letters = []
    attempts = 6  # Number of incorrect attempts allowed

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))

    while True:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        if guess.isalpha() and len(guess) == 1:
            guessed_letters.append(guess)
            if guess not in word_to_guess:
                attempts -= 1

            print(display_word(word_to_guess, guessed_letters))

            if "_" not in display_word(word_to_guess, guessed_letters):
                print("Congratulations! You guessed the word: " + word_to_guess)
                break

            if attempts == 0:
                print("Sorry, you're out of attempts. The word was: " + word_to_guess)
                break
        else:
            print("Please enter a valid single letter.")

if __name__ == "__main__":
    hangman()
