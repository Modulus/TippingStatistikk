from collections import Counter
from datetime import datetime
import json
import operator

__author__ = 'Modulus'
import urllib2


def dateformat():
    return "%d.%m.%Y"


def run():
    start_date = datetime.date(datetime(1986, 01, 01))

    current_date = datetime.now()

    lists = generate_lists(start_date.strftime(dateformat()), current_date.strftime(dateformat()))
    numbers = {}
    for index, value in enumerate(lists[1]):
        numbers[index+1] = value

    # elements = dict(sorted(numbers.iteritems(), key=operator.itemgetter(0), reverse=True)[0:5])

    counter = Counter(numbers)

    #Highest values
    print counter.most_common(6)

    print max(lists[1])

    print numbers


def generate_lists(start_date, end_date):
    base_url = "https://www.norsk-tipping.no/miscellaneous/getNumberStatisticsVikingLotto.htm?fromDate={0}&toDate={1}&".format(start_date, end_date)

    url = urllib2.urlopen(base_url)

    content = url.readlines()

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


if __name__ == "__main__":
    run()