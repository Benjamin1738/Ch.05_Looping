'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random
print("Welcome!")
print()
print("Your are in a car and on the run! The police are on your tail and are not stopping! Reach the safe house to "
      "outrun them!")
print("Check your Gas often, Check how close the police are, and dont forget your thirst levels! Your car can also"
      " break down, so check often! ")
# end of intro
print()
# start of loop
# done = False
# while not done:
# qut = input("Do you want to quit? type 'y'")
# if qut.lower() == "y":
#     quit()
# else:
#     print("Lets continue then.")

print("Your goal is to reach the safe house 100 miles away. (Refueling also gives a break")
# End of rules needed

done = False
miles = 0
thirst = 100
gallons = 30
police = -20
water = 3
while not done:
    print("--------------------------------------")
    print("A. Refuel")
    print("B. Status")
    print("C. Full Speed Ahead")
    print("D. Drink Water")
    print("E. Drive the speed limit ahead")
    print("Q. Quit")
    choice = input("Choice ->")
    if choice.lower() == "q":
        done = True
    elif choice.lower() == "b":
        print("Miles Traveled:", miles)
        print("Police are", police, "mile(s) behind")
        print("Gallons:", gallons, )
        print("Water left:", water, "bottle(s)")
    elif choice.lower() == "a":
        gallons += random.randint(1, 10)
        police += random.randint(5, 20)
        print("Refueled:", gallons)
        print("The Police are at", police, "mile(s)")
    elif choice.lower() == "c":
        miles += random.randint(15, 25)
        police += random.randint(4, 8)
        gallons -= random.randint(4, 8)
        print("You went full speed!")
    elif choice.lower() == "d":
        water -= 1
        print("Water consumed")
    elif choice.lower() == "e":
        miles += random.randint(6, 15)
        police += random.randint(1, 5)
        gallons -= random.randint(4, 6)
        print("You Drove the speed limit!")
    if miles >= 100:
        print("You escaped!")
        done = True
    if police == miles:
        print("The police caught you!")
        done = True
    if gallons <= 0:
        print("Ran out of gas! Game Over")
        done = True
if miles >= 20 and miles <= 25:
    print("You are thirsty!")
    if miles == 100:
        print("You escaped the police")
        done = True














