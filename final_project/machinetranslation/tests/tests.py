import unittest

from translator import english_to_french,french_to_english

class TestEnglishToFrench (unittest.TestCase):
    def test1(self):
        
        self.assertMultiLineEqual(english_to_french('hello'), 'Bonjour') # test when 'Hello' is given as input the output is 'Bonjour'
        self.assertNotEqual(english_to_french('Hello'), 'hola')  # test when 'Hello' is given as input the output must not be 'hola'
        self.assertIsNotNone(english_to_french("hello"), "The value is none") #testing that the input is not null
        

class TestFrenchToEnglish (unittest.TestCase):
    def test1(self):
         self.assertMultiLineEqual(french_to_english('chaussures'), 'Shoes') # test when 'des chaussures' is given as input the output is 'shoes'
         self.assertNotEqual(french_to_english('Je te déteste'), 'I love you')  # test when 'Je te déteste' is given as input the output must not be 'I love you'
         self.assertIsNotNone(french_to_english('bonjour'), "the value is none") #testing that the input is not null


unittest.main()