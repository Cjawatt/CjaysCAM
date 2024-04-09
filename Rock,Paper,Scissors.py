print("Hello would you like to play Rock,paper,scissors )")
response = input("Yes or no?: ")


if response == "yes":
    print("Okay have fun")

if response == "no":
    print("Get Out My Face!!! if u dont wanna play go away then")
    quit()



def statement_generator(statement, decoration):
    print(f"{decoration * 5} {statement} {decoration * 5}")

def instructions():
    print("Instructions go here...")

def instructions():
    statement_generator("instructions","-")

    print('''
-pick either rock/paper/scissors
-if you pick rock and the bot picks scissors you win
-if you pick paper and the bot picks rock you win
-if you pick scissors and the bot picks paper you win
-if u do the same one u both tie    
and if the other away around then the bot wins 
GOOD LUCK!!:

''')

want_instructions = input("press <enter> to read the instructions"
                          "or any key then <enter> to continue: ")

if want_instructions == "":
    instructions()


import random

options = ("Paper", "Scissors", "Rock",)
player_options = ("Rock", "Paper", "Scissors", "Dragon", "James")
running = True
while running:
    player = None
    computer = random.choice(options)



    while player not in player_options:
        player = input("Enter either rock, paper, scissors or the secret one?: ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("A TIE")

    elif player == "Rock" and computer == "Scissors":
        print("you have won!")
    elif player == "Paper" and computer == "Rock":
        print("you have won!")
    elif player == "Scissors" and computer == "Paper":
        print("you have won!")
    elif player == "Dragon" and computer == "Paper":
        print("you have won!")
    elif player == "Dragon" and computer == "Rock":
        print("you have won!")
    elif player == "Dragon" and computer == "Scissors":
        print("you have won!")
    elif player == "James" and computer == "Paper":
     print("you have won!")
    elif player == "James" and computer == "Rock":
        print("you have won!")
    elif player == "James" and computer == "Scissors":
        print("you have won!")
    elif player == "Mr Pearse" and computer == "Paper":
        print("you have won!")
    elif player == "Mr Pearse" and computer == "Rock":
        print("you have won!")
    elif player == "Mr Pearse" and computer == "Scissors":
        print("you have won!")


    else:
        print("you have lost skill issue loser")

    if not input("press Yes if u wanna continue playing: ").lower() == "yes":
        running = False
        print("Thank you for playing")