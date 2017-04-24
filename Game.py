import platform
import os
import time
import random
from Vector import Vector
from Sirin import Sirin
from Space import Space
from KeyListener import KeyListener


class Game:
    """ the game """

    def __init__(self, height, width, speed):
        # int height of field
        self.height = height
        # int width of field
        self.width = width
        # float frame rate delay
        self.speed = speed
        # int score that is length of Sirin's tail
        self.score = 0
        # Sirin starting position
        self.sirin = Sirin(Space(height // 2, width // 2, self.width))
        # cell representing egg
        self.egg = None

    def play(self):
        """ play the game """

        previous_vector = None
        listener = KeyListener()

        # start listening
        listener.start()
        # !!!!!!
        clear_screen = "cls" if platform.system() == "Windows" else "clear"
        # place the first egg
        self.place_egg()

        # game in loop
        while not self.game_over() and not listener.quit:
            # show the game
            os.system(clear_screen)
            self.display(listener.pause)

            # movement delay - Sirin's speed
            time.sleep(self.speed)

            # direction update
            current_vector = listener.vector

            # prevent Sirin from instant direction reverse
            if current_vector == Vector.reverse(previous_vector):
                current_vector = previous_vector

            # pause check to move
            if not listener.pause:
                self.move(current_vector)

            # store previous direction
            previous_vector = current_vector

        # end the key listener
        listener.end()

        # pause for 1 second
        time.sleep(1)

    def move(self, current_vector):
        """ moves """

        next_move = self.next_space(current_vector)

        if next_move:
            # Sirin gets an egg and grows by 1
            if next_move == self.egg:
                self.sirin.grow(next_move)
                self.place_egg()
                self.score += 1
            # Sirin move to next position
            else:
                self.sirin.advance(next_move)

    def display(self, pause):
        """ show the game """

        # string to visual output
        string = ""

        pause_string = "| PAUSED |"
        pause_string = pause_string if len(pause_string) + 2 <= self.width and pause else ""
        string += "#" + pause_string.center(self.width, "-") + "#\n"

        for row in reversed(range(self.height)):
            string += "|"
            for column in range(self.width):
                # print Sirin
                if Space(row, column, self.width) in self.sirin:
                    string += "S"
                # print egg
                elif Space(row, column, self.width) == self.egg:
                    string += "O"
                # print empty space
                else:
                    string += " "
            string += "|\n"

        # show the score as part of bottom border
        score_string = "| SCORE: " + str(self.score) + " |"
        # check for SCORE to match inside bottom border
        score_string = score_string if len(score_string) + 2 <= self.width else "| " + str(self.score) + " |"
        string += "#" + score_string.center(self.width, "-") + "#\n"

        print(string)

    def game_over(self):
        """ return if the game is over """

        head = self.sirin.head()
        # hit the border
        if head.x < 0 or head.x >= self.height or head.y < 0 or head.y >= self.width:
            return True
        # Sirin eat itself ( Uroboros )
        elif head in self.sirin.sirin[:-1]:
            return True
        else:
            return False

    def next_space(self, current_vector):
        """ return next space based on Sirin's head direction """

        head = self.sirin.head()

        if current_vector == Vector.UP:
            return head.up()
        elif current_vector == Vector.RIGHT:
            return head.right()
        elif current_vector == Vector.DOWN:
            return head.down()
        elif current_vector == Vector.LEFT:
            return head.left()

    def place_egg(self):
        """ place the egg by random on the field """

        x = random.randint(0, self.height - 1)
        y = random.randint(0, self.width - 1)

        egg = Space(x, y, self.width)

        # check to place egg on empty space
        while egg in self.sirin:
            x = random.randint(0, self.height - 1)
            y = random.randint(0, self.width - 1)

            egg = Space(x, y, self.width)

        self.egg = egg
