import random

options = ("Rock" , "Paper" , "Scissors")
running = True

while running == True:
    player = None
    Computer = random.choice(options)

    while player not in options:
        player = input("Enter a Choice(Rock , Paper , Scissors):")

    print(f"Player: {player}")
    print(f"Computer: {Computer}")

    if player == Computer:
        print("It's a Tie!")
    elif player == "Rock" and Computer == "Scissors":
        print("You Win the Game!")
    elif player == "Paper" and Computer == "Rock":
        print("You Win the Game!")
    elif player == "Scissors" and Computer =="Paper":
        print("You Win the Game!")
    else:
        print("You Lost the Game!")
    if not input("Play again? (y/n): ").lower()== "y":
        running = False
print("Thanks for Playing this Game!")