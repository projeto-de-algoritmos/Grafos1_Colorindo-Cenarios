import unittest
from Button import Button
from colors import STANDARD_COLOR, RED, GREEN

class TestButton(unittest.TestCase):

    def setUp(self):
        self.button1 = Button(STANDARD_COLOR, 1095, 5, 460, 205, "DRAW")
        self.button2 = Button(RED, 1095, 215, 225, 205, "RED")
        self.button3 = Button(GREEN, 1330, 215, 225, 205, "GREEN")

    def test_check(self):
        self.assertTrue(Button.check(self.button1, 1115,150))
        self.assertFalse(Button.check(self.button2, 1115,150))
        self.assertFalse(Button.check(self.button3, 1115,150))

        self.assertTrue(Button.check(self.button2, 1096,315))
        self.assertFalse(Button.check(self.button1, 1096,315))
        self.assertFalse(Button.check(self.button3, 1096,315))

        self.assertTrue(Button.check(self.button3, 1500,400))
        self.assertFalse(Button.check(self.button1, 1500,400))
        self.assertFalse(Button.check(self.button2, 1500,400))

if __name__ == '__main__':
    unittest.main()