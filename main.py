from datetime import datetime
from itertools import permutations

__author__ = 'Modulus'

from utilities.number_extractor import extract_permutations, extract_uniques, get_name


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

        print(" {0} numbers".format(get_name(url)))

        permutations = extract_permutations(7, 8, start_date, current_date, url)

        values = extract_uniques(permutations)

        for value in values:
            print(value)

        print("\n")

if __name__ == "__main__":
    run()