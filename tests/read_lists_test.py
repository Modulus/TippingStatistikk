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


        # First row: Numbers
        # Second row: Main numbers
        # Third row: Additional Numbers
        self.new_markup = """
        var sta_dataTable = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48],[3,11,7,5,4,6,6,7,5,8,7,5,9,7,6,9,10,3,8,7,7,5,6,5,11,5,7,9,6,8,9,12,5,9,2,4,8,4,8,4,7,8,8,2,9,10,3,4],[2,1,1,2,0,1,2,2,6,1,0,4,1,0,0,0,4,5,0,4,2,4,2,4,1,2,2,0,1,2,3,3,0,3,2,3,2,6,1,3,2,3,4,4,2,3,3,3]];

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


