import random

print("""
                            ♀ Hangman Game ♀

In this game, you'll be trying to guess the letters of a hidden word. But beware! 
Each incorrect guess brings the hangman closer to being fully drawn.
You have a limited number of attempts to guess the correct letters before the hangman is complete. 
The game ends when you either guess the word or the hangman is fully drawn.

Hint: The word is related to a type of flower.
Good luck! ☺
——————————————————————————————————————————————————————————————————————————————————————————————————
""")


flowers = ['rose', 'tulip', 'daisy', 'lily', 'orchid', 'sunflower', 'marigold', 'iris',
           'daffodil', 'violet', 'jasmine', 'lotus', 'lavender', 'poppy', 'hibiscus']

word = random.choice(flowers)
guessed_letters = []
attempts = 6


def hangman_display(attempt):
    if attempt == 6:
        return ("  ╒════╗\n"
                "       ║\n"
                "       ║\n"
                "       ║\n"
                "       ╩")
    if attempt == 5:
        return ("  ╒════╗\n"
                "  O    ║\n"
                "       ║\n"
                "       ║\n"
                "       ╩")
    if attempt == 4:
        return ("  ╒════╗\n"
                "  O    ║\n"
                " /     ║\n"
                "       ║\n"
                "       ╩")
    if attempt == 3:
        return ("  ╒════╗\n"
                "  O    ║\n"
                " /|    ║\n"
                "       ║\n"
                "       ╩")
    if attempt == 2:
        return ("  ╒════╗\n"
                "  O    ║\n"
                " /|\\   ║\n"
                "       ║\n"
                "       ╩")
    if attempt == 1:
        return ("  ╒════╗\n"
                "  O    ║\n"
                " /|\\   ║\n"
                " /     ║\n"
                "       ╩")
    if attempt == 0:
        return ("  ╒════╗\n"
                "  O    ║\n"
                " /|\\   ║\n"
                " / \\   ║\n"
                "       ╩")


while attempts > 0:
    print(hangman_display(attempts))
    print(f"Attempts you have: {attempts}")
    display_word = ' '.join([letter if letter in guessed_letters else '_' for letter in word])
    print("Word:", display_word)

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You've already guessed that letter! Try again.")
        print("—————————————————————————————————")
        continue
    else:
        guessed_letters.append(guess)

    if guess in word:
        print("Good guess! Keep going.")
    else:
        attempts -= 1
        print("Wrong guess!Try again.")

    if all(letter in guessed_letters for letter in word):
        print(f"Congratulations! You've guessed the word: {word}")
        break
    print("—————————————————————————————————")

else:
    print(hangman_display(attempts))
    print(f"Game over! The word was: {word}")
