#! /usr/bin/env python3

# computer needs to make a choice
# choices need to be evaluated
# print out the result (who won)
import random

def main():
    """body of the game"""
    
    choice= input("Rock, Paper, or Scissors?\n>")
    botchoice= random.choice(["rock", "paper", "scissors"])

    choice= choice.lower() # validates input by forcing input to be lower case

    # uncomment these print functions to debug
    #print(choice)
    #print(botchoice)
    
    #create a score tracker and while loop for comparison
    #while score or botscore less than 3 - cont game
    #compare choices and determine winner
    #end game best two out of three with score comparison

    score = 0
    botscore = 0
    

    while score or botscore <= 3:

        #take care of incorrect input
        if choice not in ["rock", "paper", "scissors"]:
            print("You entered an invalid choice, you lose(r)!")
    
        #if tie
        if choice == botchoice:
            print("It's a tie!")
            return
    
        #satisfy combinations if user wins
        if botchoice == "rock" and choice == "paper":
            print ("You win! I chose rock")
            score += 1
            print ("\n Score ", + score + " to ", + botscore)
        elif botchoice == "paper" and choice == "scissors":
            print ("You win! I chose paper")
            score += 1
            print ("\n Score ", + score + " to ", + botscore)
        elif botchoice == "scissor" and choice == "rock":
            print ("You win! I chose scissors")
            score += 1
            print ("\n Score ", + score + " to ", + botscore)
        elif botchoice == "rock" and choice == "scissors":
            print ("I win! I chose rock")
            botscore += 1
            print ("\n Score ", + score + " to ", + botscore)
        elif botchoice == "paper" and choice == "rock":
            print ("I win! I chose paper")
            botscore += 1
            print ("\n Score ", + score + " to ", + botscore)
        elif botchoice == "scissor" and choice == "paper":
            print ("I win! I chose scissors")
            botscore += 1
            print ("\n Score ", + score + " to ", + botscore)


    # user picked scissors... did they win or lose?

    ### ADD MORE HERE

main()
