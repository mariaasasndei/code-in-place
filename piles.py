from karel.stanfordkarel import *

# File: piles.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel
# pick up all the beepers in the world.
def main():
  move()
  while beepers_present():
     pick_beeper()
  move()
  while beepers_present():
     pick_beeper()
  move()
  while beepers_present():
     pick_beeper()
  move()
  while beepers_present():
     pick_beeper()
  move()
  while beepers_present():
     pick_beeper()
  move()

    # your code here
   
   
   
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()