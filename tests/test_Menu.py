import unittest
import Menu


class MenuTests(unittest.TestCase):

    def test_menu_show(self):
        menu = 12 # Menu.show_menu(0, 0, 80, 120, 0.08, "Error", "Not Found")
        print("12" if menu == 12 else "13")
        # self.failUnless(Menu.show_menu)
        # self.assertRaises(TypeError, menu.display, False)


def main():
    unittest.main()

if __name__ == '__main__':
    main()