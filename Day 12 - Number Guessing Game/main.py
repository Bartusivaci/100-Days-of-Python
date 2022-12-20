import random

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\n")

number = random.randint(1, 100)

attempts = 0
wrong_input = True
while wrong_input:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        attempts = 10
        wrong_input = False
    elif difficulty == "hard":
        attempts = 5
        wrong_input = False
    else:
        print("Please enter a valid answer.")

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")

    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You got it! The number was {number}")
        break
    elif guess > number:
        print("Too high.\nGuess again.")
        attempts -= 1
    elif guess < number:
        print("Too low.\nGuess again.")
        attempts -= 1

if attempts <= 0:
    print(f"You've run out of guesses. You lose. The number was {number}")