from karel.stanfordkarel import *

"""
When you finish writing this file, Karel should be able to 
place 20 beepers, then 24 beepers, and end facing East to 
the right of the 24 beepers.
"""

def main():
    for i in range(20):
        put_beeper()
    move()
    for i in range(24):
        put_beeper()
    move()    



 

if __name__ == '__main__':
    main()