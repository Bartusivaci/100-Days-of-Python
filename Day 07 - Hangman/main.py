import random
from  hangman_word_list import word_list
from hangman_stages import stages
from hangman_art import logo


print(logo)

chosen_word = random.choice(word_list)

word_length = len(chosen_word)

lives = 6

display = []
for letter in chosen_word:
    display.append("_")

print("".join(display))

end_of_game = False

while not end_of_game:

    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess


    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose. The word was {chosen_word}")

    print("".join(display))

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])