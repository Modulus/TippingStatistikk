from datetime import datetime
from utilities.name_utils import get_game_name

__author__ = 'Modulus'

from utilities.number_extractor import extract


def run():
    start_date = datetime.date(datetime(2010, 01, 01))

    current_date = datetime.now()

    urls = [
        "https://www.norsk-tipping.no/miscellaneous/getNumberStatisticsLotto.htm",
        "https://www.norsk-tipping.no/miscellaneous/getNumberStatisticsVikingLotto.htm",
        "https://www.norsk-tipping.no/miscellaneous/getNumberStatisticsExtra.htm",
        "https://www.norsk-tipping.no/miscellaneous/getNumberStatisticsKeno.htm"
    ]

    for index, url in enumerate(urls):

        print(" {0} numbers".format(get_game_name(url)))

        permutations = extract(7, 8, start_date, current_date, url)

        for value in permutations:
            print(value)

        print("\n")

if __name__ == "__main__":
    run()