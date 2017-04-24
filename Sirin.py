class Sirin:
    """ Sirin representation class """

    def __init__(self, start):
        # list of  squares represent Sirin's body
        self.sirin = [start]

    def __contains__(self, space):
        """ return square of body """

        return space in self.sirin

    def advance(self, space):
        """ step forward """

        self.sirin.pop(0)
        self.sirin.append(space)

    def grow(self, space):
        """ enlarge by 1 and step forward"""

        self.sirin.append(space)

    def head(self):
        """ get the head square"""

        return self.sirin[-1]
