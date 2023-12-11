#simple truth or dare game implementing the conditional and random



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

#Write your code below this line 👇

choice=int(input("what u want to choose? 0 for rock , 1 for paper,2 for scissors"))

comp_choice=random.randint(0,2)
print(f"computer chose {comp_choice}")
if choice > comp_choice:
  print("you win")
elif comp_choice==choice:
  print("draw")
else:
  print("comp win")
  
