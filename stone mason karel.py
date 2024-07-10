from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def column():
    while no_beepers_present() and front_is_clear():
        put_beeper()
        move()

def distance():
    move()
    move()
    move()
    move()
def main():
    turn_left()
    column()
    put_beeper()
    turn_right()
    distance()
    turn_right()
    column()
    put_beeper()
    turn_left()
    distance()
    turn_left()
    column()
    put_beeper()
    turn_right()
    distance()
    turn_right()
    column()
    put_beeper()
    turn_left()
if __name__ == '__main__':
    main()