from collections import Counter
import json
import urllib2
from itertools import permutations

__author__ = 'Modulus'


def generate_lists(start_date, end_date, url):

    base_url = url + "fromDate={0}&toDate={1}&".format(start_date, end_date)

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


def extract(amount, start_date, end_date):
    lists = generate_lists(start_date.strftime(dateformat()), end_date.strftime(dateformat()))
    numbers = {}
    for index, value in enumerate(lists[1]):
        numbers[index + 1] = value

    counter = Counter(numbers)

    print counter.most_common(amount)

    print max(lists[1])

    """Extract the actual numbers and return them"""
    return [e[0] for e in counter.most_common(amount)]


def extract_permuatations(length, amount, start_date, end_date):
    all_numbers = extract(amount, start_date, end_date)

    perm = permutations(all_numbers, length)

    return perm


