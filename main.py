import random


words = ["apple", "horse", "pizza", "happy", "tiger"]


play_again = "yes"


print("let's play hangman!")
print("If you need a hint, just type help.")
print("To guess the entire word, type guess answer.")

while play_again == "yes":
    word = random.choice(words)
    guessed_word = ["_"] * len(word)
    lives = 6
    guessed_letters = []
    letters = list(word)
    hints = 3
    hints_list = []


    while lives > 0 and "_" in guessed_word:
        print("\nword:", " ".join(guessed_word))
        print("lives left:", lives)


        # get the player's guess
        try:
            guess = input("guess a letter: ").lower()
        except OSError:
            print("your coding environment does not support input().")
            break

        if guess == "guess answer":
            try:
                answer = input("guess the entire word: ").lower()
            except OSError:
                print("your coding environment does not support input().")
                break

            if answer == word:
                guessed_word = list(word)
            else:
                lives = 0
            break

        if guess == "help" and hints > 0:
            hint = random.choice(letters)
            while hint in hints_list:
                hint = random.choice(letters)
            hints_list.append(hint)
            print("hint: " + hint)
            hints = hints - 1

        elif guess == "help" and hints <= 0:
            print("You ran out of hints!")


        elif len(guess) != 1 or not guess.isalpha():
            print("not a valid guess. please enter a single letter.")
            continue


        if guess in guessed_letters:
            print("you already guessed that letter!")
            lives = lives - 1
            continue


        guessed_letters.append(guess)


        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            lives = lives - 1
            if guess != "help":
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
