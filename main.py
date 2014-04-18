from datetime import datetime
from itertools import permutations

__author__ = 'Modulus'

from utilities.number_extractor import extract, extract_permuatations


def run():
    start_date = datetime.date(datetime(1986, 01, 01))

    current_date = datetime.now()

    numbers = extract(7, start_date, current_date)
    print(numbers)

    extracted_uniques = []
    for permutation in extract_permuatations(7, 10, start_date, current_date):
        sorted_values = sorted(permutation)
        if not sorted_values in extracted_uniques:
            extracted_uniques.append(sorted_values)

    for value in extracted_uniques:
        print(value)

if __name__ == "__main__":
    run()