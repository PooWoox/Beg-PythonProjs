import random

secret_number = random.randint(1, 20)
win = 'No'

while win != 'Yes':
    guessed_number = int(input("Type your guess: "))

    if guessed_number > secret_number:
        print("Your guess was too high.")
    elif guessed_number < secret_number:
        print("Your guess was too low")
    else:
        win = 'Yes'
        print("You guessed correctly")