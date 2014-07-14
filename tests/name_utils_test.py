from unittest import TestCase
from utilities import name_utils

__author__ = 'Modulus'


class NameUtilsTest(TestCase):

    def test_viking_url_get_name(self):
        name = name_utils.get_game_name("https://www.norsk-tipping.no/miscellaneous/getNumberStatisticsVikingLotto.htm")
        self.assertEquals("VikingLotto", name)

    def test_lotto_url_get_name(self):
        name = name_utils.get_game_name("https://www.norsk-tipping.no/miscellaneous/getNumberStatisticsLotto.htm")
        self.assertEquals("Lotto", name)

    def test_extra_get_name(self):
        name = name_utils.get_game_name("https://www.norsk-tipping.no/miscellaneous/getNumberStatisticsExtra.htm")
        self.assertEquals("Extra", name)

    def test_keno_get_name(self):
        name = name_utils.get_game_name("https://www.norsk-tipping.no/miscellaneous/getNumberStatisticsKeno.htm")
        self.assertEquals("Keno", name)