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


import random

###USER_SIDE###

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

if user_choice == 0:
  print(rock)

elif user_choice == 1:
  print(paper)

elif user_choice ==2:
  print(scissors)

else:
  print("You typed an invalid number. You lose!")

###COMPUTER_SIDE###

computer_choice = random.randint(0, 2)

if user_choice >= 3 or user_choice < 0:
  print()

elif computer_choice == 0:
  print(f"Computer chose: {rock}")

elif computer_choice == 1:
  print(f"Computer chose: {paper}")

else:
  print(f"Computer chose: {scissors}")

###RESULT###

if user_choice == 0 and computer_choice == 0:
  print("It's a draw. Try again!") 

elif user_choice == 0 and computer_choice == 1:
  print("You lost.") 

elif user_choice == 0 and computer_choice == 2:
  print("You win! Congrats :D") 

if user_choice == 1 and computer_choice == 0:
  print("You win! Congrats :D") 

elif user_choice == 1 and computer_choice == 1:
  print("It's a draw. Try again!") 

elif user_choice == 1 and computer_choice == 2:
  print("You lost.")

if user_choice == 2 and computer_choice == 0:
  print("You lost.")

elif user_choice == 2 and computer_choice == 1:
  print("You win! Congrats :D") 

elif user_choice == 2 and computer_choice == 2:
  print("It's a draw. Try again!") 


###ANSWER_RESULT###

# if user_choice >= 3 or user_choice < 0:
#   print("You typed an invalid number, you lose!")

# elif user_choice == 0 and computer_choice == 2:
#     print("You win!")

# elif computer_choice == 0 and user_choice == 2:
#   print("You lose.")

# elif computer_choice > user_choice:
#   print("You lose.")

# elif user_choice > computer_choice:
#   print("You win!")

# elif computer_choice == user_choice:
#   print("It's a draw. Try again :D")