from datetime import datetime
from itertools import permutations

__author__ = 'Modulus'

from utilities.number_extractor import extract_permuatations, extract_uniques


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
        if index == 0:
            print("Lotto numbers")
        elif index == 1:
            print("Viking lotto numbers")
        elif index == 2:
            print("Extra numbers")
        else:
            print("Keno numbers")

        permutations = extract_permuatations(7, 8, start_date, current_date, url)

        values = extract_uniques(permutations)

        for value in values:
            print(value)

        print("\n")

if __name__ == "__main__":
    run()