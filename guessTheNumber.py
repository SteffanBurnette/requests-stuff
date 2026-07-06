# Number Guessing game
import random

secret_number = random.randint(1, 20)
print("I am thinking of a number between 1 and 20.`")

# The player has 6 chances to guess the corect number
for guesses_taken in range(1, 7):
    print("Take a guess:")
    guess = int(input(">"))

    if guess < secret_number:
        print("Your guess is too low.")
    elif guess > secret_number:
        print("Your guess is too high.")
    else:
        break # This condition is the correct guess

if guess == secret_number:
    print(f"Good job! You got it in {str(guesses_taken)} guesses!")
else:
    print(f"The number was {str(secret_number)}")