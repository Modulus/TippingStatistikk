from datetime import datetime
from unittest import TestCase
from utilities import date_utils

__author__ = 'Modulus'


class MainTests(TestCase):

    def setUp(self):
        self.start = datetime.date(datetime(1986, 1, 1))
        self.end = datetime.date(datetime(2014, 3, 24))

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

    def test_saturday(self):
        saturday = datetime.date(datetime(2015, 7, 25))

        self.assertEquals(6, saturday.isoweekday())

    def test_get_all_saturdays(self):
        days = date_utils.get_saturdays()
        self.assertIsNotNone(days)
        self.assertTrue(len(days) >= 1248)
        for day in days:
            self.assertEqual(day.isoweekday(), 6, "A date that is not a saturday is present")


