#!/usr/bin/env python3

import turtle
import random

s = turtle.Screen()
t = turtle.Turtle()

"""
This module contains functions related to drawing and moving a circle around the screen
"""

__author__ = 'Debbie Johnson'
__version__ = '1.0'
__copyright__ = "Copyright 2022.02.17, Chapter 4 Assignment"
__github__ = "https://github.com/dejohns2/CSC365_Spring2022_Code_Examples"

# position where the turtle will be drawn at
# these values will change by plus/minus 20 as arrows are pressed
x = 0  # center of screen moving right or left
y = 0  # center of screen moving up or down

"""
s = None
t = None
"""

num_moves = 0
circle_size = 100
move_size = 100

previous_x = 0
previous_y = 0

hidden_x = 0
hidden_y = 0

user_color = 'red'
hidden_color = 'black'


def set_hide_locate():
    global hidden_x, hidden_y

    while True:
        hidden_x = random.randint(-420, 420)
        hidden_y = random.randint(-300, 300)

        if abs(hidden_x) > (circle_size * 2 + 10) and abs(hidden_y) > (circle_size * 2 + 10):
            break


def center_locate():
    global x, y

    center_pos = int(circle_size / 2) * -1

    x = center_pos
    y = center_pos


def set_circle_color():

    global previous_x, previous_y, user_color, hidden_color

    overlap = circle_size * 2 - 10

    if abs(x - hidden_x) < overlap and abs(y - hidden_y) < overlap:
        hidden_color = 'green yellow'
        user_color = 'green'
    else:
        if previous_x != x:
            if abs(previous_x - hidden_x) > abs(x - hidden_x):
                user_color = 'red'
            else:
                user_color = 'blue'

    previous_x = x
    previous_y = y


def debug():
    global hidden_color
    if hidden_color == 'black':
        hidden_color = 'grey'
    else:
        hidden_color = 'black'


def display_hidden_circle():
    # draw circle
    t.penup()
    t.goto(hidden_x, hidden_y)  # move to the updated x (left-right) and y (up-down) location from center
    t.pendown()  # start drawing the outline of the circle
    t.pencolor(hidden_color)
    t.fillcolor(hidden_color)  # fill color of the circle
    t.begin_fill()  # start the fill of whatever is being drawn
    t.circle(circle_size)  # diameter of the circle
    t.end_fill()


def display_instructions():
    # write text on the screen
    t.penup()  # don't want to see icon moving on the screen
    t.goto(-350, 350)  # from the current position which is center after clear, move left 350 up 350
    t.pencolor('white')  # text color
    t.write("Use arrows to move, or press 'h' for home", font=("Verdana", 12, "bold"))
    t.goto(-350, 335)
    t.write("Press 'd' for debug, or press 'r' to reset", font=("Verdana", 12, "bold"))
    """
    t.goto(-350, 320)
    t.write("Current number of moves: ", num_moves, font=("Verdana", 12, "bold"))
    """


def display_user_circle():
    # draw circle
    t.penup()
    t.goto(x, y)  # move to the updated x (left-right) and y (up-down) location from center
    t.pendown()  # start drawing the outline of the circle
    t.pencolor(user_color)
    t.fillcolor(user_color)  # fill color of the circle
    t.begin_fill()  # start the fill of whatever is being drawn
    t.circle(circle_size)  # diameter of the circle
    t.end_fill()


def display_game():
    t.clear()
    set_circle_color()
    display_hidden_circle()
    display_user_circle()
    display_instructions()


def move_home():
    """
    Reset the x and y back to zero coordinate which will be used position the circle in the center
    then call draw_circle to clear & redraw the circle is on the screen based on its new location

    Returns:
        None
    """

    center_locate()
    display_game()


def move_left():
    """
    Subtract 20 from the x coordinate which will be used move the circle to the left
    then call draw_circle to clear & redraw the circle is on the screen based on its new location

    Returns:
        None
    """

    global x, num_moves
    x -= move_size  # move to the left of center
    num_moves += 1
    display_game()


def move_right():
    """
    Add 20 to the x coordinate which will be used move the circle to the right
    then call draw_circle to clear & redraw the circle is on the screen based on its new location

    Returns:
        None
    """

    global x, num_moves
    x += move_size  # move to the right of center
    num_moves += 1
    display_game()


def move_up():
    """
    Add 20 to the y coordinate which will be used move the circle up
    then call draw_circle to clear & redraw the circle is on the screen based on its new location

    Returns:
        None
    """

    global y, num_moves
    y += move_size  # move top of center
    num_moves += 1
    display_game()


def move_down():
    """
    Subtract 20 from y coordinate which will be used move the circle to the down
    then call draw_circle to clear & redraw the circle is on the screen based on its new location
    Returns:
        None
    """

    global y, num_moves
    y -= move_size  # move down of center
    num_moves += 1
    display_game()


def setup_game():

    global num_moves, hidden_color, circle_size, move_size

    num_moves = 0
    hidden_color = 'black'

    t.clear()
    s.tracer(False)
    t.hideturtle()
    t.speed('fastest')
    s.title('Hot + Cold')
    s.bgcolor('black')

    try:
        circle_size = int(turtle.numinput('Circle', 'Size of circles (10-100)', minval=10, maxval=100))
        move_size = int(turtle.numinput('Circle', 'Size of move (10-100)', minval=10, maxval=100))
    except:
        circle_size = 50
        move_size = 50

    center_locate()
    set_hide_locate()

    # set up the keys to listen to and what function should be called
    s.onkeypress(debug, "d")
    s.onkeypress(start_game, 'r')
    s.onkeypress(move_home, "h")
    s.onkeypress(move_up, "Up")
    s.onkeypress(move_down, "Down")
    s.onkeypress(move_right, "Right")
    s.onkeypress(move_left, "Left")
    s.listen()  # start listening for keys being pressed


def start_game():
    setup_game()
    display_game()
    s.mainloop()  # Keeps turtle window open until closed


def main():
    """
    s = turtle.Screen()
    t = turtle.Turtle()
    """
    start_game()


# if this is the program starting module, then run the main function
if __name__ == '__main__':
    main()
