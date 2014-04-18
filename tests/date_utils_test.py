from datetime import datetime
from unittest import TestCase
from dateutil.relativedelta import relativedelta
from utilities.date_utils import DateUtils

__author__ = 'Modulus'


class MainTests(TestCase):

    def setUp(self):
        self.start = datetime.date(datetime(1986, 01, 01))
        self.end = datetime.date(datetime(2014, 03, 24))

    def test_timedelta(self):
        dates = DateUtils.get_dates(self.start)
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

