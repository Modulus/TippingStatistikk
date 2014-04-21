from unittest import TestCase
from utilities.number_extractor import extract_uniques

__author__ = 'Modulus'

class ExtractUniquesTest(TestCase):


    def test_extract_uniques_wrongtype(self):
        self.assertRaises(TypeError, extract_uniques, "doh!")