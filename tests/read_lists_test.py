from datetime import datetime
from unittest import TestCase
from mock import Mock
from requests import request
import requests_mock
from utilities.number_extractor import read_lists

__author__ = 'Modulus'

""" This needs to be fixed"""
class ReadListsTest(object):
    def setUp(self):
        self.markup = """<script type="text/javascript">
            <!--

            // *** Set game type. ***
            sta_game = GAME_LOTTO;

            // *** Fill the data table. ***
            // Table containing statistical information. Two dimensional array with the following format:
                // 1. index
            //   number : int
            //   times_main : int
            //   times_additional : int
            // 2. index
            //   number index
            var sta_dataTable = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34],[11,8,12,6,5,13,12,13,6,9,11,14,16,13,15,10,8,10,5,9,10,6,12,14,16,11,14,15,8,12,10,10,10,10],[4,6,2,7,7,6,7,4,5,5,8,7,5,5,4,5,5,7,2,6,0,7,3,5,3,6,0,3,1,4,0,6,6,5]];

            // -->
            </script>
            """
        self.expected_table = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
             30, 31, 32, 33, 34],
            [11, 8, 12, 6, 5, 13, 12, 13, 6, 9, 11, 14, 16, 13, 15, 10, 8, 10, 5, 9, 10, 6, 12, 14, 16, 11, 14, 15, 8,
             12, 10, 10, 10, 10],
            [4, 6, 2, 7, 7, 6, 7, 4, 5, 5, 8, 7, 5, 5, 4, 5, 5, 7, 2, 6, 0, 7, 3, 5, 3, 6, 0, 3, 1, 4, 0, 6, 6, 5]]
        session = request.Session()
        adapter = requests_mock.Adapter()
        adapter.register_uri("GET")
        request.get = Mock(return_value=self.fake_stream)

    def test_viking_url(self):
        url = "https://www.norsk-tipping.no/miscellaneous/getNumberStatisticsVikingLotto.htm"
        data = read_lists(datetime.now(), datetime.now(), url)

        self.assertIsNotNone(data)
        self.assertEquals(self.expected_table, data)

    def test_lotto_url(self):
        url = "https://www.norsk-tipping.no/miscellaneous/getNumberStatisticsLotto.htm"
        data = read_lists(datetime.now(), datetime.now(), url)

        self.assertIsNotNone(data)
        self.assertEquals(self.expected_table, data)

    def test_extra_url(self):
        url = "https://www.norsk-tipping.no/miscellaneous/getNumberStatisticsExtra.htm"
        data = read_lists(datetime.now(), datetime.now(), url)

        self.assertIsNotNone(data)
        self.assertEquals(self.expected_table, data)

    def test_keno_url(self):
        url = "https://www.norsk-tipping.no/miscellaneous/getNumberStatisticsKeno.htm"
        data = read_lists(datetime.now(), datetime.now(), url)

        self.assertIsNotNone(data)
        self.assertEquals(self.expected_table, data)


