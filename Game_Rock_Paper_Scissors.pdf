#Game of Rock-Paper-scissors

def replay():
    return input("Do you want to play again (Y/N) : ").lower().startswith('y')

import random

Game = ['Rock', 'Paper', 'Scissors']

Computer_choice = random.choice(Game)

n = Computer_choice

user_score = 0
computer_score = 0
tie = 0

print('Welcome to the Game of Rock - Paper - Scissors')


start = True


while(start) :
    print("\n enter your choice \n")
    player = input(" Rock, Paper, Scissors, Exit :\t")
    x = player.title()
    print(" ")
    if (x == 'Exit') :
        start = False
        break
    elif (x == n) :
        tie += 1
        print(" It's a TIE!")
    elif (x == "Rock") :
        if (n == "Paper") :
            print('Computer Wins! as Paper covers Rock')
            computer_score += 1
        if (n == "Scissors") :
            print('You Wins! as Rock crushes Scissors')
            user_score += 1
    elif (x == "Paper") :
        if (n == "Scissors") :
            print('Computer Wins! as Scissors cuts Paper')
            computer_score += 1
        if (n == "Rock") :
            print('You Wins! as Paper covers Rock')
            user_score += 1  
    elif (x == "Scissors") :
        if (n == "Rock") :
            print('Computer Wins! as Rock crushes Scissors')
            computer_score += 1
        if (n == "Paper") :
            print('You Wins! as Scissors cuts Paper') 
            user_score += 1
    else :
        print("That's not a valid play!")
    
    print(" ")
    print(" ")

    print("Scoreboard : ")
    print("Tie : ", tie)
    print("Player : ", user_score)
    print("Computer : ", computer_score)    
    print(" ")
    print(" ")

print(" ")
print(" ")
print("Thankyou for playing\n")

if (user_score > computer_score) :
    print("Player wins! :) ")
else :
    print("Computer wins! :) ")


print("Do you want to play again ?  ")
replay()
