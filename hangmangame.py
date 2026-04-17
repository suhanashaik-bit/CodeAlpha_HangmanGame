import random

def hangman():
    words = ["apple", "tiger", "chair", "table", "plant"]
    word = random.choice(words)   
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman Game!")

    while attempts > 0:
        display = ""

       
        for letter in word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "

        print("\nWord:", display)

        
        if "_" not in display:
            print("You won! ")
            break

        guess = input("Enter a letter: ").lower()

      
        if guess in guessed_letters:
            print("Already guessed!")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Wrong guess! Attempts left:", attempts)
        else:
            print("Correct!")

    if attempts == 0:
        print("You lost! The word was:", word)


hangman()