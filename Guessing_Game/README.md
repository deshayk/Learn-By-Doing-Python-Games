# Guessing Game

## Directions
### Step 1: Write Psuedo Code
Sample psuedo code in the Python Programming Language is as follows:

#program greeting
#program asks user to input a number for the range of the random number
#computer generates a random number between 1 and 100 
#computer tells user if guess is too high or too low
#if user guess is too high, program prints "Too high. Guess again."
#if user guess is too low, program prints "Too low. Guess again."
#if user guess is correct, program prints "You got it! The number was " + number 

### Step 2: Create Program Greeting (optional)
The program should greet the user, welcoming them to the game and giving game instructions. The program should print messages that welcomes the user and gives them game instructions.

### Step 3: Program Generates Random Number
The program should generate a random number using random.randint() and stores the random number in a variable. The program should include user input and the random.randint() method.

### Step 4: User Guesses Random Number
The program will prompt the user to guess a number by taking their input and storing that input in a variable.

### Step 5: Program compares user guess to generated random number
The program will compare the user's guess to the number it generated to check if the number guessed is correct.

### Step 6: Program prints comparison
The program will tell the user if their guess is too high or too low based on a comparison between what the user guessed and the random number the program generated. If the user's guess is greater than the generated number, the program prints a too high message. If the user's guess is less than the generated number, the program prints a too low message.

### Step 7: User guesses again
If the user's guess was too high or too low, they will guess again.

### Step 8: Repeat steps 6-8 until correct guess 
The user will continue guessing a number until they guess the correct number.

### Step 9: Print congradulations message
When the user successfully guesses the correct number, a congradulations message will be printed to the screen.

### Step 10: Ask user if they would like to play again (optional)   
Once the user successfully finishes as guessing game, they will be prompted asking if they would like to play again. If the player wants to play again, the game reboots. If the player doesn't want to play again, the program gives an exit message and the game ends.