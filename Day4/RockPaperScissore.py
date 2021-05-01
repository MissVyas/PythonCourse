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

input1 = raw_input("Enter 0 for rock, 1 for paper and 2 for scissors: ")
games_print = [rock,paper,scissors]

if input1 not in [0,1,2]:
    print "Invalid input !!"
else:
   if str(input1) == "0":
    print rock
if str(input) == "1":
    print paper
if str(input1) == "2":
    print scissors

choice = random.randint(0,2)
if str(choice) == "0":
    print rock
if str(choice) == "1":
    print paper
if str(choice) == "2":
    print scissors

if input1 == '0' and choice == "2":
    print "You win!!"
if input1 == "1" and choice == "0":
    print "You win!!"
if input1 == "2" and choice == "1":
    print "You win!!"
if input1 == choice:
    print "Its a draw"
else:
    print "You lose!!"
