#Rock, paper, and scissors game
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

choices_list = ["rock", "paper", "scissors"]

choice = int(input("What do you choose? 1 for rock, 2 for paper and 3 for scissors: "))

choice_user = "undefined"
if choice == 1:
    choice_user = "rock"
    choice_graphic = rock
elif choice == 2:
    choice_user = "paper"
    choice_graphic = paper
elif choice == 3:
    choice_user = "scissors"
    choice_graphic = scissors
else:
    print("Invalid choice")
    exit()

cpu_choice = random.choice(choices_list)

if cpu_choice == "rock":
    cpu_graphic = rock
elif cpu_choice == "paper":
    cpu_graphic = paper
elif cpu_choice == "scissors":
    cpu_graphic = scissors


print("Your choice:")
print(choice_graphic)
print("CPU choice:")
print(cpu_graphic)

if cpu_choice == "rock" and choice_user == "paper":
    print("You have won")
elif cpu_choice == "paper" and choice_user == "rock":
    print("You have lost")
elif cpu_choice == "rock" and choice_user == "scissors":
    print("You have lost")
elif cpu_choice == "scissors" and choice_user == "rock":
    print("You have won")
elif cpu_choice == "scissors" and choice_user == "paper":
    print("You have lost")
elif cpu_choice == "paper" and choice_user == "scissors":
    print("You have won")
else:
    print(f"CPU chooses {cpu_choice}")
    print("It's a tie!")
