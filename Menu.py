import msvcrt
import platform
import os
from Vector import Vector
from Game import Game


def show_menu(option, size, size_height, size_width, game_speed, size_string, game_speed_string):
    """ show the menu """

    if size == 0: size_string = "Basic"
    elif size == 1: size_string = "Custom:  " + str(size_height) + " x  " + str(size_width)
    elif size == 2: size_string = "Custom: >" + str(size_height) + " x  " + str(size_width)
    elif size == 3: size_string = "Custom:  " + str(size_height) + " x >" + str(size_width)

    if game_speed == 0: game_speed_string = "Walk"
    elif game_speed == 1: game_speed_string = "Run"
    elif game_speed == 2: game_speed_string = "Sprint"

    print("SNAKE called SIRIN\n")
    print(">" if option == 0 else " ", "Start")
    print(">" if option == 1 and size <= 1 else " ", "Size ", size_string)
    print(">" if option == 2 else " ", "Speed ", game_speed_string)
    print(">" if option == 3 else " ", "Quit")


def startGame(size, height, width, speed, size_height, size_width, game_speed):
    """ game initialization """

    if size == 0: height, width = 80, 120
    elif size == 1: height, width = size_height, size_width

    if game_speed == 0: speed = 0.08
    if game_speed == 1: speed = 0.04
    if game_speed == 2: speed = 0.02

    game = Game(height, width, speed)
    game.play()


def process_key():
    """ handling user input for menu navigation """

    global option, size, size_height, size_width, game_speed, play, quit

    key = msvcrt.getwch()

    if key == "\xe0":
        key = msvcrt.getwch()

        if key == Vector.UP and option > 0:
            if size == 2:
                size_height += 1
            elif size == 3:
                size_width += 1
            else:
                option -= 1
        elif key == Vector.DOWN and option < 3:
            if size == 2:
                # control minimum value
                if size_height > 10:
                    size_height -= 1
                else:
                    pass
            elif size == 3:
                # control minimum value
                if size_width > 5:
                    size_width -= 1
                else:
                    pass
            else:
                option += 1
        elif key == Vector.LEFT:
            if option == 1 and size > 0:
               size -= 1
            elif option == 2 and 0 < game_speed <= 2:
                game_speed -= 1
        elif key == Vector.RIGHT:
            if option == 1 and size < 3:
               size += 1
            elif option == 2 and 0 <= game_speed < 2:
               game_speed += 1

    elif key == "\r":
        if option == 0:
            play = True
        elif option == 3:
            quit = True

option = 0
size = 0
height = 0
width = 0
speed = 0
game_speed = 0
size_option = 0
# recommend max value for 1920x1080 screen - 59 x 235
size_height = 36
size_width = 64
size_string = ""
game_speed_string = ""
play = False
quit = False
clear_screen = "cls" if platform.system() == "Windows" else "clear"


while not quit:

    # show the menu
    os.system(clear_screen)
    show_menu(option, size, size_height, size_width, game_speed, size_string, game_speed_string)

    # handling user input
    process_key()

    # start the game
    if play:
        startGame(size, height, width, speed, size_height, size_width, game_speed)
        play = False
