import unittest
from '..translator' import english_to_french, french_to_english


class EnglishToFrenchTest(unittest.TestCase):

    def test_englishToFrench_null_input(self):
        self.assertEqual(english_to_french(''), "No text Provided")

    def test_englishToFrench_input_hello(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')


class FrenchToEnglish(unittest.TestCase):
    def test_frenchToEnglish_null_input(self):
        self.assertEqual(french_to_english(''), "No text Provided")

    def test_frenchToEnglish_input_bonjour(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__ == "__main__":
    unittest.main()