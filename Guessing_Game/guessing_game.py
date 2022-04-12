"""
Learn by Doing - Guessing Game by DeShay K.
Github: https://github.com/deshayk
Medium: https://www.medium.com/@deshayk
LinkedIn: https://www.linkedin.com/in/deshayk/
"""

import random #import random module

def greeting(): #program greeting
  print("Hello! Welcome to the Guessing Game!")
  print("The instructions are simple:")
  print("I'm going to tell you a number range and you're going to guess what number I'm thinking of.")
  print("Try to guess the correct number in five or less attempts.")
  print("Ready? Let's begin!")
  print("\n")

def game(): # program tells user if guess is too high or too low
  print("I'm thinking of a number between 1 and 100.")
  print("\n")
  computer_number = random.randint(1, 100) #computer generates a random number between 1 and 100
  guess_count = 0 #user guesses the number 
  user_guess = 0 
  while user_guess != computer_number: #while user guess is not equal to computer number
    user_guess = int(input("What number am I thinking of?: ")) #user guesses the number, overwriting default value
    if user_guess > computer_number: #if user guess is greater than computer number
      guess_count += 1
      print("Your guess is too high. Try again.") # if user guess is too high, program prints "Too high. Guess again."
      print("You have " + str(guess_count) + " round(s) of guessing.")
      print("\n")
    else:
      guess_count += 1
      print("Your guess is too low. Try again.") # if user guess is too low, program prints "Too low. Guess again."
      print("You have " + str(guess_count) + " round(s) of guessing.")
      print("\n")
  print("You guessed the number!")
  print("It only took you " + str(guess_count) + " round of guessing. Congratulations!")
        
#asks if user wants to play again
def play_again():
  play_again = input("Would you like to play again? (y/n)")
  print("\n")
  if play_again == "y" or play_again == "Y": #if user wants to play again, program restarts
    greeting()
    game()
  else: #if user does not want to play again, program prints "Thanks for playing!" and exits
    print("Thanks for playing!")

if __name__ == "__main__":
  greeting()
  game()
  play_again()