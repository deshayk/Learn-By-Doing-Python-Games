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
  user_guess = int(input("What number am I thinking of?: "))
  print("\n")
  computer_number = random.randint(1, 100) #computer generates a random number between 1 and x (user input)
  guess_count = 0 #user guesses the number  
  while user_guess != computer_number and guess_count <= 5: #while user guess is not equal to computer number
    if user_guess > computer_number: #if user guess is greater than computer number
      guess_count += 1
      print("Your guess is too high. Try again.") # if user guess is too high, program prints "Too high. Guess again."
      print("You have " + str(guess_count) + " guess(es) in total.")
      print("\n")
    elif user_guess < computer_number:
      guess_count += 1
      print("Your guess is too low. Try again.") # if user guess is too low, program prints "Too low. Guess again."
      print("You have " + str(guess_count) + " guess(es) in total.")
      print("\n")
    else:
      guess_count += 1
      print("You have " + str(guess_count) + " guess(es) in total.")
      print("\n")
      if user_guess == computer_number:
        guess_count += 1
        print("You guessed the correct number!") #if user guess is correct, program prints "You got it! The number was " + number
      elif guess_count >= 2 and guess_count <= 4:
        print("Congrats! It only took you " + str(guess_count) + " guesses.")
      elif guess_count >= 4 and guess_count <= 5:
        print("Phew! It was a close game, it took you " + str(guess_count) + " guesses.")
        print("But a victory is still a victory!")
      else:
        print("You have guessed the number wrong more than five times. The correct number was " + str(computer_number) + ".")
        print("Better luck next time!")
        
#asks if user wants to play again
def play_again():
  play_again = input("Would you like to play again? (y/n)")
  if play_again == "y" or play_again == "Y": #if user wants to play again, program restarts
    greeting()
    game()
  else: #if user does not want to play again, program prints "Thanks for playing!" and exits
    print("Thanks for playing!")