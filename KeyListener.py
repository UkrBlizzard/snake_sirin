import msvcrt
from threading import Thread
from Vector import Vector


class KeyListener(Thread):
    """ thread class to get keyboard input """

    def __init__(self):
        # current direction
        self.vector = None
        # boolean pause indication
        self.pause = False
        # boolean listen to quit
        self.quit = False
        # boolean state indication of this thread
        self.active = False
        # call to constructor
        super(KeyListener, self).__init__()

    def run(self):
        self.active = True

        while self.active:
            key = msvcrt.getwch()

            # get a direction
            if key == "\xe0":
                key = msvcrt.getwch()

                if key in Vector.SIDES:
                    self.vector = key
            # pause toggle
            elif key == " ":
                self.pause = not self.pause
            # quit toggle
            elif key == "q":
                self.quit = True

    def end(self):
        """ end of thread """
        self.active = False
