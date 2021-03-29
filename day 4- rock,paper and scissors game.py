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

choice_list = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor "))
user_choice = choice_list[choice]
import random
computer_choice = random.randint(0, 2)
computer_choice_output = choice_list[computer_choice]
if computer_choice_output == rock and user_choice == paper :
  print(user_choice)
  print(f"Computer chose :\n {computer_choice_output}")
  print("You Win!")
elif computer_choice_output == paper and user_choice == scissors :
  print(user_choice)
  print(f"Computer chose :\n {computer_choice_output}")
  print("You Win!")
elif computer_choice_output == scissors and user_choice == rock :
  print(user_choice)
  print(f"Computer chose :\n {computer_choice_output}")
  print("You Win!")
else :
  print(user_choice)
  print(f"Computer chose :\n {computer_choice_output}")
  print("You Loose!")