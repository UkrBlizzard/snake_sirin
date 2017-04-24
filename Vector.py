class Vector:
    """ representation of directions on a field """

    UP = "H"
    RIGHT = "M"
    DOWN = "P"
    LEFT = "K"
    SIDES = ["H", "M", "P", "K"]

    @staticmethod
    def reverse(vector):
        """ return the opposite of the current direction """

        if vector == Vector.UP:
            return Vector.DOWN
        if vector == Vector.RIGHT:
            return Vector.LEFT
        if vector == Vector.DOWN:
            return Vector.UP
        if vector == Vector.LEFT:
            return Vector.RIGHT
