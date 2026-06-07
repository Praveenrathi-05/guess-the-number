# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui

secret_number = 0
num_guess = 0

# helper function to start and restart the game

def new_game():
    # initialize global variables used in your code here
    print ""
    global secret_number, num_guess
    secret_number = random.randrange(0,100)
    num_guess = 7 
    print "New game. Range is from 0 to 100"
    print "Number of remaining guesses is " + str(num_guess)

# define event handlers for control panel

def range100():
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game
    print ""
    global secret_number, num_guess
    secret_number = random.randrange(0,1000)
    num_guess = 10
    print "New game. Range is from 0 to 1000"
    print "Number of remaining guesses is " + str(num_guess)
    
def input_guess(guess):
    # main game logic goes here	
    global num_guess
    int_guess = int(guess)
    print ""
    print "Guess was " + guess
    num_guess -= 1
    print "Number of remaining guesses is " + str(num_guess)
    if secret_number == int_guess:
        print "Correct"
        new_game()
    elif num_guess == 0:
        print "You ran out of guesses. The number was " + str(secret_number)
        new_game()
    elif secret_number > int_guess:
        print "Higher!"
    else:
        print "Lower!"     
    
# create frame
frame = simplegui.create_frame("Guess Game", 300, 300)

# register event handlers for control elements and start frame
frame.add_input("Enter a number: ", input_guess, 100)
frame.add_button("Range 0 to 100", range100, 150)
frame.add_button("Range 0 to 1000", range1000, 150)
frame.add_button("New Game", new_game, 150)
frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
