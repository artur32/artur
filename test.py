import unittest
import main


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(main.print_string("bab"), "bab")

    def test_something(self):
        self.assertEqual(main.is_palindrome("hello"), "olleh")

    def test_something(self):
        self.assertEqual(main.count_vowels("пиво"), 1)
    def test_something(self):
        self.assertEqual(main.removeduplicates("класс", "с")