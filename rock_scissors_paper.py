import random

# Rock, Paper and Scissors (ASCII DRAWING)

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

list = [rock, paper, scissors]


#Score counters for the player and computer
my_score = 0
computer_score = 0

while True:
    selection = input("Enter your selection (rock, paper, scissors, 'q') = ")
    computer_selection = random.choice(list)


    #If user wants to quit the game
    if selection == "q":
        print("Quit the game...")
        break
    #Check if the user's input is valid
    if selection not in ["rock","paper","scissors"]:
        print("Invalid Value....")
    #Player chooses rock, computer chooses scissors → player wins
    elif(selection == "rock" and computer_selection == scissors):
        print(rock,"\nrock","\t", scissors,"\nscissors")
        print("the rock broke the scissors")
        my_score += 1
    #Player chooses rock, computer chooses paper → computer wins
    elif (selection == "rock" and computer_selection == paper):
        print(rock,"\nrock", "\t\t\t", paper,"\npaper")
        print("the paper wrap the rock")
        computer_score += 1
    # Player chooses scissors, computer chooses rock → computer wins
    elif (selection == "scissors" and computer_selection == rock):
        print(scissors,"\nscissors","\t\t\t", rock, "\nrock")
        print("the rock broke the scissors")
        computer_score += 1
    #Player chooses scissors, computer chooses paper → player wins
    elif (selection == "scissors" and computer_selection == paper):
        print(scissors,"\nscissors","\t\t\t", paper,"\npaper")
        print("the scissors cut the paper")
        my_score += 1
    #Player chooses paper, computer chooses rock → player wins
    elif (selection == "paper" and computer_selection == rock):
        print(paper,"\npaper", "\t\t\t", rock,"\nrock")
        print("the paper wrap the rock")
        my_score += 1
    #Player chooses paper, computer chooses scissors → computer wins
    elif (selection == "paper" and computer_selection == scissors):
        print(paper,"\npaper","\t\t\t",scissors,"\nscissors")
        print("the scissors cut the paper")
        computer_score += 1
    #Any other case → draw
    else:
        print(selection,"\t\t\t",computer_selection)
        print("draw")

    print("My score is = ", my_score, "Computer score is = ", computer_score)
#Results
if(my_score > computer_score):
    print("I win")
elif(my_score < computer_score):
    print("Computer win")
else:
    print("Draw")