import random


words = ["apple", "horse", "pizza", "happy", "tiger"]


play_again = "yes"


print("let's play hangman!")


while play_again == "yes":
    word = random.choice(words)
    guessed_word = ["_"] * len(word)
    lives = 6
    guessed_letters = []


    while lives > 0 and "_" in guessed_word:
        print("\nword:", " ".join(guessed_word))
        print("lives left:", lives)


        # get the player's guess
        try:
            guess = input("guess a letter: ").lower()
        except OSError:
            print("your coding environment does not support input().")
            break


        if len(guess) != 1 or not guess.isalpha():
            print("not a valid guess. please enter a single letter.")
            continue


        if guess in guessed_letters:
            print("you already guessed that letter!")
            continue


        guessed_letters.append(guess)


        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            lives = lives - 1
            print("letter not found!")


    if lives == 0:
        print("out of lives, game over!")
        print("the word was:", word)
    elif "_" not in guessed_word:
        print("word guessed, you've won!")
        print("the word was:", word)


    if lives > 0 or "_" in guessed_word:
        try:
            play_again = input("play again? (yes/no) ").lower()
        except OSError:
            break


        while play_again != "yes" and play_again != "no":
            play_again = input("invalid input. play again? (yes/no) ").lower()


print("thanks for playing!")
