from collections import Counter
from datetime import datetime
import functools
import json
import urllib2
from itertools import permutations
import operator
from time import mktime
import zlib
import requests
from utilities.date_utils import dateformat


__author__ = 'Modulus'


def create_list(ex_data):
    """
    :param ex_data: A fucked up string, that needs to be converted to three list, that again contains lists
    :return: Returns these three nested lists as three lists of ints in a list.
    """
    step1 = ex_data.split("]")
    all_lists = []
    for element in step1:
        element = element.replace("[", "")
        element = element.replace("]", "")
        all_lists.append(element.split(","))

    # Map these string lists to lists of ints
    m_list = []
    for curr_list in all_lists:
        # Remove empty values in list before converting
        if '' in curr_list:
            curr_list.remove('')
        res = map(int, curr_list)
        if res:
            m_list.append(res)

    return m_list

def read_lists(start_date, end_date, url):
    """
    The first array has the actual numbers,
    The second array is amount of times this number has been selected
    The third array is how many times this number has been additional numbers
    """

    list_found = False
    finished_reading = False

    if start_date and type(start_date) != datetime:
        start = datetime.fromtimestamp(mktime(start_date))
        end = datetime.fromtimestamp(mktime(end_date))
    elif start_date and type(start_date) == datetime:
        start = start_date
        end = end_date

    start_date_string = "{0}.{1}.{2}".format(start.day, start.month, start.year)
    end_date_string = "{0}.{1}.{2}".format(end.day, end.month, end.year)

    base_url = "{0}?fromDate={1}&toDate={2}&".format(url, start_date_string, end_date_string)

    data = requests.get(base_url)

    ex_data = ""
    for line in data:
        if "sta_dataTable" in line:
            list_found = True
            json_array = line.split("=")[1]
            json_array = json_array.replace(";", "")
            ex_data += (json_array)
        elif list_found and not finished_reading:

            if "]]" in line:
                end_index = line.index("]]")
                ex_data += (line[:end_index])
                finished_reading = True
                return create_list(ex_data)
            else:
                ex_data += line

    raise RuntimeError("No data found")


def unique_filter(func):
    """This decorator is used on the extracted permutations to filter all the unique values in
    the permutation. Since repetition will happen, because of its based on position and not value"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        extracted_unique = []
        if result and type(result) == permutations:

            for element in result:
                sorted_values = sorted(element)
                if not sorted_values in extracted_unique:
                    extracted_unique.append(sorted_values)
            return extracted_unique
        else:
            raise TypeError("You need to give itertools.permutations as parameter")
    return wrapper


def extract_most_common(amount, start_date, end_date, url):
    """This function extract all the chosen amounts of most common numbers from the given url"""

    lists = read_lists(start_date=start_date,
                       end_date=end_date, url=url)

    if lists:
        numbers = {}
        for index, value in enumerate(lists[1]):
            numbers[index + 1] = value

        counter = Counter(numbers)

        """Extract the actual numbers and return them"""
        return [e[0] for e in counter.most_common(amount)]
    else:
        return []


def extract_least_common(amount, start_date, end_date, url):
    """This function will extract all the least picked numbers for the given url, start and end date"""
    lists = read_lists(start_date=start_date,
                       end_date=end_date, url=url)
    numbers = {}
    for index, value in enumerate(lists[1]):
        numbers[index + 1] = value

    counter = Counter(numbers)
    numbers = counter.most_common()

    #Sort numbers by value (amount the currect number has been picked
    sorted_numbers = sorted(iter(numbers), key=operator.itemgetter(1), reverse=False)

    return [e[0] for e in sorted_numbers[0:amount]]


@unique_filter
def extract(length, amount, start_date, end_date, url, most_common=True):
    """This functions will return all position permutations of the url given
        amount will be the count of numbers per resulting row in extracted data to be used for
        generating permutations.
        length will be the length of each row in the finished permutation.
        Keep in mind that repeating permutations will occur, since it is based on positions and not
        values.
    """

    if most_common:
        all_numbers = extract_most_common(amount, start_date, end_date, url)
    else:
        all_numbers = extract_least_common(amount, start_date, end_date, url)

    perm = permutations(all_numbers, length)

    return perm