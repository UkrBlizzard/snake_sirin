class Space:
    """ class of rectangle field """

    def __init__(self, x, y, num):
        # int coordinate for x
        self.x = x
        # int coordinate for y
        self.y = y
        # int
        self.num = num

    def __eq__(self, other):
        """ test the equality between two spaces """
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        """ hashes a space """
        return self.num * self.y + self.x

    def up(self):
        """ return the space above it """
        return Space(self.x + 1, self.y, self.num)

    def left(self):
        """ return the space to the left of it """
        return Space(self.x, self.y - 1, self.num)

    def down(self):
        """ return the space below it """
        return Space(self.x - 1, self.y, self.num)

    def right(self):
        """ return the space to the right of it """
        return Space(self.x, self.y + 1, self.num)
