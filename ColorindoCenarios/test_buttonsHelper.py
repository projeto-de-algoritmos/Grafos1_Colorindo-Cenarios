import unittest
from Button import Button
import buttonsHelper
from colors import STANDARD_COLOR, RED, GREEN, WALL

class TestBoard(unittest.TestCase):

    def setUp(self):
        draw_button = Button(STANDARD_COLOR, 1095, 5, 460, 205, "DRAW")
        red_button = Button(RED, 1095, 215, 225, 205, "RED")
        green_button = Button(GREEN, 1330, 215, 225, 205, "GREEN")

        self.buttons = [draw_button,red_button, green_button]

    def test_buttons_on_click(self):
        self.assertEqual(buttonsHelper.buttons_on_click(1115,150,STANDARD_COLOR,self.buttons),WALL)
        self.assertEqual(buttonsHelper.buttons_on_click(10,10,WALL,self.buttons),WALL)
        self.assertNotEqual(buttonsHelper.buttons_on_click(1115,150,RED,self.buttons),RED)

        self.assertEqual(buttonsHelper.buttons_on_click(1096,315,STANDARD_COLOR,self.buttons),RED)
        self.assertEqual(buttonsHelper.buttons_on_click(100,315,RED,self.buttons),RED)
        self.assertNotEqual(buttonsHelper.buttons_on_click(100,315,STANDARD_COLOR,self.buttons),RED)

        self.assertEqual(buttonsHelper.buttons_on_click(1500,400,STANDARD_COLOR,self.buttons),GREEN)
        self.assertEqual(buttonsHelper.buttons_on_click(100,315,GREEN,self.buttons),GREEN)
        self.assertNotEqual(buttonsHelper.buttons_on_click(100,315,STANDARD_COLOR,self.buttons),GREEN)


if __name__ == '__main__':
    unittest.main()