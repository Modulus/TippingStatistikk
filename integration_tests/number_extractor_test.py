# -*- coding: utf-8 -*-
import time
from unittest import TestCase
from utilities.number_extractor import read_lists

__author__ = 'Modulus'

class NumberExtractor(TestCase):

    def setUp(self):
        self.start_date = time.strptime(u"2004-06-20", "%Y-%m-%d")
        self.end_date = time.strptime(u"2014-05-20", "%Y-%m-%d")
        self.url = 'https://www.norsk-tipping.no/miscellaneous/getNumberStatisticsLotto.htm'


    def test_read_lists(self):
        data = read_lists(start_date=self.start_date, end_date=self.end_date, url=self.url)
        self.assertTrue(len(data) >= 3)

        for element in data:
            self.assertTrue(len(element) > 8)