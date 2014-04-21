from collections import Counter
import json
import urllib2
from itertools import permutations

__author__ = 'Modulus'


def generate_lists(start_date, end_date, url):

    base_url = url + "?fromDate={0}&toDate={1}&".format(start_date, end_date)

    stream = urllib2.urlopen(base_url)

    content = stream.readlines()

    """
    The first array has the actual numbers,
    The second array is amount of times this number has been selected
    The third array is how many times this number has been additional numbers
    """

    for line in content:
        if "var sta_dataTable" in line:
            json_array = line.split("=")[1]
            json_array = json_array.replace(";", "")
            return json.loads(json_array)


def dateformat():
    return "%d.%m.%Y"


def extract(amount, start_date, end_date, url):
    lists = generate_lists(start_date=start_date.strftime(dateformat()),
                           end_date=end_date.strftime(dateformat()), url=url)
    numbers = {}
    for index, value in enumerate(lists[1]):
        numbers[index + 1] = value

    counter = Counter(numbers)

    """Extract the actual numbers and return them"""
    return [e[0] for e in counter.most_common(amount)]

"""Get the name of the current game beeing displayed"""
def get_name(url):
    if url:
        elements = url.split("/")
        page = elements[-1]

        """ Remove prefix and suffix (.htm)"""
        name = page[len("getNumberStatistics"):-4]

        return name
    else:
        return None

def extract_permuatations(length, amount, start_date, end_date, url):
    all_numbers = extract(amount, start_date, end_date, url)

    perm = permutations(all_numbers, length)

    return perm


def extract_uniques(data):
    if data and type(data) == permutations:
        extracted_uniques = []
        for element in data:
            sorted_values = sorted(element)
            if not sorted_values in extracted_uniques:
                extracted_uniques.append(sorted_values)
        return extracted_uniques
    else:
        raise TypeError("You need to give itertools.permutations as parameter")

