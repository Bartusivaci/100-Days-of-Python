import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
selection = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if selection >= 3 or selection < 0:
    print("You entered an invalid number, You lose.")
else:
    print(game_images[selection])

    computer_selection = random.randint(0, 2)

    print("Computer chose:")
    print(game_images[computer_selection])

    if selection == 0 and computer_selection == 2:
        print("You win.")
    elif computer_selection == 0 and selection == 2:
        print("You lose.")
    elif computer_selection > selection:
        print("You lose.")
    elif selection > computer_selection:
        print("You win.")
    elif selection == computer_selection:
        print("Tie.")







