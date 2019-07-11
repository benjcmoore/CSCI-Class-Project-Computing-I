print("I am thinking of a number between 1 and 100.");
print("Make a guess and I will tell you if you")
print("are too high, too low, or got it right. ")
print("You've got 10 attempts.")

import random

attempts = 1

x = random.randint(1,100)

guess = int(input("Enter your Number: "))

while x != guess and attempts < 10:

    if guess < x:
        print("To Low")
    elif guess > x:
        print("To High")
    guess = int(input("Enter your Number: "))
    attempts += 1

if attempts == 10:
    print("\nSorry you've reached your maximum number of tries.")
    print("The number was ",x)

else:
    print("\nYou are correct! The number was " ,x)
    print("You got it in ", attempts,"attempts")

input("\n\nPress the enter key to exit")