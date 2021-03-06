from collections import Counter
from datetime import datetime
from unittest import TestCase
from mock import Mock
from utilities import number_extractor as extractor

__author__ = 'Modulus'


class ExtractTest(TestCase):

    def setUp(self):
        self.lists = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
              30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48], [132, 167, 154, 130, 135, 132
                , 144, 144, 143, 114, 140, 122, 138, 131, 115, 144, 140, 131, 122, 120, 147, 132, 145, 136, 137, 135, 157
        , 135, 117, 136, 135, 145, 118, 142, 131, 149, 149, 128, 137, 135, 164, 154, 139, 151, 136, 136, 130, 128],
             [49, 45, 38, 51, 47, 50, 53, 40, 44, 56, 60, 49, 60, 48, 43, 41, 47, 48, 49, 46, 42, 48, 46, 53, 43, 50, 51
                 , 45, 42, 62, 49, 49, 50, 49, 37, 35, 31, 49, 51, 42, 48, 46, 49, 43, 33, 29, 28, 30]]

    def test_extract(self):
        start_date = datetime.date(datetime(1986, 1, 1))

        current_date = datetime.date(datetime(2014, 4, 19))

        extractor.read_lists = Mock(return_value=self.lists)
        numbers = extractor.extract_most_common(7, start_date, current_date, "https://www.fjas.no")

        self.assertListEqual([2, 41, 27, 3, 42, 44, 36], numbers)


    def test_most_common(self):
        data = {1: 300, 2: 1, 4: 200, 7: 150, 1000: 23, 9999: 87, 999123992: 123}
        counter = Counter(data)
        result = counter.most_common(3)

        elements = []

        for element in result:
            elements.append(element[0])

        self.assertEquals([1, 4, 7], elements)

    def test_extract_least_common(self):
        start_date = datetime.date(datetime(1986, 1, 1))

        current_date = datetime.date(datetime(2014, 4, 19))

        extractor.read_lists = Mock(return_value=self.lists)
        numbers = extractor.extract_least_common(7, start_date, current_date, "https://www.fjas.no")

        self.assertListEqual([10, 15, 29, 33, 20, 12, 19], numbers)

    def test_exract_most_common_flag_false(self):
        start_date = datetime.date(datetime(1986, 1, 1))

        current_date = datetime.date(datetime(2014, 4, 19))

        extractor.read_lists = Mock(return_value=self.lists)
        numbers = extractor.extract(7, 7, start_date, current_date, "https://www.fjas.no", most_common=False)

        self.assertListEqual([[10, 12, 15, 19, 20, 29, 33]], numbers)

    def test_extract_most_common_flag_true(self):
        start_date = datetime.date(datetime(1986, 1, 1))

        current_date = datetime.date(datetime(2014, 4, 19))

        extractor.read_lists = Mock(return_value=self.lists)
        numbers = extractor.extract(7, 7, start_date, current_date, "https://www.fjas.no", most_common=True)

        self.assertListEqual([[2, 3, 27, 36, 41, 42, 44]], numbers)

