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
# Rock, Paper, Scissors Project By Parthiv Abhani

print("Welcome to Rock, Papers or Scissors!")
print("")


comp_count = 0
user_count = 0

while (comp_count < 5) and (user_count < 5):

    user = int(input("Type 0 for rock, 1 for paper or 2 for scissors: "))
    print("")

    comp = random.randint(0,2) 
    if user == 0 and comp == 0:
        print("You chose:")
        print(rock)
        print("Computer chose:")
        print(rock)
        print("Draw.")
        print(f"Computer points: {comp_count} You: {user_count}")

    elif user == 1 and comp == 1:
        print("You chose:")
        print(paper)
        print("Computer chose:")
        print(paper)
        print("Draw.")
        print(f"Computer points: {comp_count} You: {user_count}")

    elif user == 2 and comp == 2:
        print("You chose:")
        print(scissors)
        print("Computer chose:")
        print(scissors)
        print("Draw.")
        print(f"Computer points: {comp_count} You: {user_count}")

    elif user == 0 and comp == 1:
        print("You chose:")
        print(rock)
        print("Computer chose:")
        print(paper)
        print("Computer wins a point!")
        comp_count += 1
        print(f"Computer points: {comp_count} You: {user_count}")

    elif user == 0 and comp == 2:
        print("You chose:")
        print(rock)
        print("Computer chose:")
        print(scissors)
        print("You win a point!")
        user_count += 1
        print(f"Computer points: {comp_count} You: {user_count}")

    elif user == 1 and comp == 0:
        print("You chose:")
        print(paper)
        print("Computer chose:")
        print(rock)
        print("You win a point!")
        user_count += 1
        print(f"Computer: {comp_count} You: {user_count}")

    elif user == 1 and comp == 2:
        print("You chose:")
        print(paper)
        print("Computer chose:")
        print(scissors)
        print("Computer wins a point!")
        comp_count += 1
        print(f"Computer: {comp_count} You: {user_count}")

    elif user == 2 and comp == 0:
        print("You chose:")
        print(scissors)
        print("Computer chose:")
        print(rock)
        print("Computer wins a point!")
        comp_count += 1
        print(f"Computer: {comp_count} You: {user_count}")

    elif user == 2 and comp == 1:
        print("You chose:")
        print(scissors)
        print("Computer chose:")
        print(paper)
        print("You win a point!")
        user_count += 1
        print(f"Computer: {comp_count} You: {user_count}")

    elif user >= 3 or user <=0:
        print("Invalid Number!")
        print("")


if comp_count == 5:
    print("Computer wins the game!")
else:
    print("You win the game!")

print('\nGame Over! Press the "run" button to play again.\n')
