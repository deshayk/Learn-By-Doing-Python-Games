  """
  Program notes (4/12/22):
  Having trouble with the loop. I need to give the user a chance to guess again during
  the while loop. Right now, all it does it take one guess and iterates through the loop
  multiple times with that one guess.
  """


from guessing_game import greeting, game, play_again

def main():
  greeting()
  game()
  play_again()
  
main()