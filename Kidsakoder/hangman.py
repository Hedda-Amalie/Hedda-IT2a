from random import choice

word = choice(["code", "clutch", "spin", "magenta", "curious", "height"])

guessed = []
wrong = []

tries = 7

while tries > 0:
    out = ""
    for letter in word:
        if letter in guessed:
            out = out + letter
        else:
            out = out + "_"

    if out == word:
        break

    print("Guess a letter in the word:", out)
    print(tries, "Try again")

    guess = input()

    if guess in guessed or guess in wrong:
        print("The letter has already been guessed:", guess)
    elif guess in word:
        print("Yay")
        guessed.append(guess)
    else:
        print("Nope")
        tries = tries - 1
        wrong.append(guess)

    print()

if tries:
    print("You guessed!", word)
else:
    print("You guessed right!!!", word)