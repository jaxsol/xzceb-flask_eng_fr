from unittest import TestCase
from unittest import main
from translator import french_to_english
from translator import english_to_french

class TestFrenchToEnglish(TestCase):
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
    def test2(self):
        self.assertNotEqual(french_to_english('Bien'), 'Bad')

class TestEnglishToFrench(TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    def test2(self):
        self.assertNotEqual(english_to_french('Good'), 'Mauvais')

main()
