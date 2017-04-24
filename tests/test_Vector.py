import unittest
from Vector import Vector


class VectorTests(unittest.TestCase):

    def test_reverse_return(self):
        """ values transmission testing """
        key = Vector.SIDES
        directions = [Vector.UP, Vector.RIGHT, Vector.DOWN, Vector.LEFT]
        for Vector.reverse in directions:
            rev = Vector.reverse
            self.failUnless(rev in key)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
