from collections import Counter
import json
import urllib2
from itertools import permutations

from utilities.date_utils import dateformat


__author__ = 'Modulus'


def read_lists(start_date, end_date, url):
    """
    The first array has the actual numbers,
    The second array is amount of times this number has been selected
    The third array is how many times this number has been additional numbers
    """

    base_url = url + "?fromDate={0}&toDate={1}&".format(start_date, end_date)

    stream = urllib2.urlopen(base_url)

    content = stream.readlines()

    for line in content:
        if "var sta_dataTable" in line:
            json_array = line.split("=")[1]
            json_array = json_array.replace(";", "")
            return json.loads(json_array)


def extract(amount, start_date, end_date, url):
    """This function extract all the chosen amounts of most common numbers from the given url"""
    lists = read_lists(start_date=start_date.strftime(dateformat()),
                           end_date=end_date.strftime(dateformat()), url=url)
    numbers = {}
    for index, value in enumerate(lists[1]):
        numbers[index + 1] = value

    counter = Counter(numbers)

    """Extract the actual numbers and return them"""
    return [e[0] for e in counter.most_common(amount)]


def extract_permutations(length, amount, start_date, end_date, url):
    """This functions will return all position permutations of the url given
        amount will be the count of numbers per resulting row in extracted data to be used for
        generating permutations.
        length will be the length of each row in the finished permutation.
        Keep in mind that repeating permutations will occur, since it is based on positions and not
        values.
    """
    all_numbers = extract(amount, start_date, end_date, url)

    perm = permutations(all_numbers, length)

    return perm


def extract_uniques(data):
    """This function is unused on the extracted permutations to extract all the unique values in
    the permutation. Since repetition will happen, because of its based on position and not value"""
    if data and type(data) == permutations:
        extracted_uniques = []
        for element in data:
            sorted_values = sorted(element)
            if not sorted_values in extracted_uniques:
                extracted_uniques.append(sorted_values)
        return extracted_uniques
    else:
        raise TypeError("You need to give itertools.permutations as parameter")

