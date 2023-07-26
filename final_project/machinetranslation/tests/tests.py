'''Test for Translator'''
import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    """Class for English test"""

    def test_1(self):
        '''Test trasnslation of English to French'''
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Hello'), 'hello')
        
class TestFrenchToEnglish(unittest.TestCase):
    """Class for french test"""

    def test_1(self):
        '''Test for translation of French to English'''
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')

unittest.main()
