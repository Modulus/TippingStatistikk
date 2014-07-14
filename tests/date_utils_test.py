from datetime import datetime
from unittest import TestCase
from utilities import date_utils

__author__ = 'Modulus'


class MainTests(TestCase):

    def setUp(self):
        self.start = datetime.date(datetime(1986, 01, 01))
        self.end = datetime.date(datetime(2014, 03, 24))

    def test_timedelta(self):
        dates = date_utils.DateUtils.get_dates(self.start)
        self.assertIsNotNone(dates)
        self.assertNotEquals([], dates)
        self.assertEquals(9, len(dates))

        self.assertEquals(1986, dates[0].year)
        self.assertEquals(1996, dates[1].year)
        self.assertEquals(2006, dates[2].year)
        self.assertEquals(1992, dates[3].year)
        self.assertEquals(1998, dates[4].year)
        self.assertEquals(2004, dates[5].year)
        self.assertEquals(2010, dates[6].year)
        self.assertEquals(2016, dates[7].year)
        self.assertEquals(2022, dates[8].year)

    def test_sum(self):
        sum = 0
        for i in range(0, 10):
            sum += i

        print sum


