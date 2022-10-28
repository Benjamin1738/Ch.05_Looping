'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly chooses a 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.(1 for rock, 2 for paper, 3 for scissors and 4 for quit)
I don't want to be asked to quit each time. I will enter a 4 if I want to quit.
Add conditional statements to figure out who wins and keep the records
Each round tell me what the computer chose, what I chose and also if I won, lost or tied.
When the user quits print an end game message and their win/loss/tie record

'''

import random
done = False
computer_score = 0
player_score = 0
print("Press 4 to quit")
while not done:

    player = input("Rock, Paper, or Scissors?")
    if player.lower() == "rock" or player == "1":
        print("You Picked rock!")
    if player.lower() == "paper" or player == "2":
        print("You Picked Paper!")
    if player.lower() == "scissors" or player == "3":
        print("You Picked Scissors!")

    print()
    print("Lets see what the computer picked!")
    num = random.randint(1, 3)
    if num == 1:
        print("Computer Picked Rock!")
    if num == 2:
        print("Computer Picked Paper!")
    if num == 3:
        print("Computer Picked Scissors!")

    print("Lets See who won!")
    print()
    if num == 3 and player.lower() == "scissors":
        print("Tie!")
    if num == 2 and player.lower() == "paper":
        print("Tie!")
    if num == 1 and player.lower() == "rock":
        print("Tie!")

    if num == 1 and player.lower() == "paper":
        player_score += 1
        print("You Win with Paper!")
    if num == 1 and player.lower() == "scissors":
        computer_score += 1
        print("Computer Wins with Rock!")

    if num == 2 and player.lower() == "rock":
        computer_score += 1
        print("Computer wins with Paper!")
    if num == 2 and player.lower() == "scissors":
        player_score += 1
        print("You won with Scissors!")

    if num == 3 and player.lower() == "rock":
        player_score += 1
        print("You Won with rock!")
    if num == 3 and player.lower() == "paper":
        computer_score += 1
        print("Computer won with Scissors!")
    if player == "4":
        print("Computer Won", computer_score,"Times")
        print("Player Won", player_score,"Times")
        quit()
    print()
    print("------------------------------------------------------")













